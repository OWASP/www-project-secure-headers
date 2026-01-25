#!/bin/bash
#########################################################################
# This script manage the generation/update of the tab represented by the 
# file "tab_statistics.md".
#########################################################################
OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION="../subprojects/statistics/scripts/oshp_headers_extra_to_include.txt"
OSHP_SECURITY_HEADERS_EXTRA_FILE="/tmp/oshp_headers_extra_to_include.txt"
DATA_DB_FILE_LOCATION="../subprojects/statistics/data/data.db"
DATA_DB_FILE="/tmp/data.db"
IMAGE_FOLDER_LOCATION="../assets/tab_stats_generated_images"
echo "[+] Download the database of headers analysis anc validate the database file..."
cp $OSHP_SECURITY_HEADERS_EXTRA_FILE_LOCATION $OSHP_SECURITY_HEADERS_EXTRA_FILE 
cp $DATA_DB_FILE_LOCATION $DATA_DB_FILE 
file $DATA_DB_FILE
sqlite3 $DATA_DB_FILE ".tables"
file $OSHP_SECURITY_HEADERS_EXTRA_FILE
wc -l $OSHP_SECURITY_HEADERS_EXTRA_FILE
echo "[+] Set correct access rights for the scripts as well as UNIX CRLF settings..."
dos2unix *.sh
chmod +x tab_stats_generate_*
echo "[+] Generate the MD file of the TAB and all the MMD files for every pie chart image..."
python tab_stats_generate_md_file.py
echo "[+] Generate the PNG image corresponding to each MMD file..."
bash tab_stats_generate_png_files.sh
echo "[+] Check correct generation of the images..."
img_count=$(find $IMAGE_FOLDER_LOCATION -name "*.png" | wc -l)
if [ $img_count -eq 0 ]
then
    echo "[!] No image file was generated!"
    exit 1
else
    echo "[V] $img_count image files were generated!"
    sha256sum *.png
    exit 0
fi
