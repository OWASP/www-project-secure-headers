#!/bin/bash
#########################################################################
# Generate the PNG image files from corresponding MMD (mermaid) files.
#
# Dependencies:
#   https://github.com/mermaid-js/mermaid-cli
#
# Reference:
#   https://github.com/mermaid-js/mermaid-cli/blob/master/.github/workflows/test.yml#L24
#########################################################################
# Constants
IMAGE_FOLDER_LOCATION="../assets/tab_stats_generated_images"
# Generate images
# We use aa-exec since Ubuntu 24.04's AppArmor profile blocks the use of puppeteer otherwise
# See https://github.com/puppeteer/puppeteer/issues/12818
cd $IMAGE_FOLDER_LOCATION
for mmd_file in *.mmd
do
    png_file="${mmd_file%%.*}.png"
    aa-exec --profile=chrome npx -p @mermaid-js/mermaid-cli mmdc --quiet --input $mmd_file --output $png_file --outputFormat png --theme default --backgroundColor transparent
done
# Only let PNG files
rm *.mmd
cd -
