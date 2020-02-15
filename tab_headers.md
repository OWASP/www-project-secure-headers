---
title: Response Headers
layout: null
tab: true
order: 1
tags: headers
---

## Response Headers

* HTTP Strict Transport Security (HSTS)
* Public Key Pinning Extension for HTTP (HPKP)
* X-Frame-Options
* X-XSS-Protection
* X-Content-Type-Options
* Content-Security-Policy
* X-Permitted-Cross-Domain-Policies
* Referrer-Policy
* Expect-CT
* Feature-Policy

## HTTP Strict Transport Security (HSTS)

HTTP Strict Transport Security (HSTS) is a web security policy mechanism which helps to protect websites against protocol downgrade attacks and cookie hijacking. It allows web servers to declare that web browsers (or other complying user agents) should only interact with it using secure HTTPS connections, and never via the insecure HTTP protocol. HSTS is an IETF standards track protocol and is specified in RFC 6797. A server implements an HSTS policy by supplying a header (Strict-Transport-Security) over an HTTPS connection (HSTS headers over HTTP are ignored).

Values
Value	Description
max-age=SECONDS	The time, in seconds, that the browser should remember that this site is only to be accessed using HTTPS.
includeSubDomains	If this optional parameter is specified, this rule applies to all of the site's subdomains as well.
Example
Strict-Transport-Security: max-age=31536000 ; includeSubDomains

### References

* https://tools.ietf.org/html/rfc6797
* https://www.owasp.org/index.php/HTTP_Strict_Transport_Security
* https://www.owasp.org/index.php/Test_HTTP_Strict_Transport_Security_(OTG-CONFIG-007)
* https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
* https://www.chromium.org/hsts
* https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security
* https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html

## Public Key Pinning Extension for HTTP (HPKP)

HTTP Public Key Pinning (HPKP) is a security mechanism which allows HTTPS websites to resist impersonation by attackers using mis-issued or otherwise fraudulent certificates. (For example, sometimes attackers can compromise certificate authorities, and then can mis-issue certificates for a web origin.).

The HTTPS web server serves a list of public key hashes, and on subsequent connections clients expect that server to use one or more of those public keys in its certificate chain. Deploying HPKP safely will require operational and organizational maturity due to the risk that hosts may make themselves unavailable by pinning to a set of public key hashes that becomes invalid. With care, host operators can greatly reduce the risk of man-in-the-middle (MITM) attacks and other false authentication problems for their users without incurring undue risk.

Before implement HPKP please read this https://www.chromestatus.com/feature/5903385005916160.

Values
Value	Description
pin-sha256="<sha256>"	The quoted string is the Base64 encoded Subject Public Key Information (SPKI) fingerprint. It is possible to specify multiple pins for different public keys. Some browsers might allow other hashing algorithms than SHA-256 in the future.
max-age=SECONDS	The time, in seconds, that the browser should remember that this site is only to be accessed using one of the pinned keys.
includeSubDomains	If this optional parameter is specified, this rule applies to all of the site's subdomains as well.
report-uri="<URL>"	If this optional parameter is specified, pin validation failures are reported to the given URL.
Example
Public-Key-Pins: pin-sha256="d6qzRu9zOECb90Uez27xWltNsj0e1Md7GkYYkVoZWmM="; pin-sha256="E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g="; report-uri="http://example.com/pkp-report"; max-age=10000; includeSubDomains

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

## X-Frame-Options

X-Frame-Options response header improve the protection of web applications against Clickjacking. It declares a policy communicated from a host to the client browser on whether the browser must not display the transmitted content in frames of other web pages.

Values
Value	Description
deny	No rendering within a frame.
sameorigin	No rendering if origin mismatch.
allow-from: DOMAIN	Allows rendering if framed by frame loaded from DOMAIN.
Example
X-Frame-Options: deny

### References

* https://tools.ietf.org/html/rfc7034
* https://tools.ietf.org/html/draft-ietf-websec-x-frame-options-01
* https://tools.ietf.org/html/draft-ietf-websec-frame-options-00
* https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options
* https://www.owasp.org/index.php/Clickjacking
* https://blogs.msdn.microsoft.com/ieinternals/2010/03/30/combating-clickjacking-with-x-frame-options/

## X-XSS-Protection

This header enables the Cross-site scripting (XSS) filter in your browser.

