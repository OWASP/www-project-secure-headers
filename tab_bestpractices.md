---
title: bestpractices
displaytext: Best Practices
layout: null
tab: true
order: 5
tags: headers
---

# Best Practices

* [Configuration proposal](#configuration-proposal)
* [Prevent information disclosure via HTTP headers](#prevent-information-disclosure-via-http-headers)
* [Quickly check security HTTP headers for applications exposed on the Internet](#quickly-check-security-http-headers-for-applications-exposed-on-the-internet)
* [Quickly check security HTTP headers for applications exposed internally](#quickly-check-security-http-headers-for-applications-exposed-internally)

## Configuration proposal

Please note the best practices below suggest methods to change webserver configuration to add headers. Security headers can also be successfully added to your application at the software level as well in almost every web language. Many web frameworks add some of these headers automatically.

The following section propose a configuration for the [actively supported and working draft security headers](https://owasp.org/www-project-secure-headers/#div-headers).

### Proposed values

⚠️ The `Pragma` header is only specified for backwards compatibility with the HTTP/1.0 caches.

| Header name                                  | Proposed value  |
| ---------------------------------------------|------------|
| HTTP Strict Transport Security (HSTS)        | `max-age=31536000 ; includeSubDomains` |
| X-Frame-Options                              | `deny` |
| X-Content-Type-Options                       | `nosniff` |
| Content-Security-Policy                      | `default-src 'self'; object-src 'none'; child-src 'self'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content` |
| X-Permitted-Cross-Domain-Policies            | `none` |
| Referrer-Policy                              | `no-referrer`  |
| Clear-Site-Data                              | `"cache","cookies","storage"` |
| Cross-Origin-Embedder-Policy (COEP)          | `require-corp`   |
| Cross-Origin-Opener-Policy (COOP)            | `same-origin`   |
| Cross-Origin-Resource-Policy (CORP)          | `same-origin`  |
| Permissions-Policy                           | `accelerometer=(),autoplay=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),fullscreen=(),geolocation=(),gyroscope=(),magnetometer=(),microphone=(),midi=(),payment=(),picture-in-picture=(),publickey-credentials-get=(),screen-wake-lock=(),sync-xhr=(self),usb=(),web-share=(),xr-spatial-tracking=()` |
| Cache-Control         | `no-store, max-age=0`  |
| Pragma         | `no-cache`  |

### Web server syntax

This section indicate the syntax to use to set a HTTP header according to the web server targeted.

| Web server name | Syntax  |
| ----------------|---------|
| Apache          | `Header always set [HEADER_NAME] [PROPOSED_VALUE]` |
| Nginx           | `add_header [HEADER_NAME] [PROPOSED_VALUE] always;` |
| Lighttpd        | `setenv.add-response-header = ("[HEADER_NAME]" => "[PROPOSED_VALUE]")` |
| IIS             | Refer to this [documentation](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/httpprotocol/customheaders/). |

## Quickly check security HTTP headers for applications exposed on the Internet

The online tool [securityheaders.com](https://securityheaders.com) can be used to achieve that objective.

It returns the grade in the following HTTP response headers:

* **x-score**: Contains a Base64 encoded JSON object with the grade letter and its associated color name.
* **x-grade**: Contains the grade letter.

```shell
$ curl -v "https://securityheaders.com/?hide=on&followRedirects=on&q=https://mozilla.org"
> Trying 104.21.70.128:443...
> Connected to securityheaders.com (104.21.70.128) port 443
> ...
< HTTP/2 200
< date: Tue, 02 Mar 2021 17:29:23 GMT
< content-type: text/html; charset=UTF-8
< vary: Accept-Encoding
< x-score: eyJzY29yZSI6IkEiLCAiY29sb3VyIjoiZ3JlZW4ifQ==
< x-grade: A
< ...
```

Content of the **x-score** header value:

```shell
$ echo eyJzY29yZSI6IkEiLCAiY29sb3VyIjoiZ3JlZW4ifQ== | base64 -d
{"score":"A", "colour":"green"}
```

## Quickly check security HTTP headers for applications exposed internally

The portable cross-platform tool [Venom](https://github.com/ovh/venom) with the dedicated [test suites aligned with the OWASP Secure Headers Project](https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056) can be used to achieve that objective.

Use the following set of commands:

```shell
# Get Venom binary file from 
# https://github.com/ovh/venom/releases
# Get the YAML test suites from
# https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056
# Demonstration about usage available on
# https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056#gistcomment-3630811
$ venom run --var="target_site=https://mozilla.org" --var="logout_url=/logout" venom_security_headers_tests_suite.yml
• HTTP security response headers test suites (venom_security_headers_tests_suite.yml)
    • Strict-Transport-Security SUCCESS
    • X-Frame-Options SUCCESS
    • X-Content-Type-Options SUCCESS
    • Content-Security-Policy FAILURE
    • X-Permitted-Cross-Domain-Policies SUCCESS
    • Referrer-Policy SUCCESS
    • Clear-Site-Data SUCCESS
    • Cross-Origin-Embedder-Policy SUCCESS
    • Cross-Origin-Opener-Policy SUCCESS
    • Cross-Origin-Resource-Policy SUCCESS
    • Permissions-Policy SUCCESS    
    • Cache-Control SUCCESS    
    • Feature-Policy SUCCESS
        [info] This header was split into Permissions-Policy and Document-Policy and will be considered deprecated once all impacted features are moved off of feature policy. (venom_security_headers_tests_suite.yml:152)
    • Public-Key-Pins SUCCESS
        [info] This header has been deprecated by all major browsers and is no longer recommended. Avoid using it, and update existing code if possible! (venom_security_headers_tests_suite.yml:164)
    • Expect-CT SUCCESS
        [info] This header will likely become obsolete in June 2021. Since May 2018 new certificates are expected to support SCTs by default. Certificates before March 2018 were allowed to have a lifetime of 39 months, those will all be expired in June 2021. (venom_security_headers_tests_suite.yml:175)
    • X-Xss-Protection SUCCESS
        [info] The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side. (venom_security_headers_tests_suite.yml:189)
    • SecurityHeaders-Rating SKIPPED
```

## Prevent information disclosure via HTTP headers

This section provides a collection of HTTP response headers to remove, when possible, from any HTTP response to prevent any [disclosure of technical information](https://cwe.mitre.org/data/definitions/200.html) on production environment. The following list of headers can be used to configure a reverse proxy or a web application firewall to handle removal operation of the mentioned headers.

⚠️ The [Server](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Server) header can be a source of information disclosure. Therefore, ensure that it does not contain any technical detail about the server in use (example of value `ATS/8.0.8`).

| Header name         | Header value example | Description |
| --------------------|----------------------|-------------|
| `X-Powered-By` | `PHP/5.3.3` | Contain information about hosting environments or other frameworks in use. |
| `SourceMap` or `X-SourceMap` | `https://mysite.com/js/mylib.js.map`| Links generated code to a [source map](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map), enabling the browser to reconstruct the original source and present the reconstructed original in the debugger (source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap)). |
| `X-AspNetMvc-Version` | `5.2` | Contain the version of the ASP DotNet MVC framework in use. |
| `X-AspNet-Version` | `4.0.30319` | Contain the version of the ASP DotNet framework in use. |
| `X-SourceFiles`  | `=?UTF-8?B?QzpcVXNlcnN?=` | Contain information needed by the .NET SDK debugger during debugging operation on a project. |
| `X-Redirect-By` | `TYPO3 Shortcut/Mountpoint` | Specifies the component that is responsible for a particular redirect (source [Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)). |
| `Liferay-Portal` | `Liferay Digital Experience Platform 7.2.10 GA1` | Contain the version of the [Liferay](https://www.liferay.com) platform in use. |

References (*when found*):

* `X-Powered-By`:
    * <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers>
* `SourceMap / X-SourceMap`:
    * <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap>
    * <https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map>
* `X-Redirect-By`:
    * <https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/PageTypes/RedirectHeaders.html>
    * <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields>