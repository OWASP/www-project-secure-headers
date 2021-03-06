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

HTTP/1.1 302 Found
Location: https://www.google.com.br/?gws_rd=cr&dcr=0&ei=rtcKWpnkNYaawATUn6agCg
Cache-Control: private
Content-Type: text/html; charset=UTF-8
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Date: Tue, 14 Nov 2017 11:46:54 GMT
Server: gws
Content-Length: 273
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: NID=117=GENZIllQGZFmhCBmap1YThta_hUvvZ9Xm517XXWpF9eCKNqW6_luvZm1b_ai7BN4lAA2pP2Z22BveHqjUrqZxpY38NKSYLKWFGrVh6tGAHcbNw6OHQ_F77bNJWV0BZOZ; expires=Wed, 16-May-2018 11:46:54 GMT; path=/; domain=.google.com; HttpOnly
Alt-Svc: quic=":443"; ma=2592000; v="41,39,38,37,35"

HTTP/1.1 200 OK
Date: Tue, 14 Nov 2017 11:46:55 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=3600
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2017-11-14-11; expires=Thu, 14-Dec-2017 11:46:55 GMT; path=/; domain=.google.com.br
Set-Cookie: NID=117=fR73jhascV3B9fbiVfYdvGlilR_tgYNhela9rXdCavJiJoYpkNSTq0NtFqNSV8im602zM7Of-S1GUr_ncSuT3p6tzlw3e6_9ccqPttSuniTHWZEgBtUL1VXTgXBdjKMe; expires=Wed, 16-May-2018 11:46:55 GMT; path=/; domain=.google.com.br; HttpOnly
Alt-Svc: quic=":443"; ma=2592000; v="41,39,38,37,35"
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked
```

## Facebook

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.facebook.com -o /dev/null

HTTP/1.1 200 OK
X-XSS-Protection: 0
Pragma: no-cache
content-security-policy: default-src * data: blob:;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' fbstatic-a.akamaihd.net fbcdn-static-b-a.akamaihd.net *.atlassolutions.com blob: data: 'self';style-src data: blob: 'unsafe-inline' *;connect-src *.facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* *.akamaihd.net wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
Cache-Control: private, no-cache, no-store, must-revalidate
X-Frame-Options: DENY
expect-ct: max-age=10, report-uri="http://reports.fb.com/expectct/"
Strict-Transport-Security: max-age=15552000; preload
X-Content-Type-Options: nosniff
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Set-Cookie: fr=0Bf96eRMD0zCulvzh..BaCtgp.jl.AAA.0.0.BaCtgp.AWVGQojt; expires=Mon, 12-Feb-2018 11:48:57 GMT; Max-Age=7776000; path=/; domain=.facebook.com; secure; httponly
Set-Cookie: sb=KdgKWqMf8J84KfUg99AxaG1B; expires=Thu, 14-Nov-2019 11:48:57 GMT; Max-Age=63072000; path=/; domain=.facebook.com; secure; httponly
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
X-FB-Debug: llncdeFRYCCoWkXqx2VCdUGtdHZvjsr6OA7JNrtEe18ZuZAqcKCH4km9SSkNTHIcuXmzwRMzyBQt0Uz7T6ltQg==
Date: Tue, 14 Nov 2017 11:48:57 GMT
Transfer-Encoding: chunked
Connection: keep-alive
```

## Twitter

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.twitter.com -o /dev/null

HTTP/1.1 301 Moved Permanently
content-length: 0
date: Tue, 14 Nov 2017 11:50:11 GMT
location: https://twitter.com/
server: tsa_d
set-cookie: personalization_id="v1_nyz+ctxxDiBbh4s6VjzQIg=="; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
set-cookie: guest_id=v1%3A151066021116455299; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
strict-transport-security: max-age=631138519
x-connection-hash: d9a9eea848268dae67e7743d5bfd2dd5
x-response-time: 135

