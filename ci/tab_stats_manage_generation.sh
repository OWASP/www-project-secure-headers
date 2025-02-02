#!/bin/bash
#########################################################################
# This script manage the generation/update of the tab represented by the 
# file "tab_statistics.md".
#########################################################################
OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION="https://raw.githubusercontent.com/oshp/oshp-stats/refs/heads/main/scripts/oshp_headers_extra_to_include.txt"
OSHP_SECURITY_HEADERS_EXTRA_FILE="/tmp/oshp_headers_extra_to_include.txt"
DATA_DB_FILE_LOCATION="https://github.com/oshp/oshp-stats/raw/refs/heads/main/data/data.db"
DATA_DB_FILE="/tmp/data.db"
IMAGE_FOLDER_LOCATION="../assets/tab_stats_generated_images"
echo "[+] Download the database of headers analysis anc validate the database file..."
wget -q -O $DATA_DB_FILE $DATA_DB_FILE_LOCATION
wget -q -O $OSHP_SECURITY_HEADERS_EXTRA_FILE $OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATIO
file $DATA_DB_FILE
sqlite3 $DATA_DB_FILE ".tables"
echo "[+] Set correct access rights for the scripts as well as UNIX CRLF settings..."
dos2unix *.sh
chmod +x tab_stats_generate_*
echo "[+] Generate the MD file of the TAB and all the MMD files for every pie chart image..."
python tab_stats_generate_md_file.py
echo "[+] Generate the PNG image corresponding to each MMD file..."
bash tab_stats_generate_png_files.sh
echo "[+] Cleanup"
rm $DATA_DB_FILE
rm $OSHP_SECURITY_HEADERS_EXTRA_FILE
echo "[+] Check correct generation of the images..."
img_count=$(find $IMAGE_FOLDER_LOCATION -name "*.png" | wc -l)
if [ $img_count -eq 0 ]
then
    echo "[!] No image file was generated!"
    exit 1
else
    echo "[V] $img_count image files were generated!"
    exit 0
fi
