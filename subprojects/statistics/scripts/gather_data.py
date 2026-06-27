#!/usr/bin/python3
"""
Gathers HTTP security headers usage data from the Majestic Top 1M domains list.

Uses asyncio + aiohttp for high-concurrency I/O, batched SQLite writes,
and checkpoint/resume support so interrupted GitHub Actions jobs can continue
from where they left off.
"""
import asyncio
import json
import os
import signal
import sqlite3
import time

import aiohttp

# -------- CONSTANTS ---------

OSHP_SECURITY_HEADERS_FILE_LOCATION = (
    "https://raw.githubusercontent.com/OWASP/www-project-secure-headers/"
    "refs/heads/master/ci/headers_add.json"
)
OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION = "oshp_headers_extra_to_include.txt"
NUMBER_OF_DOMAINS_TO_TAKE = 250000

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
)

DATA_FOLDER = "../data"
DATA_DB_FILE = f"{DATA_FOLDER}/data.db"
CSV_INPUT_FILE = f"{DATA_FOLDER}/input.csv"
MAJESTIC_CSV_URL = "http://downloads.majestic.com/majestic_million.csv"
CHECKPOINT_FILE = f"{DATA_FOLDER}/checkpoint.json"

# Explicit nameservers with round-robin rotation nameservers replace 
# the GHA runner's internal DNS, which gets rate-limited and produces 
# Timeout while contacting DNS servers.
#
# 8.8.8.8 -> Google Public DNS. One of the most widely used public DNS services.
# 1.1.1.1 -> Cloudflare DNS. Known for speed and privacy-focused policies.
# 9.9.9.9 -> Quad9 DNS. Includes threat intelligence feeds to block many malicious domains.
# 208.67.222.222 -> OpenDNS (owned by Cisco). Offers filtering and security features.
NAMESERVERS = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222"]

CONCURRENCY = 200

# HTTPS timeouts. sock_connect covers only the TCP handshake, so requests
# waiting for a free pool slot don't burn the budget (aiohttp issue #10313).
# The total timeout is still needed as a hard ceiling over DNS + TLS + body.
TIMEOUT_CONNECT = 5    # TCP handshake
TIMEOUT_READ    = 10   # idle time between response chunks
TIMEOUT_TOTAL   = 20   # DNS + TCP + TLS + body combined

# Simliar to HTTPS timeouts but with a shorter budget for HTTP. HTTPS already consumed a lot of time.
TIMEOUT_HTTP_FALLBACK_CONNECT = 3
TIMEOUT_HTTP_FALLBACK_READ    = 7
TIMEOUT_HTTP_FALLBACK_TOTAL   = 15

# After every N domains, pause briefly so any temporarily rate-limited IPs
# (CDNs recognising the GHA runner) have a window to reset.
RATE_LIMIT_PAUSE_DOMAIN_LIMIT = 10000
RATE_LIMIT_PAUSE_SECS         = 5.0

BATCH_SIZE = 500
CHECKPOINT_INTERVAL = 10000   # persist checkpoint every N domains
PROGRESS_INTERVAL = 5000      # print progress every N domains

REQ_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
}

# ---------------


_shutdown_requested = False


def _request_shutdown(signum, frame):
    """Signal handler — set flag so the main loop exits gracefully."""
    global _shutdown_requested
    _shutdown_requested = True
    print(f"\n[!] Shutdown signal received (signal {signum}), finishing current batch...")


# ------- Checkpoint helpers ------

def load_checkpoint() -> int:
    """Return the last successfully flushed domain index, or 0 if none exists."""
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("last_index", 0)
        except (json.JSONDecodeError, KeyError):
            pass
    return 0


def save_checkpoint(last_index: int):
    """Persist the index of the last domain batch flushed to the DB."""
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            {"last_index": last_index, "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())},
            f,
        )


def clear_checkpoint():
    """Remove the checkpoint file after a successful full run."""
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)


# -------- SQLite helpers --------

def init_db(resume: bool = False):
    """
    Initialise the stats table.
    When not resuming, wipe any existing rows so each full run starts clean.
    """
    with sqlite3.connect(DATA_DB_FILE) as conn:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute(
            "CREATE TABLE IF NOT EXISTS stats "
            "(id integer PRIMARY KEY, domain text, http_header_name text, http_header_value text);"
        )
        if not resume:
            conn.execute("DELETE FROM stats;")
        conn.commit()


def flush_to_db(records: list):
    """Batch-insert (domain, header_name, header_value) records in one transaction."""
    if not records:
        return
    with sqlite3.connect(DATA_DB_FILE, timeout=60) as conn:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.executemany(
            "INSERT INTO stats (domain, http_header_name, http_header_value) VALUES (?, ?, ?);",
            records,
        )
        conn.commit()


def get_record_count() -> int:
    """Return the total number of rows currently in the stats table."""
    with sqlite3.connect(DATA_DB_FILE) as conn:
        row = conn.execute("SELECT max(id) FROM stats").fetchone()
        return row[0] if row and row[0] else 0


