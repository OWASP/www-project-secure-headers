#!/usr/bin/env python
import json
import re
import os
import os.path
import argparse
import pathlib
import sys
import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
"""
Script used to validate all HTTP/HTTPS links contained into a collection of
markdown (called MD) files.

The goal is to remplace, by a standalone portable script, the following github action
that is now deprecated:

https://github.com/gaurav-nelson/github-action-markdown-link-check

This script load the configuration from the file used to configure the tool "markdown-link-check"
that was used by the github actions:

https://github.com/tcort/markdown-link-check

Only the following property are supported:
- timeout
- retryCount
- aliveStatusCodes
- httpHeaders[0]["headers"]

Support for skipping validation for a link is supported via the following link MD format:

[Duck Duck Go](https://duckduckgo.com "SKIP_VALIDATION")

"SKIP_VALIDATION" marker instruct to skip the validation.

Dependencies:
    pip install requests
"""
VALIDATION_SKIP_MARKER = "SKIP_VALIDATION"
DEFAULT_ENCODING = "utf-8"
DEFAULT_TIMEOUT_IN_SECONDS = 5
DEFAULT_RETRY_COUNT = 2
DEFAULT_ALIVE_STATUS_CODE = [200, 429, 502, 503, 504]
DEFAULT_MAX_REDIRECT = 5
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
DEBUG_MODE = False


def load_config(markdown_link_check_config_file_path):
    # Load markdown-link-check configuration is present
    if os.path.isfile(markdown_link_check_config_file_path):
        with open(markdown_link_check_config_file_path, mode="r", encoding=DEFAULT_ENCODING) as f:
            cfg = json.load(f)
    else:
        cfg = {}
    # Tune settings
    cfg["defaultConfig"] = (not os.path.isfile(markdown_link_check_config_file_path))
    if "httpHeaders" not in cfg:
        cfg["httpHeaders"] = [{"headers": DEFAULT_HEADERS}]
    if len(cfg["httpHeaders"]) == 0:
        cfg["httpHeaders"] = [{"headers": DEFAULT_HEADERS}]
    if "headers" not in cfg["httpHeaders"][0]:
        cfg["httpHeaders"] = [{"headers": DEFAULT_HEADERS}]
    if "timeout" not in cfg:
        cfg["timeout"] = DEFAULT_TIMEOUT_IN_SECONDS
    else:
        cfg["timeout"] = int(cfg["timeout"].strip("ms"))
    if "retryCount" not in cfg:
        cfg["retryCount"] = DEFAULT_RETRY_COUNT
    if "aliveStatusCodes" not in cfg:
        cfg["aliveStatusCodes"] = DEFAULT_ALIVE_STATUS_CODE
    if len(cfg["aliveStatusCodes"]) == 0:
        cfg["aliveStatusCodes"] = DEFAULT_ALIVE_STATUS_CODE
    # Configure the automatic retry support
    req_session = Session()
    retries = Retry(
        total=cfg["retryCount"],
        redirect=DEFAULT_MAX_REDIRECT,
        backoff_factor=0.1,
        status_forcelist=[408, 500, 502, 503, 504],
        allowed_methods={"GET"},
        raise_on_redirect=True
    )
    req_session.mount("https://", HTTPAdapter(max_retries=retries))
    req_session.mount("http://", HTTPAdapter(max_retries=retries))
    cfg["req_session"] = req_session
    return cfg


def extract_links(markdown_file_path):
    links = []
    patterns = [r'<(http.*?)>', r'\[.*?\]\((http.*?)\)']
    with open(markdown_file_path, mode="r", encoding=DEFAULT_ENCODING) as f:
        content = f.read()
    buffer_links = []
    for pattern in patterns:
        buffer_links.extend(re.findall(pattern, content, re.IGNORECASE))
    for link in buffer_links:
        if VALIDATION_SKIP_MARKER not in link.upper() and link not in links:
            links.append(link.strip(" "))
    links.sort()
    return links


def validate_link(cfg, link):
    status = (False, "")
    try:
        if DEBUG_MODE:
            print(f"<{link}> Test pending...")
        response = cfg["req_session"].get(link, headers=cfg["httpHeaders"][0]["headers"], timeout=cfg["timeout"], allow_redirects=True, verify=False)
        is_valid = (response.status_code in cfg["aliveStatusCodes"])
        status = (is_valid, response.status_code)
    except Exception as e:
        status = (False, str(e))
    finally:
        if DEBUG_MODE:
            print(f"<{link}> Test done, link is valid? {status[0]}.")
    return status


def print_error(markdown_file_path, link, validation_status):
    if os.environ.get("GITHUB_WORKSPACE") is not None:
        print(f"::error file={markdown_file_path},title=BrokenLinkIdentified::Link is {link} => {validation_status[1]}")
    else:
        print(f"Broken link '{link}' identified in file '{markdown_file_path}' => {validation_status[1]}")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", action="store", dest="base_folder", help="Location of the root base folder from which markdown files will be searched.", required=False, default=os.getcwd())
    parser.add_argument("-c", action="store", dest="markdown_link_check_config_file_path", help="Location of the file containing the configuration for markdown-link-check.", required=False, default="markdown-link-check-config.json")
    parser.add_argument("-d", action=argparse.BooleanOptionalAction, dest="debug_mode", help="Print more information for help debugging.")
    args = parser.parse_args()
    markdown_link_check_config_file_path = args.markdown_link_check_config_file_path
    base_folder = args.base_folder
    DEBUG_MODE = args.debug_mode
    print("[+] Load config")
    conf = load_config(markdown_link_check_config_file_path)
    print(f"Default config loaded? {conf['defaultConfig']}")
    print("[+] Search and process any MD file")
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    dead_links_global_count = 0
    for md_file in pathlib.Path(base_folder).rglob("*.md", case_sensitive=False):
        markdown_file_path = str(md_file)
        markdown_file_name = md_file.name
        print(f"({markdown_file_name}) Extracting links...")
        links = extract_links(markdown_file_path)
        if len(links) == 0:
            print(f"({markdown_file_name}) No link found.")
            continue
        print(f"({markdown_file_name}) Processing {len(links)} link(s)...")
        dead_links_local_file_count = 0
        for link in links:
            validation_status = validate_link(conf, link)
            if not validation_status[0]:
                print_error(markdown_file_path, link, validation_status)
                dead_links_local_file_count += 1
        print(f"({markdown_file_name}) {dead_links_local_file_count} dead link(s) found.")
        dead_links_global_count += dead_links_local_file_count
    print(f"[+] Exit with code {dead_links_global_count}")
    sys.exit(dead_links_global_count)