Values
Value	Description
0	Filter disabled.
1	Filter enabled. If a cross-site scripting attack is detected, in order to stop the attack, the browser will sanitize the page.
1; mode=block	Filter enabled. Rather than sanitize the page, when a XSS attack is detected, the browser will prevent rendering of the page.
1; report=http://[YOURDOMAIN]/your_report_URI	Filter enabled. The browser will sanitize the page and report the violation. This is a Chromium function utilizing CSP violation reports to send details to a URI of your choice.
Example
X-XSS-Protection: 1; mode=block

### References

* https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)
* https://www.virtuesecurity.com/blog/understanding-xss-auditor/
* https://www.veracode.com/blog/2014/03/guidelines-for-setting-security-headers
* http://zinoui.com/blog/security-http-headers#x-xss-protection

## X-Content-Type-Options

Setting this header will prevent the browser from interpreting files as something else than declared by the content type in the HTTP headers.

Values
Value	Description
nosniff	Will prevent the browser from MIME-sniffing a response away from the declared content-type.
Example
X-Content-Type-Options: nosniff

### References

* https://msdn.microsoft.com/en-us/library/gg622941%28v=vs.85%29.aspx
* https://blogs.msdn.microsoft.com/ie/2008/09/02/ie8-security-part-vi-beta-2-update/

## Content-Security-Policy

A Content Security Policy (CSP) requires careful tuning and precise definition of the policy. If enabled, CSP has significant impact on the way browsers render pages (e.g., inline JavaScript disabled by default and must be explicitly allowed in policy). CSP prevents a wide range of attacks, including Cross-site scripting and other cross-site injections.

Values
Directive	Description
base-uri	Define the base uri for relative uri.
default-src	Define loading policy for all resources type in case of a resource type dedicated directive is not defined (fallback).
script-src	Define which scripts the protected resource can execute.
object-src	Define from where the protected resource can load plugins.
style-src	Define which styles (CSS) the user applies to the protected resource.
img-src	Define from where the protected resource can load images.
media-src	Define from where the protected resource can load video and audio.
frame-src	Deprecated and replaced by child-src. Define from where the protected resource can embed frames.
child-src	Define from where the protected resource can embed frames.
frame-ancestors	Define from where the protected resource can be embedded in frames.
font-src	Define from where the protected resource can load fonts.
connect-src	Define which URIs the protected resource can load using script interfaces.
manifest-src	Define from where the protected resource can load manifest.
form-action	Define which URIs can be used as the action of HTML form elements.
sandbox	Specifies an HTML sandbox policy that the user agent applies to the protected resource.
script-nonce	Define script execution by requiring the presence of the specified nonce on script elements.
plugin-types	Define the set of plugins that can be invoked by the protected resource by limiting the types of resources that can be embedded.
reflected-xss	Instructs a user agent to activate or deactivate any heuristics used to filter or block reflected cross-site scripting attacks, equivalent to the effects of the non-standard X-XSS-Protection header.
block-all-mixed-content	Prevent user agent from loading mixed content.
upgrade-insecure-requests	Instructs user agent to download insecure resources using HTTPS.
referrer	Define information user agent must send in Referer header.
report-uri	Specifies a URI to which the user agent sends reports about policy violation.
report-to	Specifies a group (defined in Report-To header) to which the user agent sends reports about policy violation.
Example
Content-Security-Policy: script-src 'self'

### References

* https://www.w3.org/TR/CSP/
* https://developer.mozilla.org/en-US/docs/Web/Security/CSP
* https://www.owasp.org/index.php/Content_Security_Policy
* https://scotthelme.co.uk/content-security-policy-an-introduction/
* https://report-uri.io
* http://www.cspplayground.com/home
* http://content-security-policy.com

## X-Permitted-Cross-Domain-Policies

A cross-domain policy file is an XML document that grants a web client, such as Adobe Flash Player or Adobe Acrobat (though not necessarily limited to these), permission to handle data across domains. When clients request content hosted on a particular source domain and that content make requests directed towards a domain other than its own, the remote domain needs to host a cross-domain policy file that grants access to the source domain, allowing the client to continue the transaction. Normally a meta-policy is declared in the master policy file, but for those who can’t write to the root directory, they can also declare a meta-policy using the X-Permitted-Cross-Domain-Policies HTTP response header.

