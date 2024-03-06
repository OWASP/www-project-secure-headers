"""
Utility script to verify that every site mentioned in the tab named "Case Studies" have a mention to OSHP.

The goal is to allow detection of site not mentioning the OSHP anymore and then update the "Case Studies" content.

Try to not use any external dependency to stay the more portable possible.
"""
import re
import urllib.request

OSHP_MARKER_STRINGS = ["owasp secure headers project", "https://owasp.org/www-project-secure-headers", "https://www.owasp.org/index.php/security_headers", "secure headers project"]
DEFAULT_ENCODING = "utf-8"
IGNORED_HTTP_RESPONSE_CODES = [401]
SOURCE_MD_FILE = "../tab_casestudies.md"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"


def verify_mention(site_url):
    oshp_is_mentioned = "NO"
    request = urllib.request.Request(url=site_url, method="GET")
    request.add_header("User-Agent", USER_AGENT)
    request.add_header("Accept", "*/*")
    request.add_header("Accept-Encoding", "deflate")
    try:
        # Assume by default that site refer to static non SPA page
        with urllib.request.urlopen(request) as f:
            content = f.read().decode(DEFAULT_ENCODING)
        content_lower = content.lower()
        for marker in OSHP_MARKER_STRINGS:
            if marker in content_lower:
                oshp_is_mentioned = "YES"
                break
        # If mention is not detected then try to check if it's an SPA
        if oshp_is_mentioned == "NO":
            expr = r'app\.[a-f0-9]+\.js'
            bundles = re.findall(expr, content)
            if len(bundles) > 0 or "React" in content:
                oshp_is_mentioned = "NO => SPA"
    except urllib.error.HTTPError as e:
        if e.code in IGNORED_HTTP_RESPONSE_CODES:
            oshp_is_mentioned = f"HTTP {e.code}"
    return oshp_is_mentioned


def extract_site_urls():
    expr = r'\*\s+\[[a-zA-Z0-9\s_\-\.]+\]\((.*?)\)'
    with open(SOURCE_MD_FILE, mode="r", encoding=DEFAULT_ENCODING) as f:
        content = f.read()
    return re.findall(expr, content)


if __name__ == "__main__":
    verify_mention("https://eoahgl4pezvrojk.m.pipedream.net/")
    print("[+] Extract site urls...")
    site_urls = extract_site_urls()
    print(f"{len(site_urls)} urls founds.")
    print("[+] Verify mention to OSHP on each site...")
    lines = []
    for site_url in site_urls:
        if site_url.strip().startswith("http"):
            oshp_is_mentioned = verify_mention(site_url)
            lines.append(f"[{str(oshp_is_mentioned):<9}] {site_url}")
    lines.sort()
    print("\n".join(lines))
