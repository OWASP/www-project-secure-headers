"""
Utility script to generate the reference both JSON files providing the collection of HTTP response security headers to add and remove.

Use as a source, the information defined in the file "tab_bestpractices.md" in the following tables:
- Section "Configuration proposal" for the headers to add:
    Identification via the markers "<!--HEADERS_ADD_TABLE_START-->" and "<!--HEADERS_ADD_TABLE_END-->"
- Section "Prevent information disclosure via HTTP headers" for the headers to remove:
    Identification via the markers "<!--HEADERS_REMOVE_TABLE_START-->" and "<!--HEADERS_REMOVE_TABLE_END-->"

Try to not use any external dependency to stay the more portable possible.

A last update date attribute was added in both JSON files to allow user to quickly identify when files were changed
and trigger update on their side. In addition, it helps the CI workflow to be easier by causing the JSON files to be different
at each run of the script (made commit easier to manage).
"""

import json
import re
import operator
from datetime import datetime

# Constants
SOURCE_MD_FILE = "../tab_bestpractices.md"
HEADERS_TO_ADD_JSON_FILE = "headers_add.json"
HEADERS_TO_REMOVE_JSON_FILE = "headers_remove.json"
HEADERS_TO_ADD_TABLE_EXTRACTION_MARKERS = ("<!-- HEADERS_ADD_TABLE_START -->", "<!-- HEADERS_ADD_TABLE_END -->")
HEADERS_TO_REMOVE_TABLE_EXTRACTION_MARKERS = ("<!-- HEADERS_REMOVE_TABLE_START -->", "<!-- HEADERS_REMOVE_TABLE_END -->")
EXECUTION_DATETIME_UTC = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
LAST_UPDATE_ATTRIBUTE_NAME = "last_update_utc"
JSON_IDENT = 2


def extract_table_md(headers_category="add"):
    markers = HEADERS_TO_ADD_TABLE_EXTRACTION_MARKERS
    if headers_category != "add":
        markers = HEADERS_TO_REMOVE_TABLE_EXTRACTION_MARKERS
    with open(SOURCE_MD_FILE, mode="r", encoding="utf-8") as md_file:
        md_content = md_file.read()
    start = md_content.find(markers[0])
    end = md_content.find(markers[1])
    if start == -1 or end == -1:
        raise Exception(f"No table was identified with markers {markers} for headers category '{headers_category}'!")
    md_table = md_content[start + len(markers[0]):end]
    md_table = md_table.strip("\t\n\r ")
    return md_table


def generate_headers_to_add_json(md_table):
    lines = md_table.split("\n")
    headers = []
    for i in range(2, len(lines)):
        header_info = lines[i]
        header_parts = header_info.split("|")
        header_name = header_parts[1].strip(" `*\t\n\r")
        header_value = header_parts[2].strip(" `*\t\n\r")
        headers.append({"name": header_name, "value": header_value})
    headers.sort(key=operator.itemgetter("name"))
    data = {LAST_UPDATE_ATTRIBUTE_NAME: EXECUTION_DATETIME_UTC, "headers": headers}
    return json.dumps(data, indent=JSON_IDENT)


def generate_headers_to_remove_json(md_table):
    lines = md_table.split("\n")
    headers = []
    for i in range(2, len(lines)):
        header_info = lines[i]
        header_parts = header_info.split("|")
        header_name = header_parts[1].strip(" `*\t\n\r")
        header_name = re.findall(r'\[(.*)\]', header_name)[0]
        headers.append(header_name)
    headers.sort()
    data = {LAST_UPDATE_ATTRIBUTE_NAME: EXECUTION_DATETIME_UTC, "headers": headers}
    return json.dumps(data, indent=JSON_IDENT)


if __name__ == "__main__":
    for headers_category in ["add", "remove"]:
        print(f"[+] Generate content for headers category: {headers_category}")
        md_table = extract_table_md(headers_category)
        if headers_category == "add":
            json_content = generate_headers_to_add_json(md_table)
            json_ref_file = HEADERS_TO_ADD_JSON_FILE
        else:
            json_content = generate_headers_to_remove_json(md_table)
            json_ref_file = HEADERS_TO_REMOVE_JSON_FILE
        with open(json_ref_file, mode="w", encoding="utf-8") as json_file:
            json_file.write(json_content)
