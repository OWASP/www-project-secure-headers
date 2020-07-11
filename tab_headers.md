---
title: headers
displaytext: Response Headers
layout: null
tab: true
order: 1
tags: headers
---

# Response Headers

* HTTP Strict Transport Security (HSTS)
* X-Frame-Options
* X-XSS-Protection
* X-Content-Type-Options
* Content-Security-Policy
* X-Permitted-Cross-Domain-Policies
* Referrer-Policy
* Feature-Policy
* Public Key Pinning Extension for HTTP (HPKP)
* Expect-CT

## HTTP Strict Transport Security (HSTS)

HTTP Strict Transport Security (HSTS) is a web security policy mechanism which helps to protect websites against protocol downgrade attacks and cookie hijacking. It allows web servers to declare that web browsers (or other complying user agents) should only interact with it using secure HTTPS connections, and never via the insecure HTTP protocol. HSTS is an IETF standards track protocol and is specified in RFC 6797. A server implements an HSTS policy by supplying a header (`Strict-Transport-Security`) over an HTTPS connection (HSTS headers over HTTP are ignored).

### Values

| Value               | Description |
|---------------------|-------------|
| `max-age=SECONDS`   | The time, in seconds, that the browser should remember that this site is only to be accessed using HTTPS. |
| `includeSubDomains` | If this optional parameter is specified, this rule applies to all of the site's subdomains as well. |

### Example

```
Strict-Transport-Security: max-age=31536000 ; includeSubDomains
```

### References

* https://tools.ietf.org/html/rfc6797
* https://www.owasp.org/index.php/HTTP_Strict_Transport_Security
* https://www.owasp.org/index.php/Test_HTTP_Strict_Transport_Security_(OTG-CONFIG-007)
* https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
* https://www.chromium.org/hsts
* https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security
* https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html

## X-Frame-Options

The `X-Frame-Options` response header improves the protection of web applications against clickjacking. It instructs the browser whether the content can be displayed within frames.
The CSP frame-ancestors directive obsoletes the X-Frame-Options header. If a resource has both policies, the CSP frame-ancestors policy will be enforced and the X-Frame-Options policy will be ignored.

### Values

| Value                | Description |
|----------------------|-------------|
| `deny`               | No rendering within a frame. |
| `sameorigin`         | No rendering if origin mismatch. |
| `allow-from: DOMAIN` | Allows rendering if framed by frame loaded from DOMAIN. |

### Example

```
X-Frame-Options: deny
```

### References

* https://tools.ietf.org/html/rfc7034
* https://tools.ietf.org/html/draft-ietf-websec-x-frame-options-01
* https://tools.ietf.org/html/draft-ietf-websec-frame-options-00
* https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options
* https://www.owasp.org/index.php/Clickjacking
* https://blogs.msdn.microsoft.com/ieinternals/2010/03/30/combating-clickjacking-with-x-frame-options/

## X-XSS-Protection

This header enables the cross-site scripting (XSS) filter in your browser.

The X-XSS-Protection header has been deprecated by modern browsers and its use can introduce additional security issues on the client side. As such, it is recommended to set the header as `X-XSS-Protection: 0` in order to disable the XSS Auditor, and not allow it to take the default behavior of the browser handling the response.

### Values

| Value                                           | Description |
|-------------------------------------------------|-------------|
| `0`                                             | Filter disabled. |
| `1`                                             | Filter enabled. If a cross-site scripting attack is detected, in order to stop the attack, the browser will sanitize the page. |
| `1; mode=block`                                 | Filter enabled. Rather than sanitize the page, when a XSS attack is detected, the browser will prevent rendering of the page. |
| `1; report=http://[YOURDOMAIN]/your_report_URI` | Filter enabled. The browser will sanitize the page and report the violation. This is a Chromium function utilizing CSP violation reports to send details to a URI of your choice. |

### Example

```
X-XSS-Protection: 0
```

### References

* https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
* https://www.chromestatus.com/feature/5021976655560704
* https://bugzilla.mozilla.org/show_bug.cgi?id=528661
* https://blogs.windows.com/windowsexperience/2018/07/25/announcing-windows-10-insider-preview-build-17723-and-build-18204/
* https://github.com/zaproxy/zaproxy/issues/5849
* https://scotthelme.co.uk/security-headers-updates/#removing-the-x-xss-protection-header
* https://portswigger.net/daily-swig/google-chromes-xss-auditor-goes-back-to-filter-mode
* https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)
* https://www.virtuesecurity.com/blog/understanding-xss-auditor/
* https://www.veracode.com/blog/2014/03/guidelines-for-setting-security-headers
* http://zinoui.com/blog/security-http-headers#x-xss-protection

