---
title: Compatibility
displaytext: Compatibility Matrix
layout: null
tab: true
order: 2
tags: headers
---

# Browser Support

| Feature                                      | Internet Explorer | Edge  | Firefox | Chrome | Safari | Opera | Android |
| ---------------------------------------------|-------------------|-------|---------|--------|--------|-------|---------|
| HTTP Strict Transport Security (HSTS)        | 11                | 13    | 47      | 49     | 9.1    | 39    | 4.4     |
| X-Frame-Options                              | 8                 | 13    | 47      | 49     | 9.1    | 39    | 4.4     |
| X-Content-Type-Options                       | 8                 | 12    | 50      | 64     | 11     | 73    | 81      |
| Content-Security-Policy                      | 11                | 13    | 47      | 49     | 9.1    | 39    | 4.4     |
| X-Permitted-Cross-Domain-Policies            |                   |       |         |        |        |       |         |
| Referrer-Policy                              | NS                | NS    | 50      | 56     | NS     | 43    |         |
| Feature-Policy                               | NS                | 79    | 74      | 60     | 11.1   | 47    | 81      |
| Public Key Pinning Extension for HTTP (HPKP) | NS                | NS    | 35-71   | 38-71  | NS     | 23-65 | NS      |
| Expect-CT                                    | NS                | 79    | NS      | 61     | NS     | 48    | NS      |
| X-XSS-Protection                             | 8                 | 12-16 | NS      | 4-77   | 13.1+  | 10-64 | NS      |
| Clear-Site-Data                              | NS                | 79    | 63      | 61     | NS     | 48    | 61      |
| Cross-Origin-Embedder-Policy (COEP)          | NS                | 83    | 79      | 83     | NS     | NS    | NS      |
| Cross-Origin-Opener-Policy (COOP)            | NS                | 83    | 79      | 83     | NS     | NS    | NS      |
| Cross-Origin-Resource-Policy (CORP)          | NS                | 79    | 74      | 73     | 12     | NS    | 73      |

_`NS` = Not Supported_  
_`+` = Specified version and above_

## References

* HTTP Strict Transport Security (HSTS)
  - <https://blogs.windows.com/msedgedev/2015/06/09/http-strict-transport-security-comes-to-internet-explorer-11-on-windows-8-1-and-windows-7/>
  - <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>
  - <https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html>
  - <https://caniuse.com/#search=HSTS>

* X-Frame-Options
  - <https://caniuse.com/#search=X-Frame-Options>

* X-Content-Type-Options
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options>
  - <https://caniuse.com/mdn-http_headers_x-content-type-options>

* Content-Security-Policy
  - <https://caniuse.com/#search=Content%20Security%20Policy>

* X-Permitted-Cross-Domain-Policies
  - <https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html>

* Referrer-Policy
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy>

* Feature-Policy
  - Note: Depends greatly on the specific attribute
  - <https://caniuse.com/#search=Feature-Policy>
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy>

* Public Key Pinning Extension for HTTP (HPKP)
  - <https://caniuse.com/#search=Public%20Key%20Pinning>
  - <https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ>
  - <https://www.chromestatus.com/feature/5903385005916160>

* Expect-CT
  - <https://www.chromestatus.com/feature/5677171733430272>
  - <https://caniuse.com/mdn-http_headers_expect-ct>

* X-XSS-Protection
  - <https://wiki.mozilla.org/Security/Features/XSS_Filter>
  - <https://blogs.msdn.microsoft.com/ieinternals/2011/01/31/controlling-the-xss-filter/>
  
* Clear-Site-Data 
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data#browser_compatibility>
  - <https://www.chromestatus.com/feature/4713262029471744>
  - <https://caniuse.com/?search=clear-site-data>

* Cross-Origin-Embedder-Policy (COEP)
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy#browser_compatibility>
  - <https://caniuse.com/?search=Cross-Origin-Embedder-Policy>

* Cross-Origin-Opener-Policy (COOP)
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy#browser_compatibility>
  - <https://caniuse.com/?search=Cross-Origin-Opener-Policy>

* Cross-Origin-Resource-Policy (CORP)
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Resource-Policy#browser_compatibility>
  - <https://caniuse.com/?search=Cross-Origin-Resource-Policy>
