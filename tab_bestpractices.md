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
* [Prevent exposure to cross-site scripting when hosting uploaded files](#prevent-exposure-to-cross-site-scripting-when-hosting-uploaded-files)
* [Quickly check security HTTP headers for applications exposed on the Internet](#quickly-check-security-http-headers-for-applications-exposed-on-the-internet)
* [Quickly check security HTTP headers for applications exposed internally](#quickly-check-security-http-headers-for-applications-exposed-internally)

## Configuration proposal

Please note the best practices below suggest methods to change web server configuration to add headers. Security headers can also be successfully added to your application at the software level as well in almost every web language. Many web frameworks add some of these headers automatically.

The following section proposes a configuration for the [actively supported and working draft security headers](https://owasp.org/www-project-secure-headers/#div-headers).

### Proposed values

⚠️ The `Pragma` header is only specified for backwards compatibility with the HTTP/1.0 caches.

💡 Content of the table below is also provided, as JSON, via this [file](ci/headers_add.json) (automatically updated).

<!-- HEADERS_ADD_TABLE_START -->

| Header name                                  | Proposed value  |
| ---------------------------------------------|------------|
| Strict-Transport-Security                    | `max-age=31536000 ; includeSubDomains` |
| X-Frame-Options                              | `deny` |
| X-Content-Type-Options                       | `nosniff` |
| Content-Security-Policy                      | `default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content` |
| X-Permitted-Cross-Domain-Policies            | `none` |
| Referrer-Policy                              | `no-referrer`  |
| Clear-Site-Data                              | `"cache","cookies","storage"` |
| Cross-Origin-Embedder-Policy                 | `require-corp`   |
| Cross-Origin-Opener-Policy                   | `same-origin`   |
| Cross-Origin-Resource-Policy                 | `same-origin`  |
| Permissions-Policy                           | `accelerometer=(),ambient-light-sensor=(),autoplay=(),battery=(),camera=(),display-capture=(),document-domain=(),encrypted-media=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),layout-animations=(self),legacy-image-formats=(self),magnetometer=(),microphone=(),midi=(),oversized-images=(self),payment=(),picture-in-picture=(),publickey-credentials-get=(),speaker-selection=(),sync-xhr=(self),unoptimized-images=(self),unsized-media=(self),usb=(),screen-wake-lock=(),web-share=(),xr-spatial-tracking=()` |
| Cache-Control         | `no-store, max-age=0`  |
| Pragma         | `no-cache`  |

<!-- HEADERS_ADD_TABLE_END -->

### Web server syntax

This section indicates the syntax to use to set an HTTP header according to the web server targeted.

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

The portable cross-platform tool [Venom](https://github.com/ovh/venom) with the dedicated [OSHP Validator test suites aligned with the OWASP Secure Headers Project](https://github.com/oshp/oshp-validator).

Use the following example set of commands:

```shell
# Get Venom binary file from 
# https://github.com/ovh/venom/releases
# Get the YAML test suites from
# check out project https://github.com/oshp/oshp-validator
# Read the README.md, additional demonstration about usage available on
# https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056#gistcomment-3630811
$ venom run --var="target_site=https://mozilla.org" --var="logout_url=/logout" tests_suite.yml
• HTTP security response headers test suites
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
        [info] This header was split into Permissions-Policy and Document-Policy and will be considered deprecated once all impacted features are moved off of feature policy.
    • Public-Key-Pins SUCCESS
        [info] This header has been deprecated by all major browsers and is no longer recommended. Avoid using it, and update existing code if possible!
    • Expect-CT SUCCESS
        [info] This header will likely become obsolete in June 2021. Since May 2018 new certificates are expected to support SCTs by default. Certificates before March 2018 were allowed to have a lifetime of 39 months, those will all be expired in June 2021.
    • X-Xss-Protection SUCCESS
        [info] The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side.
    • SecurityHeaders-Rating SKIPPED
```

## Prevent information disclosure via HTTP headers

This section provides a collection of HTTP response headers to remove, when possible, from any HTTP response to prevent any [disclosure of technical information](https://cwe.mitre.org/data/definitions/200.html) about environment. The following list of headers can be used to configure a [reverse proxy](https://www.nginx.com/resources/glossary/reverse-proxy-server/) or a [web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall) to handle removal operation of the mentioned headers.

💡 Content of the table below is also provided, as JSON, via this [file](ci/headers_remove.json) (automatically updated).

<!-- HEADERS_REMOVE_TABLE_START -->

| Header name         | Header value example | Description |
| --------------------|----------------------|-------------|
| [Server](https://webtechsurvey.com/response-header/server) | `Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips` | Contain information about the server handling the request. |
| [Liferay-Portal](https://webtechsurvey.com/response-header/liferay-portal) | `Liferay Digital Experience Platform 7.2.10 GA1` | Contain the version of the [Liferay](https://www.liferay.com) software in use. |
| [X-Turbo-Charged-By](https://webtechsurvey.com/response-header/x-turbo-charged-by) | `LiteSpeed/5.4.12 Enterprise` | Contain information about the server handling the request. |
| [X-Powered-By](https://webtechsurvey.com/response-header/x-powered-by) | `PHP/5.3.3` | Contain information about hosting environments or other frameworks in use. |
| [X-Server-Powered-By](https://webtechsurvey.com/response-header/x-server-powered-by) | `Engintron` | Contain information about hosting environments or other frameworks in use. |
| [X-Powered-CMS](https://webtechsurvey.com/response-header/x-powered-cms) | `Bitrix Site Manager (DEMO)` | Contain the information about the [CMS](https://en.wikipedia.org/wiki/Content_management_system) that generated the HTTP response. |
| [SourceMap](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap) | `https://mysite.com/js/mylib.js.map`| Links generated code to a [source map](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map) file, enabling the browser to reconstruct the original source and present the reconstructed original in the debugger. |
| [X-SourceMap](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/SourceMap) | `https://mysite.com/js/mylib.js.map`| Links generated code to a [source map](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map) file, enabling the browser to reconstruct the original source and present the reconstructed original in the debugger. |
| [X-AspNetMvc-Version](https://webtechsurvey.com/response-header/x-aspnetmvc-version) | `5.2` | Contain the version of the ASP .Net MVC framework in use. |
| [X-AspNet-Version](https://webtechsurvey.com/response-header/x-aspnet-version) | `4.0.30319` | Contain the version of the ASP .Net framework in use. |
| [X-SourceFiles](https://webtechsurvey.com/response-header/x-sourcefiles)  | `=?UTF-8?B?QzpcVXNlcnN?=` | Contain information needed by the .Net SDK debugger during debugging operation on a project. |
| [X-Redirect-By](https://webtechsurvey.com/response-header/x-redirect-by) | `TYPO3 Shortcut/Mountpoint` | Specifies the component that is responsible for a particular redirect (source [Wikipedia](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)). |
| [X-Generator](https://webtechsurvey.com/response-header/x-generator) | `Drupal 8` | Contain the information about the [CMS](https://en.wikipedia.org/wiki/Content_management_system) that generated the HTTP response. |
| [X-Generated-By](https://webtechsurvey.com/response-header/x-generated-by) | `Smartsite version 7.11.1.3` | Contain the information about the [CMS](https://en.wikipedia.org/wiki/Content_management_system) that generated the HTTP response. |
| [X-CMS](https://webtechsurvey.com/response-header/x-cms) | `Thinq CMS 1.7.0.0` | Contain the information about the [CMS](https://en.wikipedia.org/wiki/Content_management_system) that generated the HTTP response. |
| [X-Powered-By-Plesk](https://webtechsurvey.com/response-header/x-powered-by-plesk) | `PleskLin` or `PleskWin` | Indicate that the platform is based on the [Plesk](https://www.plesk.com) software in addition to the underlying operating system. |
| [X-Php-Version](https://webtechsurvey.com/response-header/x-php-version) | `7.4` | Indicate the version of [PHP](https://www.php.net) technology used. |
| [Powered-By](https://webtechsurvey.com/response-header/powered-by) | `PrestaShop` | Indicate the name of the framework or platform used. |
| [X-Content-Encoded-By](https://webtechsurvey.com/response-header/x-content-encoded-by) | `Joomla! 2.5` | Indicate the name of the framework or platform used. |
| [Product](https://webtechsurvey.com/response-header/product) | `Z-BlogPHP 1.7.2` | Indicate the name of the framework or platform used. |
| [X-CF-Powered-By](https://webtechsurvey.com/response-header/x-cf-powered-by) | `CF-Joomla 0.1.5` | Indicate the name of the framework or platform used. |
| [X-Framework](https://webtechsurvey.com/response-header/x-framework) | `JP/4.01` | Indicate the name of the framework or platform used. |
| [Host-Header](https://webtechsurvey.com/response-header/host-header) | `CorpAxe.com` | Indicate which virtual host of the web server the response is coming from. |
| [X-Envoy-Upstream-Service-Time](https://webtechsurvey.com/response-header/x-envoy-upstream-service-time) | `42` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [Pega-Host](https://webtechsurvey.com/response-header/pega-host) | `srv-pega11` | Indicate the internal host name of the server that handled the request in the context of usage of a software from the [PEGA](https://www.pega.com/) company. |
| [X-Atmosphere-first-request](https://github.com/Atmosphere/atmosphere) | `true` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Atmosphere-tracking-id](https://github.com/Atmosphere/atmosphere) | `7852fcbf-f8a9-4667-9dcc-a0b5b162499c` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Atmosphere-error](https://github.com/Atmosphere/atmosphere) | `Websocket protocol not supported` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Mod-Pagespeed](https://webtechsurvey.com/response-header/x-mod-pagespeed) | `1.13.35.2-0` | Indicate the presence of the Apache module [mod_pagespeed](https://github.com/apache/incubator-pagespeed-mod) in the call flow. |
| [X-Page-Speed](https://webtechsurvey.com/response-header/x-page-speed) | `1.13.35.2-0` | Indicate the presence of the Nginx module [mod_pagespeed](https://github.com/apache/incubator-pagespeed-mod) in the call flow. |

<!-- HEADERS_REMOVE_TABLE_END -->

## Prevent exposure to cross-site scripting when hosting uploaded files

This section describes, how the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used to prevent exposure to cross-site scripting when hosting uploaded files and opening them in the same web browsing context than the application.

It can happen a case in which an application allows a user to upload a file and then allow this file to be accessed by other users. If such feature allows uploading of HTML files (also apply for [SVG file](http://ghostlulz.com/xss-svg/)) then it can be used, as a vector, to store an HTML file containing JavaScript code. Therefore, the feature become prone to [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability.

To prevent this exposure, the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used with the following value to instruct browsers to download the file instead of open it in the same web browsing context than the application:

```
Content-Disposition: attachment; filename="myfile.html"
```
