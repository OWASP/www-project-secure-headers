#!/bin/bash
#########################################################################
# This script manage the generation/update of the tab represented by the 
# file "tab_statistics.md".
#########################################################################
DATA_DB_FILE_LOCATION="https://github.com/oshp/oshp-stats/raw/refs/heads/main/data/data.db"
DATA_DB_FILE="/tmp/data.db"
echo "[+] Download the database of headers analysis..."
wget -q -O $DATA_DB_FILE $DATA_DB_FILE_LOCATION
file $DATA_DB_FILE
echo "[+] Set correct access rights for the scripts as well as UNIX CRLF settings..."
dos2unix tab_stats_generate_*
chmod +x tab_stats_generate_*
echo "[+] Generate the MD file of the TAB and all the MMD files for every pie chart image..."
python tab_stats_generate_md_file.py
echo "[+] Generate the PNG image corresponding to each MMD file..."
bash tab_stats_generate_png_files.sh
echo "[+] Cleanup"
rm $DATA_DB_FILE