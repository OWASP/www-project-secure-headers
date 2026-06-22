#!/bin/bash
#########################################################################
# Audit all GHA (GitHub Actions) workflows with Plumber.
#
# Dependencies:
#   apt install curl jq
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
$PLUMBER_BINARY_LOCATION config validate
echo "[+] Audit the GHA workflows..."
rm -f $PLUMBER_REPORT_LOCATION 2>/dev/null
$PLUMBER_BINARY_LOCATION analyze --sarif $PLUMBER_REPORT_LOCATION
# Currently the disabling of the check on protected branch is not taken in account so the
# following execution error is raised:
# "data collection incomplete: branch protection could not be fetched; branch controls were not evaluated"
# So we update the attribute "invocations[0].executionSuccessful" to true if the report was correctly generated
if [ -s "$PLUMBER_REPORT_LOCATION" ]
then
  jq '(.runs[].invocations[].executionSuccessful) = true' $PLUMBER_REPORT_LOCATION > "$PLUMBER_REPORT_LOCATION.tmp"
  mv "$PLUMBER_REPORT_LOCATION.tmp" $PLUMBER_REPORT_LOCATION
fi
cat $PLUMBER_REPORT_LOCATION | jq
# Force exit 0 because plumber return an exit code 3 because an access token is not provided
exit 0