Values
Value	Description
none	No policy files are allowed anywhere on the target server, including this master policy file.
master-only	Only this master policy file is allowed.
by-content-type	[HTTP/HTTPS only] Only policy files served with Content-Type: text/x-cross-domain-policy are allowed.
by-ftp-filename	[FTP only] Only policy files whose file names are crossdomain.xml (i.e. URLs ending in /crossdomain.xml) are allowed.
all	All policy files on this target domain are allowed.
Example
X-Permitted-Cross-Domain-Policies: none

### References

* https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html
* https://www.adobe.com/devnet/adobe-media-server/articles/cross-domain-xml-for-streaming.html
* https://www.perpetual-beta.org/weblog/security-headers.html#rule-8470-2-establish-a-cross-domain-meta-policy
* https://danielnixon.org/http-security-headers/
* https://rorsecurity.info/portfolio/new-http-headers-for-more-security
* https://github.com/twitter/secureheaders/issues/88

## Referrer-Policy

The Referrer-Policy HTTP header governs which referrer information, sent in the Referer header, should be included with requests made.

Values
Value	Description
no-referrer	The Referer header will be omitted entirely. No referrer information is sent along with requests.
no-referrer-when-downgrade	This is the user agent's default behavior if no policy is specified. The origin is sent as referrer to a-priori as-much-secure destination (HTTPS->HTTPS), but isn't sent to a less secure destination (HTTPS->HTTP).
origin	Only send the origin of the document as the referrer in all cases. The document https://example.com/page.html will send the referrer https://example.com/.
origin-when-cross-origin	Send a full URL when performing a same-origin request, but only send the origin of the document for other cases.
same-origin	A referrer will be sent for same-site origins, but cross-origin requests will contain no referrer information.
strict-origin	Only send the origin of the document as the referrer to a-priori as-much-secure destination (HTTPS->HTTPS), but don't send it to a less secure destination (HTTPS->HTTP).
strict-origin-when-cross-origin	Send a full URL when performing a same-origin request, only send the origin of the document to a-priori as-much-secure destination (HTTPS->HTTPS), and send no header to a less secure destination (HTTPS->HTTP).
unsafe-url	Send a full URL (stripped from parameters) when performing a a same-origin or cross-origin request.
Example
Referrer-Policy: no-referrer

### References

* https://www.w3.org/TR/referrer-policy/
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy

## Expect-CT

The Expect-CT header is used by a server to indicate that browsers should evaluate connections to the host emitting the header for Certificate Transparency compliance.

Values
Value	Description
report-uri	The optional report-uri directive indicates the URL to which the browser should report Expect-CT failures.
enforce	The optional enforce directive is a valueless directive that, if present, signals to the browser that compliance to the CT Policy should be enforced (rather than report-only) and that the browser should refuse future connections that violate its CT Policy. When both the enforce directive and report-uri directive are present, the configuration is referred to as an "enforce-and-report" configuration, signalling to the browser both that compliance to the CT Policy should be enforced and that violations should be reported.
max-age	The max-age directive specifies the number of seconds after the reception of the Expect-CT header field during which the browser should regard the host from whom the message was received as a Known Expect-CT Host.
Example
Expect-CT: max-age=86400, enforce, report-uri="https://foo.example/report"

### References

* https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct-02
* http://httpwg.org/http-extensions/expect-ct.html
* https://scotthelme.co.uk/a-new-security-header-expect-ct/

## Feature-Policy

The Feature-Policy header allows developers to selectively enable and disable use of various browser features and APIs..

Values
Value	Description
accelerometer	Controls access to accelerometer sensors on the device.
ambient-light-sensor	Controls access to ambient light sensors on the device.
autoplay	Controls access to autoplay through play() and autoplay.
camera	Controls access to video input devices.
encrypted-media	Controls whether requestMediaKeySystemAccess() is allowed.
fullscreen	Controls whether requestFullscreen() is allowed.
geolocation	Controls access to Geolocation interface.
gyroscope	Controls access to gyroscope sensors on the device.
magnetometer	Controls access to magnetometer sensors on the device.
microphone	Controls access to audio input devices.
midi	Controls access to requestMIDIAccess() method.
payment	Controls access to PaymentRequest interface.
picture-in-picture	Controls access to Picture in Picture.
speaker	Controls access to audio output devices.
usb	Controls access to USB devices.
vibrate	Controls access to vibrate() method.
vr	Controls access to VR displays.
Example
Feature-Policy: vibrate 'none'; geolocation 'none'

### References

* https://wicg.github.io/feature-policy/
* https://github.com/WICG/feature-policy/blob/master/features.md
* https://scotthelme.co.uk/a-new-security-header-feature-policy/