## X-Content-Type-Options

Setting this header will prevent the browser from interpreting files as a different MIME type to what is specified in the `Content-Type` HTTP header (e.g. treating `text/plain` as `text/css`).

### Values

| Value     | Description |
|-----------|-------------|
| `nosniff` | Will prevent the browser from MIME-sniffing a response away from the declared content-type. |

### Example

```
X-Content-Type-Options: nosniff
```

### References

* https://msdn.microsoft.com/en-us/library/gg622941%28v=vs.85%29.aspx
* https://blogs.msdn.microsoft.com/ie/2008/09/02/ie8-security-part-vi-beta-2-update/

## Content-Security-Policy

A Content Security Policy (CSP) requires careful tuning and precise definition of the policy. If enabled, CSP has significant impact on the way browsers render pages (e.g., inline JavaScript is disabled by default and must be explicitly allowed in the policy). CSP prevents a wide range of attacks, including cross-site scripting and other cross-site injections.

### Values

| Directive                   | Description |
|-----------------------------|-------------|
| `base-uri`                  | Define the base URI for relative URIs. |
| `default-src`               | Define loading policy for all resources type in case a resource type's dedicated directive is not defined (fallback). |
| `script-src`                | Define which scripts the protected resource can execute. |
| `object-src`                | Define from where the protected resource can load plugins. |
| `style-src`                 | Define which styles (CSS) can be applied to the protected resource. |
| `img-src`                   | Define from where the protected resource can load images. |
| `media-src`                 | Define from where the protected resource can load video and audio. |
| `frame-src`                 | _(Deprecated and replaced by `child-src`)_ Define from where the protected resource can embed frames. |
| `child-src`                 | Define from where the protected resource can embed frames. |
| `frame-ancestors`           | Define from where the protected resource can be embedded in frames. |
| `font-src`                  | Define from where the protected resource can load fonts. |
| `connect-src`               | Define which URIs the protected resource can load using script interfaces. |
| `manifest-src`              | Define from where the protected resource can load manifests. |
| `form-action`               | Define which URIs can be used as the action of HTML form elements. |
| `sandbox`                   | Specifies an HTML sandbox policy that the user agent applies to the protected resource. |
| `script-nonce`              | Define script execution by requiring the presence of the specified nonce on script elements. |
| `plugin-types`              | Define the set of plugins that can be invoked by the protected resource by limiting the types of resources that can be embedded. |
| `reflected-xss`             | Instruct the user agent to activate or deactivate any heuristics used to filter or block reflected cross-site scripting attacks, equivalent to the effects of the non-standard `X-XSS-Protection` header. |
| `block-all-mixed-content`   | Prevent the user agent from loading mixed content. |
| `upgrade-insecure-requests` | Instruct the user agent to download insecure HTTP resources using HTTPS. |
| `referrer`                  | _(Deprecated)_ Define information the user agent can send in the `Referer` header. |
| `report-uri`                | _(Deprecated and replaced by `report-to`)_ Specifies a URI to which the user agent sends reports about policy violation. |
| `report-to`                 | Specifies a group (defined in the `Report-To` header) to which the user agent sends reports about policy violation. |

### Example

```
Content-Security-Policy: script-src 'self'
```

### References

* https://www.w3.org/TR/CSP/
* https://developer.mozilla.org/en-US/docs/Web/Security/CSP
* https://www.owasp.org/index.php/Content_Security_Policy
* https://scotthelme.co.uk/content-security-policy-an-introduction/
* https://report-uri.io
* http://www.cspplayground.com/home
* http://content-security-policy.com

## X-Permitted-Cross-Domain-Policies

A cross-domain policy file is an XML document that grants a web client, such as Adobe Flash Player or Adobe Acrobat (though not necessarily limited to these), permission to handle data across domains. When clients request content hosted on a particular source domain and that content makes requests directed towards a domain other than its own, the remote domain needs to host a cross-domain policy file that grants access to the source domain, allowing the client to continue the transaction. Normally a meta-policy is declared in the master policy file, but for those who can’t write to the root directory, they can also declare a meta-policy using the `X-Permitted-Cross-Domain-Policies` HTTP response header.

