---
title: top
displaytext: Top Websites Examples
layout: null
tab: true
order: 4
tags: headers
---

# Top Websites Examples

HTTP response headers from the top websites in the world.

Command used to extract the headers:

```sh
curl -L -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" -s -D - https://www.example.com -o /dev/null
```

## Google

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.google.com -o /dev/null

HTTP/2 200
date: Sat, 15 Jan 2022 16:20:55 GMT
expires: -1
cache-control: private, max-age=0
content-type: text/html; charset=UTF-8
strict-transport-security: max-age=31536000
bfcache-opt-in: unload
p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."
server: gws
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
accept-ranges: none
vary: Accept-Encoding
```

## Facebook

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.facebook.com -o /dev/null

HTTP/2 200
vary: Accept-Encoding
x-fb-rlafr: 0
document-policy: force-load-at-top
pragma: no-cache
cache-control: private, no-cache, no-store, must-revalidate
expires: Sat, 01 Jan 2000 00:00:00 GMT
x-content-type-options: nosniff
x-xss-protection: 0
content-security-policy-report-only: default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com 'unsafe-eval' *.fbcdn.net;script-src *.facebook.com *.fbcdn.net 'unsafe-inline' 'unsafe-eval' blob: data: 'self';style-src *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net wss://*.facebook.com:* attachment.fbsbx.com blob: *.cdninstagram.com 'self' wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d-test.facebook.com/ wss://kaios-d.facebook.com/ *.fbsbx.com;font-src data: *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net blob: android-webview-video-poster:;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com data:;frame-src *.facebook.com *.fbsbx.com fbsbx.com data: *.fbcdn.net;worker-src blob: *.facebook.com data:;report-uri https://www.facebook.com/csp/reporting/?m=c&minimize=0;
content-security-policy: default-src data: blob: 'self' https://*.fbsbx.com 'unsafe-inline' *.facebook.com 'unsafe-eval' *.fbcdn.net;script-src *.facebook.com *.fbcdn.net 'unsafe-inline' 'unsafe-eval' blob: data: 'self';style-src *.fbcdn.net data: *.facebook.com 'unsafe-inline';connect-src *.facebook.com facebook.com *.fbcdn.net wss://*.facebook.com:* attachment.fbsbx.com blob: *.cdninstagram.com 'self' wss://gateway.facebook.com wss://edge-chat.facebook.com wss://snaptu-d.facebook.com wss://kaios-d-test.facebook.com/ wss://kaios-d.facebook.com/ *.fbsbx.com;font-src data: *.facebook.com *.fbcdn.net *.fbsbx.com;img-src *.fbcdn.net *.facebook.com data: https://*.fbsbx.com facebook.com *.cdninstagram.com fbsbx.com fbcdn.net blob: android-webview-video-poster:;media-src *.cdninstagram.com blob: *.fbcdn.net *.fbsbx.com www.facebook.com *.facebook.com data:;frame-src *.facebook.com *.fbsbx.com fbsbx.com data: *.fbcdn.net;worker-src blob: *.facebook.com data:;block-all-mixed-content;upgrade-insecure-requests;report-uri https://www.facebook.com/csp/reporting/?m=c&minimize=0;
x-frame-options: DENY
strict-transport-security: max-age=15552000; preload
content-type: text/html; charset="utf-8"
x-fb-debug: M4/CJ5A2DSyEA2LjHGF5BfVjsjpbSZ/6GcXpeTlWMQ5//gvXD216nkTu5ISGgMpJ0Y1pKYBEgwXHJCKjyUx+hw==
date: Sat, 15 Jan 2022 16:25:09 GMT
priority: u=3,i
alt-svc: h3=":443"; ma=3600, h3-29=":443"; ma=3600
```

## Twitter

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.twitter.com -o /dev/null

