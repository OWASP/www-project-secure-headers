---
title: bestpractices
displaytext: Best Practices
layout: null
tab: true
order: 3
tags: headers
---

# Best Practices

* [Configuration proposal](#configuration-proposal)
* [Prevent information disclosure via HTTP headers](#prevent-information-disclosure-via-http-headers)
* [Prevent exposure to cross-site scripting when hosting uploaded files](#prevent-exposure-to-cross-site-scripting-when-hosting-uploaded-files)

## Configuration proposal

<!-- <div id=div-bestpractices class="ruletitle"></div> -->

Please note the best practices below suggest methods to change web server configuration to add headers. Security headers can also be successfully added to your application at the software level as well in almost every web language. Many web frameworks add some of these headers automatically.

The following section proposes a configuration for the [actively supported and working draft security headers](https://owasp.org/www-project-secure-headers/#div-headers).

💡 Additional information about HTTP security headers on [OpenCRE](https://opencre.org/cre/636-347?name=OWASP+Secure+Headers+Project&section=configuration&link=https%3A%2F%2Fowasp.org%2Fwww-project-secure-headers%2F%23div-bestpractices).

### Proposed values

⚠️ The `Pragma` header is only specified for backwards compatibility with the HTTP/1.0 caches.

💡 Content of the table below is also provided, as JSON, via this [file](ci/headers_add.json) (automatically updated).

<!-- HEADERS_ADD_TABLE_START -->

| Header name                                  | Proposed value  |
| ---------------------------------------------|------------|
| Strict-Transport-Security                    | `max-age=31536000 ; includeSubDomains` |
| X-Frame-Options                              | `deny` |
| X-Content-Type-Options                       | `nosniff` |
| Content-Security-Policy                      | `default-src 'self'; form-action 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content` |
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

## Prevent information disclosure via HTTP headers

<!-- <div id=div-bestpractices class="ruletitle"></div> -->

This section provides a collection of HTTP response headers to remove, when possible, from any HTTP response to prevent any [disclosure of technical information](https://cwe.mitre.org/data/definitions/200.html) about environment. The following list of headers can be used to configure a [reverse proxy](https://www.nginx.com/resources/glossary/reverse-proxy-server/) or a [web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall) to handle removal operation of the mentioned headers.

💡 Additional information about technical information disclosure in HTTP header on [OpenCRE](https://www.opencre.org/cre/403-005?name=OWASP+Secure+Headers+Project&section=Prevent+information+disclosure+via+HTTP+headers&link=https%3A%2F%2Fowasp.org%2Fwww-project-secure-headers%2F%23div-bestpractices_prevent-information-disclosure-via-http-headers).

💡 When an HTTP response header is known by the analytics site [WebTechSurvey](https://webtechsurvey.com/), then, a reference link is added to its usage statistics page. Otherwise, a reference link regarding the documentation of the header is provided.

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
| [Host-Header](https://webtechsurvey.com/response-header/host-header) | `owasp.org` | Indicate which virtual host of the web server the response is coming from. |
| [Pega-Host](https://webtechsurvey.com/response-header/pega-host) | `srv-pega11` | Indicate the internal host name of the server that handled the request in the context of usage of a software from the [PEGA](https://www.pega.com/) company. |
| [X-Atmosphere-first-request](https://github.com/Atmosphere/atmosphere) | `true` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Atmosphere-tracking-id](https://github.com/Atmosphere/atmosphere) | `7852fcbf-f8a9-4667-9dcc-a0b5b162499c` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Atmosphere-error](https://github.com/Atmosphere/atmosphere) | `Websocket protocol not supported` | Indicate that the java framework [Atmosphere](https://github.com/Atmosphere/atmosphere) is used. |
| [X-Mod-Pagespeed](https://webtechsurvey.com/response-header/x-mod-pagespeed) | `1.13.35.2-0` | Indicate the presence of the Apache module [mod_pagespeed](https://github.com/apache/incubator-pagespeed-mod) in the call flow. |
| [X-Page-Speed](https://webtechsurvey.com/response-header/x-page-speed) | `1.13.35.2-0` | Indicate the presence of the Nginx module [mod_pagespeed](https://github.com/apache/incubator-pagespeed-ngx) in the call flow. |
| [X-Varnish-Backend](https://webtechsurvey.com/response-header/x-varnish-backend) | `pb01` | Indicate the name of the backend server from which the [Varnish](https://varnish-cache.org) instance will accelerate the content. |
| [X-Varnish-Server](https://webtechsurvey.com/response-header/x-varnish-server) | `proxy01` | Indicate the name of the [Varnish](https://varnish-cache.org) server instance that provided the accelerated content. |
| [X-Envoy-Upstream-Service-Time](https://webtechsurvey.com/response-header/x-envoy-upstream-service-time) | `42` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [X-Envoy-Attempt-Count](https://webtechsurvey.com/response-header/x-envoy-attempt-count) | `1` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [X-Envoy-External-Address](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers) | `124.128.159.165` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [X-Envoy-Internal](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers) | `true` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [X-Envoy-Original-Dst-Host](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers) | `10.195.16.237:8888` | Indicate the presence of the proxy software [Envoy](https://www.envoyproxy.io) in the call flow. |
| [X-B3-ParentSpanId](https://webtechsurvey.com/response-header/x-b3-parentspanid) | `dea3f6d0324583db` | Indicate the presence of the software [Zipkin](https://zipkin.io/) that is a distributed tracing system. |
| [X-B3-Sampled](https://webtechsurvey.com/response-header/x-b3-sampled) | `0` | Indicate the presence of the software [Zipkin](https://zipkin.io/) that is a distributed tracing system. |
| [X-B3-SpanId](https://webtechsurvey.com/response-header/x-b3-spanid) | `244753d494e83353` | Indicate the presence of the software [Zipkin](https://zipkin.io/) that is a distributed tracing system. |
| [X-B3-TraceId](https://webtechsurvey.com/response-header/x-b3-traceid) | `11bef07b0f5c0468` | Indicate the presence of the software [Zipkin](https://zipkin.io/) that is a distributed tracing system. |
| [K-Proxy-Request](https://knative.dev/docs/serving/istio-authorization/) | `activator` | Indicate the presence of the software [Knative](https://knative.dev) that is an Open-Source Enterprise-level solution to build Serverless and Event Driven Applications in Kubernetes environments. |
| [X-Old-Content-Length](https://webtechsurvey.com/response-header/x-old-content-length) | `135` | Indicate the presence of the software [WebSEAL](https://www.ibm.com/docs/en/sva/8.0.1?topic=responses-filtering-changes-content-length-header) that is a high performance, multi-threaded web server by IBM. |
| [$wsep](https://www.ibm.com/docs/en/was/8.5.5?topic=SSEQTP_8.5.5/com.ibm.websphere.nd.multiplatform.doc/ae/rweb_custom_props.htm) | `empty value` | Indicate the presence of the software [WebSphere Application Server](https://www.ibm.com/products/websphere-application-server) that is a JavaEE application server by IBM. |
| [X-Nextjs-Matched-Path](https://webtechsurvey.com/response-header/x-nextjs-matched-path) | `/blog` | Indicate that the web framework [Next.js](https://nextjs.org/) is used. |
| [X-Nextjs-Page](https://webtechsurvey.com/response-header/x-nextjs-page) | `/articles` | Indicate that the web framework [Next.js](https://nextjs.org/) is used. |
| [X-Nextjs-Cache](https://webtechsurvey.com/response-header/x-nextjs-cache) | `REVALIDATED` | Indicate that the web framework [Next.js](https://nextjs.org/) is used. |
| [X-Nextjs-Redirect](https://github.com/search?q=repo%3Avercel%2Fnext.js%20X-Nextjs-Redirect&type=code) | `/home` | Indicate that the web framework [Next.js](https://nextjs.org/) is used. |
| [X-OneAgent-JS-Injection](https://webtechsurvey.com/response-header/x-oneagent-js-injection) | `true` | Indicate that the [Dynatrace](https://www.dynatrace.com) analytics and automation platform is used. |
| [X-ruxit-JS-Agent](https://webtechsurvey.com/response-header/X-ruxit-JS-Agent) | `true` | Indicate that the [Dynatrace](https://www.dynatrace.com) analytics and automation platform is used. |
| [X-dtHealthCheck](https://www.dynatrace.com/support/help/platform-modules/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum) | `Technical diagnostic data` | Indicate that the [Dynatrace](https://www.dynatrace.com) analytics and automation platform is used. |
| [X-dtAgentId](https://www.dynatrace.com/support/help/platform-modules/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum) | `95b3121c36` | Indicate that the [Dynatrace](https://www.dynatrace.com) analytics and automation platform is used. |
| [X-dtInjectedServlet](https://www.dynatrace.com/support/help/platform-modules/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum) | `com.company.ReportServlet` | Indicate that the [Dynatrace](https://www.dynatrace.com) analytics and automation platform is used. |
| [X-Litespeed-Cache-Control](https://webtechsurvey.com/response-header/X-Litespeed-Cache-Control) | `no-cache` | Indicate the presence of the [LiteSpeed](https://litespeedtech.com/) web server. |
| [X-LiteSpeed-Purge](https://webtechsurvey.com/response-header/X-LiteSpeed-Purge) | `/phpinfo.php` | Indicate the presence of the [LiteSpeed](https://litespeedtech.com/) web server. |
| [X-LiteSpeed-Tag](https://webtechsurvey.com/response-header/X-LiteSpeed-Tag) | `pubtag1,pubtag2` | Indicate the presence of the [LiteSpeed](https://litespeedtech.com/) web server. |
| [X-LiteSpeed-Vary](https://webtechsurvey.com/response-header/X-LiteSpeed-Vary) | `value=ismobile` | Indicate the presence of the [LiteSpeed](https://litespeedtech.com/) web server. |
| [X-LiteSpeed-Cache](https://webtechsurvey.com/response-header/X-LiteSpeed-Cache) | `hit,litemage` | Indicate the presence of the [LiteSpeed](https://litespeedtech.com/) web server. |

<!-- HEADERS_REMOVE_TABLE_END -->

## Prevent exposure to cross-site scripting when hosting uploaded files

This section describes, how the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used to prevent exposure to cross-site scripting when hosting uploaded files and opening them in the same web browsing context than the application.

It can happen a case in which an application allows a user to upload a file and then allow this file to be accessed by other users. If such feature allows uploading of HTML files (also apply for [SVG file](http://ghostlulz.com/xss-svg/)) then it can be used, as a vector, to store an HTML file containing JavaScript code. Therefore, the feature become prone to [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability.

To prevent this exposure, the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used with the following value to instruct browsers to download the file instead of open it in the same web browsing context than the application:

```
Content-Disposition: attachment; filename="myfile.html"
```
