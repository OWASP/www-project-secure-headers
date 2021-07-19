---
title: misc
displaytext: Miscellaneous
layout: null
tab: true
order: 6
tags: headers
---

# Miscellaneous

This section provide extra useful information about HTTP Security headers.

## Request headers

### Fetch metadata request header

A fetch metadata request header is an HTTP request header that provides additional information about the context from which the request originated. This allows the server to make decisions about whether a request should be allowed based on where the request came from and how the resource will be used .

These headers are prefixed with `Sec-`, and hence have [forbidden header names](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_header_name). As such, they *cannot be modified from JavaScript*.

Source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Glossary/Fetch_metadata_request_header).

These headers can be leveraged to add protection measures against [XS-Leaks](https://xsleaks.dev/docs/defenses/opt-in/fetch-metadata/) attacks.

#### Sec-Fetch-Dest

The `Sec-Fetch-Dest` fetch metadata request header indicates the request's destination. That is the initiator of the original fetch request, which is where (and how) the fetched data will be used.

Possible values are detailled [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest#directives).

Source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest).

#### Sec-Fetch-Mode

The `Sec-Fetch-Mode` fetch metadata request header indicates the [mode](https://developer.mozilla.org/en-US/docs/Web/API/Request/mode) of the request: **cors**, **no-cors**, **same-origin**, **navigate** or **websocket**.

Broadly speaking, this allows a server to distinguish between: requests originating from a user navigating between HTML pages, and requests to load images and other resources.

Possible values are detailled [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode#directives).

Source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode).

#### Sec-Fetch-User

The `Sec-Fetch-User` fetch metadata request header *is only sent for requests initiated by user activation*, and its value will always be `?1`.

Source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-User).

#### Sec-Fetch-Site

The `Sec-Fetch-Site` fetch metadata request header indicates the relationship between a request initiator's origin and the origin of the requested resource.

In other words, this header tells a server whether a request for a resource is coming from the same origin, the same site, a different site, or is a "user initiated" request. The server can then use this information to decide if the request should be allowed.

Possible values are detailled [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site#directives).

Source [Mozilla MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site).

Explanation about **Site** vs **Origin** can found [here](https://web.dev/same-site-same-origin/).

#### Example

```
GET /www-project-secure-headers/
Host: owasp.org
User-Agent: Chrome/91.0.4472.124
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: cross-site
Sec-Fetch-User: ?1
```

#### References

* <https://developer.mozilla.org/en-US/docs/Glossary/Fetch_metadata_request_header>
* <https://caniuse.com/mdn-http_headers_sec-fetch-dest>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Dest>
* <https://caniuse.com/mdn-http_headers_sec-fetch-mode>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Mode>
* <https://caniuse.com/mdn-http_headers_sec-fetch-user>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-User>
* <https://caniuse.com/mdn-http_headers_sec-fetch-site>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Sec-Fetch-Site>
* <https://web.dev/same-site-same-origin/>
* <https://jub0bs.com/posts/2021-01-29-great-samesite-confusion/#are-site-and-origin-interchangeable>
* <https://portswigger.net/daily-swig/firefox-becomes-latest-browser-to-support-fetch-metadata-request-headers>
* <https://xsleaks.dev/docs/defenses/opt-in/fetch-metadata/>