### Values

| Value             | Description |
|-------------------|-------------|
| `none`            | No policy files are allowed anywhere on the target server, including this master policy file. |
| `master-only`     | Only this master policy file is allowed. |
| `by-content-type` | [HTTP/HTTPS only] Only policy files served with Content-Type: text/x-cross-domain-policy are allowed. |
| `by-ftp-filename` | [FTP only] Only policy files whose file names are crossdomain.xml (i.e. URLs ending in /crossdomain.xml) are allowed. |
| `all`             | All policy files on this target domain are allowed. |

### Example

```
X-Permitted-Cross-Domain-Policies: none
```

### References

* https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html
* https://www.adobe.com/devnet/adobe-media-server/articles/cross-domain-xml-for-streaming.html
* https://www.perpetual-beta.org/weblog/security-headers.html#rule-8470-2-establish-a-cross-domain-meta-policy
* https://danielnixon.org/http-security-headers/
* https://rorsecurity.info/portfolio/new-http-headers-for-more-security
* https://github.com/twitter/secureheaders/issues/88

## Referrer-Policy

The `Referrer-Policy` HTTP header governs which referrer information, sent in the `Referer` header, should be included with requests made.

### Values

| Value                             | Description |
|-----------------------------------|-------------|
| `no-referrer`                     | The `Referer` header will be omitted entirely. No referrer information is sent along with requests. |
| `no-referrer-when-downgrade`      | This is the user agent's default behavior if no policy is specified. The origin is sent as referrer to a-priori as-much-secure destination (HTTPS → HTTPS), but isn't sent to a less secure destination (HTTPS → HTTP). |
| `origin`                          | Only send the origin of the document as the referrer in all cases. (e.g. the document `https://example.com/page.html` will send the referrer `https://example.com/`.) |
| `origin-when-cross-origin`        | Send a full URL when performing a same-origin request, but only send the origin of the document for other cases. |
| `same-origin`                     | A referrer will be sent for same-site origins, but cross-origin requests will contain no referrer information. |
| `strict-origin`                   | Only send the origin of the document as the referrer to a-priori as-much-secure destination (HTTPS → HTTPS), but don't send it to a less secure destination (HTTPS → HTTP). |
| `strict-origin-when-cross-origin` | Send a full URL when performing a same-origin request, only send the origin of the document to a-priori as-much-secure destination (HTTPS → HTTPS), and send no header to a less secure destination (HTTPS → HTTP). |
| `unsafe-url`                      | Send a full URL (stripped from parameters) when performing a a same-origin or cross-origin request. |

### Example

```
Referrer-Policy: no-referrer
```

### References

* https://www.w3.org/TR/referrer-policy/
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy

## Feature-Policy

The Feature-Policy header allows developers to selectively enable and disable use of various browser features and APIs..

### Values

| Value                  | Description |
|------------------------|-------------|
| `accelerometer`        | Controls access to accelerometer sensors on the device. |
| `ambient-light-sensor` | Controls access to ambient light sensors on the device. |
| `autoplay`             | Controls access to autoplay through `play()` and the `autoplay` attribute. |
| `camera`               | Controls access to video input devices. |
| `encrypted-media`      | Controls whether `requestMediaKeySystemAccess()` is allowed. |
| `fullscreen`           | Controls whether `requestFullscreen()` is allowed. |
| `geolocation`          | Controls access to the `Geolocation` interface. |
| `gyroscope`            | Controls access to gyroscope sensors on the device. |
| `magnetometer`         | Controls access to magnetometer sensors on the device. |
| `microphone`           | Controls access to audio input devices. |
| `midi`                 | Controls access to `requestMIDIAccess()` method. |
| `payment`              | Controls access to the `PaymentRequest` interface. |
| `picture-in-picture`   | Controls access to picture-in-picture. |
| `speaker`              | Controls access to audio output devices. |
| `usb`                  | Controls access to USB devices. |
| `vibrate`              | Controls access to the `vibrate()` method. |
| `vr`                   | Controls access to VR displays. |

### Example

```
Feature-Policy: vibrate 'none'; geolocation 'none'
```

### References

* https://wicg.github.io/feature-policy/
* https://github.com/WICG/feature-policy/blob/master/features.md
* https://scotthelme.co.uk/a-new-security-header-feature-policy/