HTTP/1.1 200 OK
cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
content-length: 345977
content-security-policy: script-src https://connect.facebook.net https://cm.g.doubleclick.net https://ssl.google-analytics.com https://graph.facebook.com 'nonce-f/+1f61E6Z0qq8p+L4UIQw==' https://twitter.com 'unsafe-eval' https://*.twimg.com https://api.twitter.com https://analytics.twitter.com https://publish.twitter.com https://ton.twitter.com https://syndication.twitter.com https://www.google.com https://t.tellapart.com https://platform.twitter.com https://www.google-analytics.com blob: 'self'; frame-ancestors 'self'; font-src https://twitter.com https://*.twimg.com data: https://ton.twitter.com https://fonts.gstatic.com https://maxcdn.bootstrapcdn.com https://netdna.bootstrapcdn.com 'self'; media-src https://rmpdhdsnappytv-vh.akamaihd.net https://prod-video-eu-central-1.pscp.tv https://v.cdn.vine.co https://dwo3ckksxlb0v.cloudfront.net https://twitter.com https://amp.twimg.com https://smmdhdsnappytv-vh.akamaihd.net https://*.twimg.com https://prod-video-eu-west-1.pscp.tv https://rmmdhdsnappytv-vh.akamaihd.net https://prod-video-us-west-2.pscp.tv https://prod-video-us-west-1.pscp.tv https://prod-video-ap-northeast-1.pscp.tv https://smdhdsnappytv-vh.akamaihd.net https://ton.twitter.com https://rmdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://smpdhdsnappytv-vh.akamaihd.net https://prod-video-sa-east-1.pscp.tv https://mdhdsnappytv-vh.akamaihd.net https://prod-video-ap-southeast-2.pscp.tv https://mtc.cdn.vine.co https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv blob: 'self' https://prod-video-ap-southeast-1.pscp.tv https://mpdhdsnappytv-vh.akamaihd.net https://dev-video-eu-west-1.pscp.tv; connect-src https://rmpdhdsnappytv-vh.akamaihd.net https://prod-video-eu-central-1.pscp.tv https://graph.facebook.com https://*.giphy.com https://dwo3ckksxlb0v.cloudfront.net https://vmaprel.snappytv.com https://smmdhdsnappytv-vh.akamaihd.net https://*.twimg.com https://embed.pscp.tv https://api.twitter.com https://prod-video-eu-west-1.pscp.tv https://rmmdhdsnappytv-vh.akamaihd.net https://prod-video-us-west-2.pscp.tv https://pay.twitter.com https://prod-video-us-west-1.pscp.tv https://analytics.twitter.com https://vmap.snappytv.com https://*.twprobe.net https://prod-video-ap-northeast-1.pscp.tv https://smdhdsnappytv-vh.akamaihd.net https://syndication.twitter.com https://sentry.io https://rmdhdsnappytv-vh.akamaihd.net https://media.riffsy.com https://mmdhdsnappytv-vh.akamaihd.net https://embed.periscope.tv https://smpdhdsnappytv-vh.akamaihd.net https://prod-video-sa-east-1.pscp.tv https://vmapstage.snappytv.com https://upload.twitter.com https://proxsee.pscp.tv https://mdhdsnappytv-vh.akamaihd.net https://prod-video-ap-southeast-2.pscp.tv https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv 'self' https://vmap.grabyo.com https://prod-video-ap-southeast-1.pscp.tv https://mpdhdsnappytv-vh.akamaihd.net https://dev-video-eu-west-1.pscp.tv; style-src https://fonts.googleapis.com https://twitter.com https://*.twimg.com https://translate.googleapis.com https://ton.twitter.com 'unsafe-inline' https://platform.twitter.com https://maxcdn.bootstrapcdn.com https://netdna.bootstrapcdn.com 'self'; object-src https://twitter.com https://pbs.twimg.com; default-src 'self'; frame-src https://staticxx.facebook.com https://twitter.com https://*.twimg.com https://5415703.fls.doubleclick.net https://player.vimeo.com https://pay.twitter.com https://www.facebook.com https://ton.twitter.com https://syndication.twitter.com https://vine.co twitter: https://www.youtube.com https://platform.twitter.com https://upload.twitter.com https://s-static.ak.facebook.com https://4337974.fls.doubleclick.net https://8122179.fls.doubleclick.net 'self' https://donate.twitter.com; img-src https://prod-video-eu-central-1.pscp.tv https://prod-profile.pscp.tv https://graph.facebook.com https://prod-thumbnail.pscp.tv https://*.giphy.com https://twitter.com https://*.twimg.com https://ad.doubleclick.net https://prod-video-eu-west-1.pscp.tv data: https://prod-video-us-west-2.pscp.tv https://prod-video-us-west-1.pscp.tv https://prod-video-ap-northeast-1.pscp.tv https://lumiere-a.akamaihd.net https://fbcdn-profile-a.akamaihd.net https://www.facebook.com https://ton.twitter.com https://*.fbcdn.net https://syndication.twitter.com https://media.riffsy.com https://www.google.com https://prod-profile.periscope.tv https://prod-video-sa-east-1.pscp.tv https://stats.g.doubleclick.net https://platform.twitter.com https://prod-video-ap-southeast-2.pscp.tv https://api.mapbox.com https://www.google-analytics.com https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv blob: https://prod-thumbnail-small.pscp.tv https://prod-thumbnail-small.periscope.tv 'self' https://prod-thumbnail.periscope.tv https://prod-video-ap-southeast-1.pscp.tv https://dev-video-eu-west-1.pscp.tv; report-uri https://twitter.com/i/csp_report?a=NVQWGYLXFVZXO2LGOQ%3D%3D%3D%3D%3D%3D&ro=false;
content-type: text/html;charset=utf-8
date: Tue, 14 Nov 2017 11:50:11 GMT
expires: Tue, 31 Mar 1981 05:00:00 GMT
last-modified: Tue, 14 Nov 2017 11:50:11 GMT
pragma: no-cache
server: tsa_d
set-cookie: fm=0; Expires=Tue, 14 Nov 2017 11:50:02 UTC; Path=/; Domain=.twitter.com; Secure; HTTPOnly
set-cookie: _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMOCXbpfAToMY3NyZl9p%250AZCIlOTk3MjYzYzc1NDhkOTA1ZTlhZTIyNGE2Zjk5Nzg0NTk6B2lkIiU0ODIw%250AZWRkNjc4Njg2M2IzYmI3ZTA3N2YxMTA4YzE5Nw%253D%253D--7abf7eef950088f9f728686ce29881ef501487dd; Path=/; Domain=.twitter.com; Secure; HTTPOnly
set-cookie: personalization_id="v1_rrHzrB5h0Qs1Oz4uhOjFJg=="; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
set-cookie: guest_id=v1%3A151066021139105511; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
set-cookie: ct0=ba98c8a6cb4c664151a98c8bd9eb4b4d; Expires=Tue, 14 Nov 2017 17:50:11 UTC; Path=/; Domain=.twitter.com; Secure
status: 200 OK
strict-transport-security: max-age=631138519
x-connection-hash: 769f9dcd87b9274776136b99b3181a44
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-response-time: 359
x-transaction: 007d216900cbc2ad
x-twitter-response-tags: BouncerCompliant
x-ua-compatible: IE=edge,chrome=1
x-xss-protection: 1; mode=block
```

## Github

```
$ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.github.com -o /dev/null
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://github.com/

