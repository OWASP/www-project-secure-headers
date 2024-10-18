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
* [Prevent CORS misconfiguration issues](#prevent-cors-misconfiguration-issues)
* [Prevent information disclosure via the browser local cached files](#prevent-information-disclosure-via-the-browser-local-cached-files)
* [Prevent CSP bypasses](#prevent-csp-bypasses)

## Configuration proposal

<!-- <div id=div-bestpractices class="ruletitle"></div> -->

Please note the best practices below suggest methods to change web server configuration to add headers. Security headers can also be successfully added to your application at the software level as well in almost every web language. Many web frameworks add some of these headers automatically.

The following section proposes a configuration for the [actively supported and working draft security headers](https://owasp.org/www-project-secure-headers/#div-headers).

💡 Additional information about HTTP security headers on [OpenCRE](https://opencre.org/cre/636-347?name=OWASP+Secure+Headers+Project&section=configuration&link=https%3A%2F%2Fowasp.org%2Fwww-project-secure-headers%2F%23div-bestpractices).

📖 The headers proposed below can be applied both in the context of a *classic web application* and in that of a *web API*.

🚩 The header `Clear-Site-Data` will cause the browser to take additional processing time for the HTTP response, so, set it to the logout function when possible.

🔬 For the header `Permissions-Policy`, as it is currently only supported by [Chromium based browsers](https://caniuse.com/permissions-policy), the proposed value was generated with this [site](https://www.permissionspolicy.com/) and tested against the version `128.0.6606.0` of [Chromium](https://chromium.woolyss.com/download/en/) to only specify supported features.

💡 Content of the table below is also provided, as JSON, via this [file](ci/headers_add.json) (automatically updated).

<!-- HEADERS_ADD_TABLE_START -->

| Header name                                  | Proposed value  |
| ---------------------------------------------|------------|
| Strict-Transport-Security                    | `max-age=31536000; includeSubDomains` |
| X-Frame-Options                              | `deny` |
| X-Content-Type-Options                       | `nosniff` |
| Content-Security-Policy                      | `default-src 'self'; form-action 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content` |
| X-Permitted-Cross-Domain-Policies            | `none` |
| Referrer-Policy                              | `no-referrer`  |
| Clear-Site-Data                              | `"cache","cookies","storage"` |
| Cross-Origin-Embedder-Policy                 | `require-corp`   |
| Cross-Origin-Opener-Policy                   | `same-origin`   |
| Cross-Origin-Resource-Policy                 | `same-origin`  |
| Permissions-Policy                           | `accelerometer=(), autoplay=(), camera=(), cross-origin-isolated=(), display-capture=(), encrypted-media=(), fullscreen=(), geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(), midi=(), payment=(), picture-in-picture=(), publickey-credentials-get=(), screen-wake-lock=(), sync-xhr=(self), usb=(), web-share=(), xr-spatial-tracking=(), clipboard-read=(), clipboard-write=(), gamepad=(), hid=(), idle-detection=(), interest-cohort=(), serial=(), unload=()` |
| Cache-Control         | `no-store, max-age=0`  |

<!-- HEADERS_ADD_TABLE_END -->

## Prevent information disclosure via HTTP headers

<!-- <div id=div-bestpractices class="ruletitle"></div> -->

This section provides a collection of HTTP response headers to remove, when possible, from any HTTP response to prevent any [disclosure of technical information](https://cwe.mitre.org/data/definitions/200.html) about environment. The following list of headers can be used to configure a [reverse proxy](https://www.nginx.com/resources/glossary/reverse-proxy-server/) or a [web application firewall](https://en.wikipedia.org/wiki/Web_application_firewall) to handle removal operation of the mentioned headers.

💡 Additional information about technical information disclosure in HTTP header on [OpenCRE](https://www.opencre.org/cre/403-005?name=OWASP+Secure+Headers+Project&section=Prevent+information+disclosure+via+HTTP+headers&link=https%3A%2F%2Fowasp.org%2Fwww-project-secure-headers%2F%23div-bestpractices_prevent-information-disclosure-via-http-headers).

💡 When an HTTP response header is known by the analytics site [WebTechSurvey](https://webtechsurvey.com/), then, a reference link is added to its usage statistics page. Otherwise, a reference link regarding the documentation of the header is provided.

🚩 The response header `Content-Type` can sometimes discloses the web framework used. It is the case for the following ones:

* [Spring Boot Actuator REST API](https://docs.spring.io/spring-boot/api/rest/actuator/auditevents.html): `Content-Type: application/vnd.spring-boot.actuator.v3+json`.

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
| [X-Old-Content-Length](https://webtechsurvey.com/response-header/x-old-content-length) | `135` | Indicate the presence of the software [WebSEAL](https://www.ibm.com/docs/en/samfm/8.0.1.2?topic=overview-webseal-introduction) that is a high performance, multithreaded web server by IBM. |
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
| [X-Umbraco-Version](https://webtechsurvey.com/response-header/X-Umbraco-Version) | `4.7` | Indicate the usage of the [Umbraco CMS](https://umbraco.com/products/umbraco-cms/) software as well as its version. |
| [OracleCommerceCloud-Version](https://webtechsurvey.com/response-header/OracleCommerceCloud-Version) | `23.08.01` | Indicate the usage of the [Oracle Commerce](https://www.oracle.com/cx/ecommerce/) software as well as its version. |
| [X-BEServer](https://webtechsurvey.com/response-header/x-beserver) | `EXSRV01` | Indicate the internal host name of the server that handled the request in the context of usage of the [Microsoft Exchange](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-ashttp/08ad30b6-5b73-41bc-890b-1cab2cf49827) software. |
| [X-DiagInfo](https://webtechsurvey.com/response-header/x-diaginfo) | `EXSRV01` | Indicate the internal host name of the server that handled the request in the context of usage of the [Microsoft Exchange](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-ashttp/08ad30b6-5b73-41bc-890b-1cab2cf49827) software. |
| [X-FEServer](https://webtechsurvey.com/response-header/x-feserver) | `EXSRV01` | Indicate the internal host name of the server that handled the request in the context of usage of the [Microsoft Exchange](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-ashttp/08ad30b6-5b73-41bc-890b-1cab2cf49827) software. |
| [X-CalculatedBETarget](https://webtechsurvey.com/response-header/x-calculatedbetarget) | `exsrv01.mydomain.com` | Indicate the internal host name of the server that handled the request in the context of usage of the [Microsoft Exchange](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-ashttp/08ad30b6-5b73-41bc-890b-1cab2cf49827) software. |
| [X-OWA-Version](https://webtechsurvey.com/response-header/x-owa-version) | `15.2.1258.27` | Indicate the version of the Microsoft Exchange software in use. |
| [X-Cocoon-Version](https://webtechsurvey.com/response-header/x-cocoon-version) | `2.1.13` | Indicate that the web framework [Apache Cocoon](https://cocoon.apache.org/) is used as well as the version used. |
| [X-Kubernetes-PF-FlowSchema-UI](https://kubernetes.io/docs/reference/debug-cluster/flow-control) | `cf931e2d-5a5e-4c12-892c-9bafa71f30dc` | Indicate that the web application issuing the HTTP response is deployed on a [Kubernetes](https://kubernetes.io/) cluster. |
| [X-Kubernetes-PF-PriorityLevel-UID](https://kubernetes.io/docs/reference/debug-cluster/flow-control) | `78b3face-e1cf-4fc6-a27e-08eb7f0f5b23` | Indicate that the web application issuing the HTTP response is deployed on a [Kubernetes](https://kubernetes.io/) cluster. |
| [X-Jitsi-Release](https://webtechsurvey.com/response-header/x-jitsi-release) | `5082` | Indicate the version of [Jitsi](https://github.com/jitsi/jitsi) software in use. |
| [X-Joomla-Version](https://webtechsurvey.com/response-header/x-joomla-version) | `3.9.25` |Indicate that the CMS [Joomla](https://www.joomla.org/) is used as well as the version used. |
| [X-Backside-Transport](https://webtechsurvey.com/response-header/x-backside-transport) | `OK OK` |Indicate the presence of the products [IBM WebSphere DataPower](https://www.ibm.com/products/datapower-gateway) in the call flow.|

<!-- HEADERS_REMOVE_TABLE_END -->

## Prevent exposure to cross-site scripting when hosting uploaded files

This section describes, how the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used to prevent exposure to cross-site scripting when hosting uploaded files and opening them in the same web browsing context than the application.

It can happen a case in which an application allows a user to upload a file and then allow this file to be accessed by other users. If such feature allows uploading of HTML files (also apply for [SVG file](https://hackerone.com/reports/1276742)) then it can be used, as a vector, to store an HTML file containing JavaScript code. Therefore, the feature become prone to [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability.

To prevent this exposure, the HTTP response header named [Content-Disposition](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition), can be used with the following value to instruct browsers to download the file instead of open it in the same web browsing context than the application:

```text
Content-Disposition: attachment; filename="myfile.html"
```

## Prevent CORS misconfiguration issues

> 📖 An excellent tutorial about [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (called **CORS**) is provided on the [Mozilla MDN](https://developer.mozilla.org/en-US/). In addition, [Julien Cretel](https://jub0bs.com/about/) provided a great [blog post](https://jub0bs.com/posts/2023-02-08-fearless-cors/) about CORS pitfalls.

This section proposes an approach to help preventing [CORS misconfiguration issues](https://portswigger.net/research/exploiting-cors-misconfigurations-for-bitcoins-and-bounties) using a simple idea: *Provide the collection of [CORS related HTTP response headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers) to use according to different contexts.*

### Key points to consider

* 💡 If the web framework/web server you are using provides CORS features then always leverage them instead of implements it manually:
  * [List of web framework/web server](https://enable-cors.org/server.html) supporting CORS.
  * [CORS middleware for Go](https://pkg.go.dev/github.com/jub0bs/cors) by Julien Cretel.

* 🚩 Whatever the context, when the request is a **HTTP OPTIONS** ([preflight request](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests)) then the value provided by the following headers must be validated against expected values. If the validation failed then return an HTTP 403 **without any [CORS related HTTP response headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers)**:

  * [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#origin)
  * [Access-Control-Request-Method](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#access-control-request-method)
  * [Access-Control-Request-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#access-control-request-headers)

* 🚩 Validation of the `Origin` / `Access-Control-Request-Method` / `Access-Control-Request-Headers` request header value, against a list of allowed ones, must be performed using [strict case sensitive string comparison](https://jub0bs.com/posts/2023-02-08-fearless-cors/#violation-of-the-case-sensitivity-of-method-names) to prevent, as much as possible, the [presence of bypasses into the validation logic](https://portswigger.net/web-security/cors#errors-parsing-origin-headers). If possible, does not use regular expression for the implementation of the validation, see [here](https://jub0bs.com/posts/2023-02-08-fearless-cors/#disallow-dangerous-origin-patterns) for an explanation of the source of this recommendation.

* 🚩 CORS scope is the access control aspect, from a browser perspective (client side), regarding [cross origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin) access to a resource. Thus, it **does NOT replace** the requirement to implements access control on the server side too. CORS and server-side access controls are complementary.

* 🚩 Never take the value of the request header [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#origin) to add it into the response header [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#access-control-allow-origin) (mirroring), see [here](https://portswigger.net/web-security/cors#server-generated-acao-header-from-client-specified-origin-header) for an explanation of the source of this recommendation. Indeed, always use a list of allowed origins when only a restricted collection of origins is expected to call your endpoints.

### Contexts

#### Public without authentication

💬 Context:

Your endpoints are expected to be consumed, by a browser, from any origins without any authentication.

💻 Configuration proposal:

```text
Access-Control-Allow-Origin: *
Access-Control-Max-Age: 3600
Access-Control-Allow-Credentials: false
```

#### Public with authentication

💬 Context:

Your endpoints are expected to be consumed, by a browser, from any origins with authentication.

🚩 The value `*`, for the response header `Access-Control-Allow-Origin`, cannot be used when the response header `Access-Control-Allow-Credentials` is allowed (`true`). Indeed, the browser raises the following error (tested on Chrome 118.x):

```text
The value of the 'Access-Control-Allow-Origin' header in the response must not be 
the wildcard '*' when the request's credentials mode is 'include'.
```

📖 It is explicitly mentioned, into the [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) documentation, as the following:

```text
When responding to a "credentialed request" request, the server must specify an origin in the value 
of the Access-Control-Allow-Origin header, instead of specifying the "*" wildcard.
```

Therefore, refer to the [restricted with authentication](#restricted-with-authentication) case for the configuration to use.

#### Restricted without authentication

💬 Context:

Your endpoints are expected to be consumed, by a browser, from a specific collection of origins without any authentication.

💻 Configuration proposal:

* If the value of the request header [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#origin) is present into the **list of allowed Origins** then:

```text
Access-Control-Allow-Origin: [Value_Taken_From_The_List_Of_Allowed_Origins]
Access-Control-Max-Age: 10
Access-Control-Allow-Credentials: false
```

* Otherwise return an HTTP 403 **without any [CORS related HTTP response headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers)**.

#### Restricted with authentication

💬 Context:

Your endpoints are expected to be consumed, by a browser, from a specific collection of origins with authentication.

💻 Configuration proposal:

* If the value of the request header [Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#origin) is present into the **list of allowed Origins** then:

```text
Access-Control-Allow-Origin: [Value_Taken_From_The_List_Of_Allowed_Origins]
Access-Control-Max-Age: 10
Access-Control-Allow-Credentials: true
```

* Otherwise return an HTTP 403 **without any [CORS related HTTP response headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#the_http_response_headers)**.

### Test CORS configuration

The tools [nuclei](https://github.com/projectdiscovery/nuclei) can be used, via the template named [cors-misconfig](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/generic/cors-misconfig.yaml), to test a CORS configuration.

💻 Command to use:

```bash
$ nuclei -silent -template-id cors-misconfig -u https://domain.com
[cors-misconfig:arbitrary-origin] [http] [info] https://domain.com [...]
```

### References

* <https://portswigger.net/web-security/cors>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS>
* <https://jub0bs.com/posts/2023-02-08-fearless-cors/>
* <https://enable-cors.org/>
* <https://developer.mozilla.org/en-US/docs/Glossary/Origin>
* <https://cwe.mitre.org/data/definitions/942.html>
* <https://cwe.mitre.org/data/definitions/346.html>
* [OWASP WSTG - Testing Cross Origin Resource Sharing](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing)
* <https://pkg.go.dev/github.com/jub0bs/cors>

## Prevent information disclosure via the browser local cached files

This section describes why it is important to specify a **caching policy**, via the [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) HTTP response header, when sensitive information is managed by a web-based application.

### Context

💬 The application allows a user to access to documents containing information, considered sensitive, from a confidentiality perspective.

Let's assume that the application returns the following HTTP response to a request, in which, no caching policy is defined:

```text
HTTP/1.1 200 OK
accept-ranges: bytes
content-length: 433994
content-type: application/pdf
date: Sat, 30 Mar 2024 10:06:34 GMT
server: LiteSpeed
```

So, the browser will store a copy of the file (here a PDF one) into its cache storage for a certain amount of time.

🚩 **Consequence:** Any application running on the user's computer, will be able to access to the file (at least if executed as the user identity or an administrator one) causing an exposure of the resource to non-expected entities.

📺 This [demonstration video](assets/misc/demo_information_disclosure_via_browser_file_caching.mp4) show an example, of such information disclosure, via a file cached by the browser.

### Configuration proposal

💻 To prevent such issue, the following **caching policy** can be specified:

```text
Cache-Control: no-store, max-age=0
```

👀 Where:

* `no-store`: Is used to indicate that the response may not be stored in any cache.
* `max-age=0`: Is used to force the expiration of any cached version of the resources associated to the response.

💡 The HTTP response header [Clear-Site-Data](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data) can also be leveraged, in addition, to instruct the browser to remove any cached data related to the application.

### Other vulnerabilities related to caching

📖 An excellent research and course content, about [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning), is provided by the [PortSwigger team](https://portswigger.net/).

### References

* <https://redbot.org>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching>
* <https://caniuse.com/mdn-http_headers_cache-control>
* <https://cwe.mitre.org/data/definitions/525.html>
* <https://cwe.mitre.org/data/definitions/524.html>
* [OWASP WSTG - Testing for Browser Cache Weaknesses](https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/04-Authentication_Testing/06-Testing_for_Browser_Cache_Weaknesses)
* <https://portswigger.net/kb/issues/00700100_cacheable-https-response>
* <https://portswigger.net/web-security/web-cache-poisoning>
* <https://portswigger.net/web-security/web-cache-deception>
* <https://portswigger.net/research/gotta-cache-em-all>

## Prevent CSP bypasses

This section describes some points, to keep in mind, during the creation of a [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (called **CSP**) policy to prevent introducing bypasses.

🚩 Not every **[directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy#directives)** fallback to the **[default-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/default-src)** directive when it is not specified in the CSP policy.

## Directive form-action

👀 It is the case for the **[form-action](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/form-action)** directive. Therefore, an html form can be used to bypass the CSP in place when the `form-action` is not defined.

📺 This [demonstration video](assets/misc/demo_csp_bypass_due_to_no_form_action_directive.mp4) show an example.

💡 Therefore, ensure to always specify the `form-action` directive in a CSP policy to at least, the `'self'` value, to allow forms only on the current domain.

## Directive frame-ancestors

👀 It is the case for the **[frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors)** directive. Therefore, IF it is not defined **AND** IF the header [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) is not/incorrectly specified then the current domain can be embedded into a frame.

📺 This [demonstration video](assets/misc/demo_csp_bypass_due_to_no_frame_ancestors_directive.mp4) show an example.

💡 Therefore, ensure to always specify the `frame-ancestors` directive in a CSP policy to at least, the `'none'` value, to deny the current domain to be "framed".
