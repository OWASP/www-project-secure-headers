#!/bin/bash
#########################################################################
# Audit all GHA (GitHub Actions) workflows with Plumber.
#
# Dependencies:
#   apt install curl 
#
# We use a fixed version to apply control on the version used and
# decrease exposure if the repo of plumber is compromised.
#
# The fixed hash is taken for the VirusTotal scan of the "plumber-linux-amd64"
# artefacts of the release.
#
# Reference:
#   https://github.com/getplumber/plumber
#########################################################################
PLUMBER_RELEASE_USED="0.3.69"
PLUMBER_RELEASE_SHA256="9090ce56e911e3a35d3b01e254bc4121f97c1ee94c90f375991140a05358e09c"
PLUMBER_DOWNLOAD_URL="https://github.com/getplumber/plumber/releases/download/v$PLUMBER_RELEASE_USED/plumber-linux-amd64"
PLUMBER_BINARY_LOCATION="/tmp/plumber"
PLUMBER_REPORT_LOCATION="/tmp/plumber-report.sarif"
export PATH=$PLUMBER_BINARY_LOCATION:$PATH
export PLUMBER_NO_UPDATE_CHECK=1
echo "[+] Download the release v$PLUMBER_RELEASE_USED of plumber..." 
curl -L -s -o $PLUMBER_BINARY_LOCATION "$PLUMBER_DOWNLOAD_URL"
file $PLUMBER_BINARY_LOCATION
chmod +x $PLUMBER_BINARY_LOCATION
echo "[+] Check the hash..."
hash=$(sha256sum $PLUMBER_BINARY_LOCATION | cut -d' ' -f1)
if [ "$PLUMBER_RELEASE_SHA256" != "$hash"  ]
then
    echo "[!] Plumber hashes do not match!"
    echo "Expected: $PLUMBER_RELEASE_SHA256"
    echo "Computed: $hash"
    echo "See https://github.com/getplumber/plumber/releases for releases informations."
    exit 1
fi
echo "[+] Validate the plumber configuration file..."
plumber config validate
echo "[+] Audit the GHA workflows..."
rm -f $PLUMBER_REPORT_LOCATION 2>/dev/null
plumber analyze --sarif $PLUMBER_REPORT_LOCATION