HTTP/2 200
date: Sat, 15 Jan 2022 16:25:30 GMT
expiry: Tue, 31 Mar 1981 05:00:00 GMT
pragma: no-cache
server: tsa_f
content-type: text/html; charset=utf-8
x-powered-by: Express
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
last-modified: Sat, 15 Jan 2022 16:25:30 GMT
x-frame-options: DENY
x-xss-protection: 0
x-content-type-options: nosniff
content-security-policy: connect-src 'self' blob: https://*.giphy.com https://*.pscp.tv https://*.video.pscp.tv https://*.twimg.com https://api.twitter.com https://api-stream.twitter.com https://ads-api.twitter.com https://aa.twitter.com https://caps.twitter.com https://media.riffsy.com https://pay.twitter.com https://sentry.io https://ton.twitter.com https://twitter.com https://upload.twitter.com https://www.google-analytics.com https://accounts.google.com/gsi/status https://accounts.google.com/gsi/log https://app.link https://api2.branch.io https://bnc.lt wss://*.pscp.tv https://vmap.snappytv.com https://vmapstage.snappytv.com https://vmaprel.snappytv.com https://vmap.grabyo.com https://dhdsnappytv-vh.akamaihd.net https://pdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://dwo3ckksxlb0v.cloudfront.net ; default-src 'self'; form-action 'self' https://twitter.com https://*.twitter.com; font-src 'self' https://*.twimg.com; frame-src 'self' https://twitter.com https://mobile.twitter.com https://pay.twitter.com https://cards-frame.twitter.com https://accounts.google.com/  https://recaptcha.net/recaptcha/ https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/; img-src 'self' blob: data: https://*.cdn.twitter.com https://ton.twitter.com https://*.twimg.com https://analytics.twitter.com https://cm.g.doubleclick.net https://www.google-analytics.com https://www.periscope.tv https://www.pscp.tv https://media.riffsy.com https://*.giphy.com https://*.pscp.tv https://*.periscope.tv https://prod-periscope-profile.s3-us-west-2.amazonaws.com https://platform-lookaside.fbsbx.com https://scontent.xx.fbcdn.net https://scontent-sea1-1.xx.fbcdn.net https://*.googleusercontent.com https://imgix.revue.co; manifest-src 'self'; media-src 'self' blob: https://twitter.com https://*.twimg.com https://*.vine.co https://*.pscp.tv https://*.video.pscp.tv https://*.giphy.com https://media.riffsy.com https://dhdsnappytv-vh.akamaihd.net https://pdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://mdhdsnappytv-vh.akamaihd.net https://mpdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://dwo3ckksxlb0v.cloudfront.net; object-src 'none'; script-src 'self' 'unsafe-inline' https://*.twimg.com https://recaptcha.net/recaptcha/ https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://www.google-analytics.com https://twitter.com https://app.link https://accounts.google.com/gsi/client https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js  'nonce-NDFlMzM0YjgtOWZkZS00MWFjLWE3ODktYjYxYmVjYjExMjlk'; style-src 'self' 'unsafe-inline' https://accounts.google.com/gsi/style https://*.twimg.com; worker-src 'self' blob:; report-uri https://twitter.com/i/csp_report?a=O5RXE%3D%3D%3D&ro=false
strict-transport-security: max-age=631138519
cross-origin-opener-policy: same-origin-allow-popups
cross-origin-embedder-policy: unsafe-none
x-response-time: 141
x-connection-hash: d29168d08eb4439a1e87f5d5234656e361f15325b079c5aaa156ea87b583d000
```

## GitHub

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.github.com -o /dev/null

HTTP/2 200
server: GitHub.com
date: Sat, 15 Jan 2022 16:25:45 GMT
content-type: text/html; charset=utf-8
vary: X-PJAX, X-PJAX-Container, Accept-Language, Accept-Encoding, Accept, X-Requested-With
permissions-policy: interest-cohort=()
content-language: en-US
etag: W/"d4406bbb5b88163f272b94947d7b2fca"
cache-control: max-age=0, private, must-revalidate
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
x-xss-protection: 0
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
expect-ct: max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"
content-security-policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/; connect-src 'self' uploads.github.com objects-origin.githubusercontent.com www.githubstatus.com collector.githubapp.com api.github.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events translator.github.com wss://alive.github.com github.githubassets.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com objects-origin.githubusercontent.com; frame-ancestors 'none'; frame-src render.githubusercontent.com viewscreen.githubusercontent.com notebooks.githubusercontent.com; img-src 'self' data: github.githubassets.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com secured-user-images.githubusercontent.com/ *.githubusercontent.com customer-stories-feed.github.com spotlights-feed.github.com; manifest-src 'self'; media-src github.com user-images.githubusercontent.com/ github.githubassets.com; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; worker-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/
accept-ranges: bytes
x-github-request-id: 2B45:1FFB:1ED7F0B:203CC0F:61E2F58E
```