## Public Key Pinning Extension for HTTP (HPKP)

> **Warning:** This header has been deprecated by all major browsers and is no longer recommended. **Avoid using it**, and update existing code if possible;

HTTP Public Key Pinning (HPKP) is a security mechanism which allows HTTPS websites to resist impersonation by attackers using mis-issued or otherwise fraudulent certificates. (For example, sometimes attackers can compromise certificate authorities, and then can mis-issue certificates for a web origin.).

The HTTPS web server serves a list of public key hashes, and on subsequent connections clients expect that server to use one or more of those public keys in its certificate chain. Deploying HPKP safely will require operational and organizational maturity due to the risk that hosts may make themselves unavailable by pinning to a set of public key hashes that becomes invalid. With care, host operators can greatly reduce the risk of man-in-the-middle (MITM) attacks and other false authentication problems for their users without incurring undue risk.

### Deprecation Reason

Criticism and concern revolved around malicious or human error scenarios known as [HPKP Suicide and Ransom PKP](https://scotthelme.co.uk/using-security-features-to-do-bad-things/). In such scenarios, a website owner would have their ability to publish new contents to their domain severely hampered by either losing access to their own keys or having new keys announced by a malicious attacker.

### Values

| Value                   | Description |
|-------------------------|-------------|
| `pin-sha256="<sha256>"` | The quoted string is the Base64 encoded Subject Public Key Information (SPKI) fingerprint. It is possible to specify multiple pins for different public keys. Some browsers might allow other hashing algorithms than SHA-256 in the future. |
| `max-age=SECONDS`       | The time, in seconds, that the browser should remember that this site is only to be accessed using one of the pinned keys. |
| `includeSubDomains`     | If this optional parameter is specified, this rule applies to all of the site's subdomains as well. |
| `report-uri="<URL>"`    | If this optional parameter is specified, pin validation failures are reported to the given URL. |

### Example

```
Public-Key-Pins: pin-sha256="d6qzRu9zOECb90Uez27xWltNsj0e1Md7GkYYkVoZWmM="; pin-sha256="E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g="; report-uri="http://example.com/pkp-report"; max-age=10000; includeSubDomains
```

### References

* https://tools.ietf.org/html/rfc7469
* https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning#HTTP_pinning
* https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning
* https://developer.mozilla.org/en-US/docs/Web/Security/Public_Key_Pinning
* https://raymii.org/s/articles/HTTP_Public_Key_Pinning_Extension_HPKP.html
* https://labs.detectify.com/2016/07/05/what-hpkp-is-but-isnt/
* https://blog.qualys.com/ssllabs/2016/09/06/is-http-public-key-pinning-dead
* https://scotthelme.co.uk/im-giving-up-on-hpkp/
* https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ

## Expect-CT

> **Note:** This header will likely become obsolete in June 2021. Since May 2018 new certificates are expected to support SCTs by default. Certificates before March 2018 were allowed to have a lifetime of 39 months, those will all be expired in June 2021.

The `Expect-CT` header is used by a server to indicate that browsers should evaluate connections to the host for Certificate Transparency compliance.  
In Chrome 61 (Aug 2017) Chrome enabled its enforcement via SCT by default ([source](https://www.chromestatus.com/feature/5677171733430272)). You can still use this header to specify an `report-uri`.  
  
This header comes from the (now expired) internet draft [Expect-CT Extension for HTTP](https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct-08).

### Values

| Value         | Description |
|---------------|-------------|
| `report-uri`  | _(Optional)_ Indicates the URL to which the browser should report Expect-CT failures. |
| `enforce`     | _(Optional)_ A valueless directive that, if present, signals to the browser that compliance to the CT Policy should be enforced (rather than report-only) and that the browser should refuse future connections that violate its CT Policy. When both the `enforce` and `report-uri` directives are present, the configuration is referred to as an "enforce-and-report" configuration, signalling to the browser both that compliance to the CT Policy should be enforced and that violations should be reported. |
| `max-age`     | Specifies the number of seconds after the response is received the browser should remember and enforce certificate transparency compliance. |

### Example

```
Expect-CT: max-age=86400, enforce, report-uri="https://foo.example/report"
```

### References

* https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct-02
* http://httpwg.org/http-extensions/expect-ct.html
* https://scotthelme.co.uk/a-new-security-header-expect-ct/
