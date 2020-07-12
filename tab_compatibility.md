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
| X-Content-Type-Options                       | 8                 |       | 51      | 1.0    | NS     | 13    |         |
| Content-Security-Policy                      | 11                | 13    | 47      | 49     | 9.1    | 39    | 4.4     |
| X-Permitted-Cross-Domain-Policies            |                   |       |         |        |        |       |         |
| Referrer-Policy                              | NS                | NS    | 50      | 56     | NS     | 43    |         | 
| Feature-Policy                               | NS                | 79    | 74      | 60     | 11.1   | 47    | 81      | 
| Public Key Pinning Extension for HTTP (HPKP) | NS                | NS    | 35-71   | 38-71  | NS     | 23-65 | NS      |
| Expect-CT                                    |                   |       |         | 61     |        | 48    |         | 
| X-XSS-Protection                             | 8                 | 12-16 | NS      | 4-77   | 13.1+  | 10-64 | NS      |

_`NS` = Not Supported_  
_`+` = Specified version and above_

## References

* HTTP Strict Transport Security (HSTS)
  - https://blogs.windows.com/msedgedev/2015/06/09/http-strict-transport-security-comes-to-internet-explorer-11-on-windows-8-1-and-windows-7/
  - https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
  - https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet
  - http://caniuse.com/#search=HSTS

* X-Frame-Options
  - http://caniuse.com/#search=X-Frame-Options

* X-Content-Type-Options
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options

* Content-Security-Policy
  - http://caniuse.com/#search=Content%20Security%20Policy

* X-Permitted-Cross-Domain-Policies
  - https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html

* Referrer-Policy
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy

* Feature-Policy
  - Note: Depends greatly on the specific attribute
  - https://caniuse.com/#search=Feature-Policy
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy

* Public Key Pinning Extension for HTTP (HPKP)
  - http://caniuse.com/#search=Public%20Key%20Pinning
  - https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ
  - https://www.chromestatus.com/feature/5903385005916160

* Expect-CT
  - https://www.chromestatus.com/feature/5677171733430272

* X-XSS-Protection
  - https://wiki.mozilla.org/Security/Features/XSS_Filter
  - https://blogs.msdn.microsoft.com/ieinternals/2011/01/31/controlling-the-xss-filter/
