"""
Utility script to generate a markdown file with the update health state of all GitHub repositories mentioned in the tab named "Technical".

The goal is to allow detection of old and dead projects.

Sources:
    https://thispointer.com/python-get-difference-between-two-dates-in-months/
    https://docs.github.com/en/rest/repos/repos#get-a-repository

Try to not use any external dependency to stay the more portable possible.
"""
import json
import re
import sys
import urllib.request
from datetime import datetime

# Constants
EXECUTION_DATETIME_UTC = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
DEFAULT_ENCODING = "utf-8"
SOURCE_MD_FILE = "../tab_technical.md"
DASHBOARD_MD_FILE = "../monitoring_technical_references_dashboard.md"
DASHBOARD_MD_FILE_TEMPLATE = f"""
# Technical References Dashboard

> 📅 Last verification (UTC): {EXECUTION_DATETIME_UTC}

## GitHub repositories health status

Provides a quick visual status on the health status (whether they are updated or not) of the referenced GitHub projects in the tab named **Technical**.

Project reaching the :red_circle: status **are removed**.

:speech_balloon: **Status icon legends:**

* :green_circle: Updated within the last **12 months** from the date of verification.
* :orange_circle: Updated within the last **24 months** from the date of verification.
* :red_circle: Not updated for **more than 24 months** from the date of verification.

%s

"""


def determine_health_state(repo_updated_datetime):
    # Format: 2022-09-14T13:40:24Z
    # Keep only the date part
    start_date = datetime.strptime(repo_updated_datetime.split("T")[0], "%Y-%m-%d")
    end_date = datetime.now()
    diff_months = ((end_date.year - start_date.year) * 12) + (end_date.month - start_date.month)
    if diff_months <= 12:
        health_state_icon = ":green_circle:"
    elif diff_months <= 24:
        health_state_icon = ":orange_circle:"
    else:
        health_state_icon = ":red_circle:"
    return (diff_months, health_state_icon)


def extract_updated_datetime(github_repo_url, github_access_token):
    # Extract the repo owner and project name from the repo url
    parts = github_repo_url.strip(' \r\n\t').split("/")
    repo_owner = parts[3]
    project_name = parts[4]
    # Get the info of the repo using the GitHub API
    api_url = f"https://api.github.com/repos/{repo_owner}/{project_name}"
    request = urllib.request.Request(url=api_url, method="GET")
    if github_access_token is not None:
        request.add_header("Authorization", f"Bearer {github_access_token}")
    with urllib.request.urlopen(request) as f:
        repo_info = json.loads(f.read().decode(DEFAULT_ENCODING))
    # Return the updated date attribute
    # Format: 2022-09-14T13:40:24Z
    return repo_info["pushed_at"]


def extract_github_repositories_url():
    github_repositories_url_collection = []
    expr = r'https://github\.com/[a-zA-Z0-9.\-_/]+'
    with open(SOURCE_MD_FILE, mode="r", encoding=DEFAULT_ENCODING) as f:
        content = f.read()
    repos = re.findall(expr, content)
    for repo in repos:
        github_repositories_url_collection.append(repo.strip(' <>'))
    github_repositories_url_collection.sort()
    return github_repositories_url_collection


def generate_md_table(github_repositories_url_collection, github_access_token):
    table_md = "| Last update | Status | Repository |\n| --- | --- | --- |\n"
    lines = []
    for repo in github_repositories_url_collection:
        updated_datetime = extract_updated_datetime(repo, github_access_token)
        health_state = determine_health_state(updated_datetime)
        repo_name = repo.replace("https://github.com/", "")
        lines.append(f"| `{updated_datetime}` ({health_state[0]} months ago) | {health_state[1]} | [{repo_name}]({repo}) |")
    lines.sort()
    table_md += "\n".join(lines)
    return table_md


if __name__ == "__main__":
    github_access_token = None
    if len(sys.argv) == 2:
        print("[i] GitHub access token provided.")
        github_access_token = sys.argv[1]
    else:
        print("[i] No GitHub access token provided.")
    print("[+] Extract GitHub repositories url...")
    repos = extract_github_repositories_url()
    print(f"{len(repos)} repos.")
    print("[+] Generate MD table...")
    table_md = generate_md_table(repos, github_access_token)
    print("[+] Update dashboard MD file...")
    dashboard_content = DASHBOARD_MD_FILE_TEMPLATE % table_md
    with open(DASHBOARD_MD_FILE, mode="w", encoding=DEFAULT_ENCODING) as f:
        f.write(dashboard_content)
    print(f"[V] File '{DASHBOARD_MD_FILE}' updated.")
