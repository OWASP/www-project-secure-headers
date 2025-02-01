#!/bin/bash
#########################################################################
# Generate the PNG image files from corresponding MMD (mermaid) files.
#
# Dependencies:
#   https://github.com/mermaid-js/mermaid-cli
#########################################################################
# Constants
IMAGE_FOLDER_LOCATION="../assets/tab_stats_generated_images"
# Generate images
cd $IMAGE_FOLDER_LOCATION
for mmd_file in *.mmd
do
    png_file="${mmd_file%%.*}.png"
    npx -p @mermaid-js/mermaid-cli mmdc --quiet --input $mmd_file --output $png_file --outputFormat png --theme default --backgroundColor transparent
done
# Only let PNG files
rm *.mmd
cd -
