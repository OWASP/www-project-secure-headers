"""
Utility script to verify that every site mentioned in the tab named "Case Studies" have a mention to OSHP.

The goal is to allow detection of site not mentioning the OSHP anymore and then update the "Case Studies" content.

Dependencies:
    pip install requests
"""
import re
import requests
import time
import os
import sys

OSHP_MARKER_STRINGS = ["owasp secure headers project", "https://owasp.org/www-project-secure-headers", "https://www.owasp.org/index.php/security_headers", "https://owasp.org/index.php/owasp_secure_headers_project"]
DEFAULT_ENCODING = "utf-8"
WAIT_DELAY_SECONDS = 4
MAX_RETRY = 4
TIMEOUT_SECONDS = 20
IGNORED_HTTP_RESPONSE_CODES = [401]
SOURCE_MD_FILE = "../tab_casestudies.md"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"


def verify_mention(site_url):
    oshp_is_mentioned = "NO"
    # Assume by default that site refer to static non SPA page
    response = requests.get(url=site_url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT_SECONDS, allow_redirects=True)
    if response.status_code in IGNORED_HTTP_RESPONSE_CODES:
        oshp_is_mentioned = "YES"
    else:
        content = response.text
        content_lower = content.lower()
        for marker in OSHP_MARKER_STRINGS:
            if marker.lower() in content_lower:
                oshp_is_mentioned = "YES"
                break
    # If mention is not detected then try to check if it's an SPA
    if oshp_is_mentioned == "NO":
        expr = r'(app|index|main)(\.|-)[a-zA-Z0-9_]+\.js'
        bundles = re.findall(expr, content)
        if len(bundles) > 0 or "React" in content:
            oshp_is_mentioned = "SPA"
    # If mention is not detected then try to check if the site is protected by CLOUDFLARE
    if oshp_is_mentioned == "NO" and ("CF-RAY" in response.headers or "cf-mitigated" in response.headers):
        oshp_is_mentioned = "CLOUDFLARE"
    return oshp_is_mentioned


def extract_site_urls():
    expr = r'\*\s+\[[a-zA-Z0-9\s_\-\.]+\]\((.*?)\)'
    with open(SOURCE_MD_FILE, mode="r", encoding=DEFAULT_ENCODING) as f:
        content = f.read()
    return re.findall(expr, content)


def print_github_error(site_url, oshp_is_mentioned):
    print(f"::error file={os.path.basename(__file__)},title=MissingOSHPReference::For site '{site_url}' reference is '{oshp_is_mentioned}'.")


if __name__ == "__main__":
    print("[+] Extract site urls...")
    site_urls = extract_site_urls()
    print(f"{len(site_urls)} urls founds.")
    print("[+] Verify mention to OSHP on each site...")
    valid_mentions = ["YES", "SPA", "CLOUDFLARE"]
    error_count = 0
    for site_url in site_urls:
        if site_url.strip().startswith("http"):
            oshp_is_mentioned = "NO"
            for _ in range(0, MAX_RETRY):
                try:
                    oshp_is_mentioned = verify_mention(site_url)
                    if oshp_is_mentioned in valid_mentions:
                        break
                    else:
                        time.sleep(WAIT_DELAY_SECONDS)
                except requests.exceptions.Timeout:
                    oshp_is_mentioned = "IO_ERROR"
                    time.sleep(WAIT_DELAY_SECONDS)
                    pass
            if oshp_is_mentioned not in valid_mentions:
                print_github_error(site_url, oshp_is_mentioned)
                error_count += 1
    if error_count == 0:
        print("All references are OK.")
    sys.exit(error_count)