HTTP/1.1 200 OK
Server: GitHub.com
Date: Tue, 14 Nov 2017 11:51:27 GMT
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Status: 200 OK
Cache-Control: no-cache
Vary: X-PJAX
X-UA-Compatible: IE=Edge,chrome=1
Set-Cookie: logged_in=no; domain=.github.com; path=/; expires=Sat, 14 Nov 2037 11:51:27 -0000; secure; HttpOnly
Set-Cookie: _gh_sess=eyJzZXNzaW9uX2lkIjoiODI5ZGZjZDhlZDFlMjBjZTBhMTljMjk5ZDU1ZDBlODgiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUxMDY2MDI4NzMxNywiX2NzcmZfdG9rZW4iOiIvTjkya2RHLzJJN2dtbU12eWQ3UGJDeTJ0aU1tZHJrci8wVzlpMi9yajFZPSJ9--5920790d2e11e8d4a32177a14ac25fae6e8f9789; path=/; secure; HttpOnly
X-Request-Id: b31804a05047fd1326fe28cf3d6f33aa
X-Runtime: 0.036845
Expect-CT: max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"
Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src render.githubusercontent.com; connect-src 'self' uploads.github.com status.github.com collector.githubapp.com api.github.com www.google-analytics.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com wss://live.github.com; font-src assets-cdn.github.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; img-src 'self' data: assets-cdn.github.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com; media-src 'none'; script-src assets-cdn.github.com; style-src 'unsafe-inline' assets-cdn.github.com
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Public-Key-Pins: max-age=0; pin-sha256="WoiWRyIOVNa9ihaBciRSC7XHjliYS9VwUGOIud4PB18="; pin-sha256="RRM1dGqnDFsCJXBTHky16vi1obOlCgFFn/yOhI/y+ho="; pin-sha256="k2v657xBsOVe1PQRwOsHsw3bsGT2VzIqz5K+59sNQws="; pin-sha256="K87oWBWM9UZfyddvDfoxL+8lpNyoUB2ptGtn0fv6G2Q="; pin-sha256="IQBnNBEiFuhj+8x6X8XLgh01V9Ic5/V3IRQLNFFc7v4="; pin-sha256="iie1VXtL7HzAMF+/PVPR9xzT80kQxdZeJ+zduCB3uj0="; pin-sha256="LvRiGEjRqfzurezaWuj8Wie2gyHMrW5Q06LspMnox7A="; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-Runtime-rack: 0.043225
X-GitHub-Request-Id: 9AB0:25783:6A523:B814E:5A0AD8BE
```