# -------- Load input --------

async def load_security_headers(session: aiohttp.ClientSession) -> list:
    """
    Fetch the OSHP security-headers list from GitHub and merge with the local
    extras file.
    Returns a sorted, deduplicated list of lowercase header names.
    """
    headers = []

    async with session.get(
        OSHP_SECURITY_HEADERS_FILE_LOCATION,
        timeout=aiohttp.ClientTimeout(total=15),
    ) as resp:
        if resp.status != 200:
            raise RuntimeError(f"Failed to fetch OSHP headers: HTTP {resp.status}")
        data = await resp.json(content_type=None)
        for h in data["headers"]:
            headers.append(h["name"].lower())

    if os.path.exists(OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION):
        with open(OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION, "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip().lower()
                if name:
                    headers.append(name)

    return set(headers)


async def get_input_csv(session: aiohttp.ClientSession):
    """
    Download and parse the Majestic Top 1M CSV if the local input file is missing.
    Extracts the rank and domain columns to match the expected format.
    """
    
    # Skip downloading if the file exists. This speeds up local development
    # and ensures resumed checkpoint runs use the exact same dataset.
    if os.path.exists(CSV_INPUT_FILE):
        return

    print(f"[+] {CSV_INPUT_FILE} not found. Downloading Majestic Top 1M CSV...")
    os.makedirs(os.path.dirname(CSV_INPUT_FILE), exist_ok=True)

    async with session.get(MAJESTIC_CSV_URL, timeout=aiohttp.ClientTimeout(total=300)) as resp:
        if resp.status != 200:
            raise RuntimeError(f"Failed to fetch Majestic CSV: HTTP {resp.status}")
        
        with open(CSV_INPUT_FILE, "w", encoding="utf-8") as out_f:
            # Skip the first header line
            await resp.content.readline()
            
            async for line in resp.content:
                decoded_line = line.decode('utf-8', errors='ignore').strip()
                if not decoded_line:
                    continue
                parts = decoded_line.split(',')
                if len(parts) >= 3:
                    out_f.write(f"{parts[0]},{parts[2]}\n")

    print(f"[+] Successfully generated {CSV_INPUT_FILE}")


def load_domains(filepath: str, limit: int) -> list:
    """
    Read up to *limit* domain names from the Majestic CSV file.
    Each CSV row is expected to be `rank,domain[,...]`; only the domain column is kept.
    """
    domains = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",", 1)
            if len(parts) == 2:
                domains.append(parts[1].strip())
            if len(domains) >= limit:
                break

    return domains


async def _aiohttp_fetch(
    session: aiohttp.ClientSession,
    url: str,
    security_headers: set,
    connect_timeout: int,
    read_timeout: int,
    total_timeout: int,
) -> list | None:
    """
    GET *url* and return a list of (header_name, value) pairs for any
    security headers present.  Returns None on any network/HTTP error.

    Uses sock_connect (not connect) so the timeout applies only to the TCP
    handshake — not to time spent waiting for a free slot in the connection
    pool (aiohttp issue #10313).
    """
    timeout = aiohttp.ClientTimeout(total=total_timeout, sock_connect=connect_timeout, sock_read=read_timeout)
    try:
        async with session.get(url, timeout=timeout, allow_redirects=True, ssl=False) as resp:
            return [
                (header.lower(), value.encode("utf-8", errors="ignore").decode("utf-8"))
                for header, value in resp.headers.items()
                if header.lower() in security_headers
            ]
    except Exception as e:
        print(f"[-] Error for URL '{url}' with message: {str(e)}")
        return None


async def fetch_headers(
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    domain: str,
    security_headers: set,
) -> list:
    """
    Fetch security headers for *domain*, trying HTTPS first then plain HTTP.
    Returns a list of (domain, header_name, header_value) tuples.
    Yields a single (domain, None, None) entry when the site is unreachable
    or exposes no tracked headers.
    """
    async with semaphore:
        result = await _aiohttp_fetch(session, f"https://{domain}", security_headers, TIMEOUT_CONNECT, TIMEOUT_READ, TIMEOUT_TOTAL)

        if result is None:
            result = await _aiohttp_fetch(session, f"http://{domain}", security_headers, TIMEOUT_HTTP_FALLBACK_CONNECT, TIMEOUT_HTTP_FALLBACK_READ, TIMEOUT_HTTP_FALLBACK_TOTAL)

        if result:
            return [(domain, name, value) for name, value in result]
        return [(domain, None, None)]


