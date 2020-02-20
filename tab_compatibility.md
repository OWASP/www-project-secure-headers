---
title: Compatibility
displaytext: Compatibility Matrix
layout: null
tab: true
order: 2
tags: headers
---

# Browser Support

Internet Explorer	Edge	Firefox	Chrome	Safari	Opera	Android
HTTP Strict Transport Security (HSTS)	11	13	47	49	9.1	39	4.4
Public Key Pinning Extension for HTTP (HPKP)	NS	NS	47	49	NS	39	51
X-Frame-Options	8	13	47	49	9.1	39	4.4
X-XSS-Protection	8		NS	4+			
X-Content-Type-Options	8		51	1.0	NS	13	
Content-Security-Policy	11	13	47	49	9.1	39	4.4
X-Permitted-Cross-Domain-Policies							
Referrer-Policy	NS	NS	50	56	NS	43	
Expect-CT				61		48	
Feature-Policy							
NS = Not Supported
+ = Specified version and above

## References

* HTTP Strict Transport Security (HSTS)
https://blogs.windows.com/msedgedev/2015/06/09/http-strict-transport-security-comes-to-internet-explorer-11-on-windows-8-1-and-windows-7/
https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet
http://caniuse.com/#search=HSTS
* Public Key Pinning Extension for HTTP (HPKP)
http://caniuse.com/#search=Public%20Key%20Pinning
https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ
* X-Frame-Options
http://caniuse.com/#search=X-Frame-Options
* X-XSS-Protection
https://wiki.mozilla.org/Security/Features/XSS_Filter
https://blogs.msdn.microsoft.com/ieinternals/2011/01/31/controlling-the-xss-filter/
* X-Content-Type-Options
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options
* Content-Security-Policy
http://caniuse.com/#search=Content%20Security%20Policy
* X-Permitted-Cross-Domain-Policies
https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html
* Referrer-Policy
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
* Expect-CT
https://www.chromestatus.com/feature/5677171733430272
* Feature-Policy
[update needed]