async def process_domains(
    session: aiohttp.ClientSession,
    domains: list,
    resume_index: int,
    total_domains: int,
    security_headers: set,
    start_time: float,
) -> int:
    """
    Drive the fetch loop over *domains*, writing results to the DB in batches
    and saving checkpoints periodically.

    *resume_index* is the absolute offset of domains[0] within the full input
    list — used only for accurate progress display and checkpoint values.

    Returns the number of domains actually processed in this run.
    """

    # A semaphore is a counter that limits how many coroutines can be inside 'async with semaphore:' at the same time.
    semaphore = asyncio.Semaphore(CONCURRENCY)
    pending_records = []
    processed_count = 0
    domains_since_checkpoint = 0

    for batch_start in range(0, len(domains), BATCH_SIZE):
        if _shutdown_requested:
            print("[!] Shutdown requested, flushing pending records...")
            break

        batch_end = batch_start + BATCH_SIZE
        batch = domains[batch_start:batch_end]

        tasks = [fetch_headers(session, semaphore, domain, security_headers) for domain in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            if not isinstance(result, Exception):
                pending_records.extend(result)

        processed_count += len(batch)
        domains_since_checkpoint += len(batch)

        if len(pending_records) >= BATCH_SIZE:
            flush_to_db(pending_records)
            pending_records = []

        # Usecase: if the job runs for a while and gets cancelled by GitHub Actions, the next run reads the checkpoint to skip already-processed domains.
        if domains_since_checkpoint >= CHECKPOINT_INTERVAL:
            save_checkpoint(resume_index + processed_count)
            domains_since_checkpoint = 0

        # Brief pause every N domains so that servers or CDNs that are
        # temporarily rate-limiting this runner's IP have a chance to reset.
        if processed_count % RATE_LIMIT_PAUSE_DOMAIN_LIMIT < BATCH_SIZE and processed_count > 0:
            await asyncio.sleep(RATE_LIMIT_PAUSE_SECS)

        # Print progress at every PROGRESS_INTERVAL boundary.
        if processed_count % PROGRESS_INTERVAL < BATCH_SIZE:
            elapsed = time.time() - start_time
            rate = processed_count / elapsed if elapsed > 0 else 0
            remaining = (len(domains) - processed_count) / rate if rate > 0 else 0
            total_done = resume_index + processed_count
            print(
                f"[+] Progress: {total_done}/{total_domains} domains "
                f"({total_done * 100 / total_domains:.1f}%) | "
                f"{rate:.1f} domains/sec | "
                f"ETA: {remaining / 60:.1f} min"
            )

    if pending_records:
        flush_to_db(pending_records)

    return processed_count


async def main():
    start_time = time.time()

    connector = aiohttp.TCPConnector(
        limit=CONCURRENCY,
        limit_per_host=3,
        # Explicit nameservers over the GitHub Actions runner's internal DNS
        # which gets rate-limited under high concurrency.
        # rotate=True enables c-ares round-robin across all servers (default is
        # always-first-server with failover only on failure).
        resolver=aiohttp.AsyncResolver(nameservers=NAMESERVERS, rotate=True),
        ttl_dns_cache=300,
        enable_cleanup_closed=True,
        # Each domain is visited once, so keep-alive connections are never
        # reused. force_close prevents timed-out connections from leaving
        # "sticky" slots in the pool (aiohttp issue #9670).
        force_close=True,
    )

    async with aiohttp.ClientSession(connector=connector,
        headers=REQ_HEADERS,
        max_field_size=65536,   # default is 8190; Twitter's CSP alone exceeds that :)
    ) as session:
        print("[+] Loading OSHP security headers list...")
        security_headers = await load_security_headers(session)
        print(f"    Headers: {security_headers}")

        await get_input_csv(session)

        print(f"[+] Loading domains from {CSV_INPUT_FILE}...")
        all_domains = load_domains(CSV_INPUT_FILE, NUMBER_OF_DOMAINS_TO_TAKE)
        total_domains = len(all_domains)
        print(f"[+] Loaded {total_domains} domains.")

        resume_index = load_checkpoint() #If there's any existing checkpoint. Otherwise 0
        if 0 < resume_index < total_domains:
            print(f"[+] Resuming from checkpoint at domain index {resume_index}...")
            domains = all_domains[resume_index:]
            init_db(resume=True)
        else:
            domains = all_domains
            resume_index = 0
            init_db(resume=False)
            clear_checkpoint()

        print(f"[+] Starting work: {len(domains)} domains to process, concurrency={CONCURRENCY}")

        processed_count = await process_domains(
            session, domains, resume_index, total_domains, security_headers, start_time
        )

        final_index = resume_index + processed_count
        save_checkpoint(final_index)

    record_count = get_record_count()
    elapsed_min = round((time.time() - start_time) / 60, 1)
    print("\n[+] Data gathered:")
    print(f"    Records: {record_count}")
    print(f"    Domains processed: {final_index}/{total_domains}")
    print(f"    Time: {elapsed_min} minutes")

    if final_index >= total_domains:
        clear_checkpoint()
        print("[+] All domains processed. Checkpoint cleared.")


if __name__ == "__main__":
    # Handling the case when a GitHub Actions job is cancelled (manually or due to timeout).
    signal.signal(signal.SIGTERM, _request_shutdown)
    signal.signal(signal.SIGINT, _request_shutdown)
    
    asyncio.run(main())
