---

layout: col-sidebar
title: OWASP secure headers
tags: example-tag
level: 0
type: code

auto-migrated: 1
---

This is an example of a Project or Chapter Page.
# Main

![Incubator_banner.jpg](Incubator_banner.jpg "Incubator_banner.jpg")

<table>
<tbody>
<tr class="odd">
<td><h2 id="owasp_secure_headers_project">OWASP Secure Headers Project</h2>
<p>The OWASP Secure Headers Project describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.</p>
<p>The OWASP Secure Headers Project describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.</p>
<h2 id="introduction">Introduction</h2>
<h2 id="introduction">Introduction</h2>
<p>HTTP headers are well known and also despised. Seeking the balance between usability and security developers implement functionality through the headers that can make your more versatile or secure application. But in practice how the headers are being implemented? What sites follow the best implementation practices? Big companies, small, all or none?</p>
<p>HTTP headers are well known and also despised. Seeking the balance between usability and security developers implement functionality through the headers that can make your more versatile or secure application. But in practice how the headers are being implemented? What sites follow the best implementation practices? Big companies, small, all or none?</p>
<h2 id="description">Description</h2>
<h2 id="description">Description</h2>
<p>We aim to publish reports on header usage stats, developments and changes. Code libraries that make these headers easily accessible to developers on a range of platforms. Data sets concerning the general usage of these headers.</p>
<p>We aim to publish reports on header usage stats, developments and changes. Code libraries that make these headers easily accessible to developers on a range of platforms. Data sets concerning the general usage of these headers.</p>
<h2 id="licensing">Licensing</h2>
<h2 id="licensing">Licensing</h2>
<p>OWASP Secure Headers is free to use. It is licensed under the <a href="https://github.com/oshp/headers/blob/master/LICENSE">Apache 2.0 License</a>.</p></td>
<p>OWASP Secure Headers is free to use. It is licensed under the <a href="https://github.com/oshp/headers/blob/master/LICENSE">Apache 2.0 License</a>.</p></td>
<p><a href="User:Riramar" title="wikilink">Ricardo Iramar</a><br />
<a href="User:Amenezes" title="wikilink">Alexandre Menezes</a></p>
<h2 id="project_contributors">Project Contributors</h2>
<p><a href="User:Jmanico" title="wikilink">Jim Manico</a><br />
</p>
<h2 id="related_projects">Related Projects</h2>
<ul>
<li><a href="OWASP_Application_Security_Verification_Standard_Project" title="wikilink">OWASP Application Security Verification Standard Project</a></li>
<li><a href="OWASP_Top_Ten_Project" title="wikilink">OWASP Top Ten Project</a></li>
</ul>
<h2 id="quick_links">Quick Links</h2>
<ul>
<li><a href="https://github.com/oshp/">Project GitHub Organization</a></li>
<li><a href="https://hub.docker.com/r/oshp/">Docker Hub Organization</a></li>
<li><a href="http://oshp.bsecteam.com">Demo [develop preview</a>]</li>
<li><a href="https://github.com/riramar/hsecscan">hsecscan A security scanner for HTTP response headers</a></li>
<li><a href="https://lists.owasp.org/mailman/listinfo/owasp_secure_headers_project">Project Email List</a></li>
</ul></td>
<ul>
<li>[23 Jul 2018] Included Feature-Policy header</li>
<li>[20 Oct 2017] OWASP Secure Headers Project on <a href="https://github.com/OWASP/Top10/blob/master/2017/OWASP%20Top%2010%202017%20RC2%20Final.pdf">| OWASP Top 10 RC2</a></li>
<li>[14 Mar 2017] <a href="https://hub.docker.com/r/oshp">| Docker Hub Organization</a></li>
<li>[15 Oct 2016] <a href="http://roadsec.com.br/curitiba2016/">| RoadSec Curitiba 2016 Presentation</a></li>
<li>[20/21 Set 2016] <a href="http://mindthesec.com.br/ricardo-iramar-dos-santos">| Mind The Sec 2016 Presentation</a></li>
<li>[05 Sep 2016] <a href="https://github.com/oshp/">| Project Github Organization</a></li>
<li>[01 Sep 2016] Included X-Permitted-Cross-Domain-Policies header</li>
<li>[14 Dec 2015] Reborn from the ashes</li>
</ul>
<h2 id="classifications">Classifications</h2>
<table>
<tbody>
<tr class="odd">
<img src="New_projects.png" title="New_projects.png" alt="New_projects.png" width="100" /><figcaption>New_projects.png</figcaption>
</figure></td>
<img src="Owasp-builders-small.png" title="Owasp-builders-small.png" alt="Owasp-builders-small.png" /><figcaption>Owasp-builders-small.png</figcaption>
</figure></td>
</tr>
<tr class="even">
<img src="Owasp-defenders-small.png" title="Owasp-defenders-small.png" alt="Owasp-defenders-small.png" /><figcaption>Owasp-defenders-small.png</figcaption>
</figure></td>
</tr>
<tr class="odd">
<img src="Cc-button-y-sa-small.png" title="Cc-button-y-sa-small.png" alt="Cc-button-y-sa-small.png" /><figcaption>Cc-button-y-sa-small.png</figcaption>
</figure></td>
</tr>
<tr class="even">
<img src="Project_Type_Files_CODE.jpg" title="Project_Type_Files_CODE.jpg" alt="Project_Type_Files_CODE.jpg" /><figcaption>Project_Type_Files_CODE.jpg</figcaption>
</figure></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

# Headers

The following contains a list of HTTP response headers related to
security.

## Response Headers

  - [HTTP Strict Transport Security (HSTS)](#hsts "wikilink")
  - [Public Key Pinning Extension for HTTP (HPKP)](#hpkp "wikilink")
  - [X-Frame-Options](#xfo "wikilink")
  - [X-XSS-Protection](#xxxsp "wikilink")
  - [X-Content-Type-Options](#xcto "wikilink")
  - [Content-Security-Policy](#csp "wikilink")
  - [X-Permitted-Cross-Domain-Policies](#xpcdp "wikilink")
  - [Referrer-Policy](#rp "wikilink")
  - [Expect-CT](#ect "wikilink")
  - [Feature-Policy](#fp "wikilink")

\==

<div id="hsts">

HTTP Strict Transport Security (HSTS)

</div>

\==

HTTP Strict Transport Security (HSTS) is a web security policy mechanism
which helps to protect websites against protocol [downgrade
attacks](https://en.wikipedia.org/wiki/Downgrade_attack) and [cookie
hijacking](https://www.owasp.org/index.php/Session_hijacking_attack). It
allows web servers to declare that web browsers (or other complying user
agents) should only interact with it using secure HTTPS connections, and
never via the insecure HTTP protocol. HSTS is an IETF standards track
protocol and is specified in RFC 6797. A server implements an HSTS
policy by supplying a header (Strict-Transport-Security) over an HTTPS
connection (HSTS headers over HTTP are ignored).

### Values

| Value             | Description                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| max-age=SECONDS   | The time, in seconds, that the browser should remember that this site is only to be accessed using HTTPS. |
| includeSubDomains | If this optional parameter is specified, this rule applies to all of the site's subdomains as well.       |

### Example

`Strict-Transport-Security: max-age=31536000 ; includeSubDomains`

### References

  - <https://tools.ietf.org/html/rfc6797>
  - <https://www.owasp.org/index.php/HTTP_Strict_Transport_Security>
  - <https://www.owasp.org/index.php/Test_HTTP_Strict_Transport_Security_(OTG-CONFIG-007)>
  - <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>
  - <https://www.chromium.org/hsts>
  - <https://developer.mozilla.org/en-US/docs/Web/Security/HTTP_strict_transport_security>
  - <https://raymii.org/s/tutorials/HTTP_Strict_Transport_Security_for_Apache_NGINX_and_Lighttpd.html>

\==

<div id="hpkp">

Public Key Pinning Extension for HTTP (HPKP)

</div>

\==

HTTP Public Key Pinning (HPKP) is a security mechanism which allows
HTTPS websites to resist impersonation by attackers using mis-issued or
otherwise fraudulent certificates. (For example, sometimes attackers can
compromise certificate authorities, and then can mis-issue certificates
for a web origin.).

The HTTPS web server serves a list of public key hashes, and on
subsequent connections clients expect that server to use one or more of
those public keys in its certificate chain. Deploying HPKP safely will
require operational and organizational maturity due to the risk that
hosts may make themselves unavailable by pinning to a set of public key
hashes that becomes invalid. With care, host operators can greatly
reduce the risk of [man-in-the-middle (MITM)
attacks](https://www.owasp.org/index.php/Man-in-the-middle_attack) and
other false authentication problems for their users without incurring
undue risk.

Before implement HPKP please read this
<https://www.chromestatus.com/feature/5903385005916160>.

### Values

| Value                 | Description                                                                                                                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pin-sha256="<sha256>" | The quoted string is the Base64 encoded Subject Public Key Information (SPKI) fingerprint. It is possible to specify multiple pins for different public keys. Some browsers might allow other hashing algorithms than SHA-256 in the future. |
| max-age=SECONDS       | The time, in seconds, that the browser should remember that this site is only to be accessed using one of the pinned keys.                                                                                                                   |
| includeSubDomains     | If this optional parameter is specified, this rule applies to all of the site's subdomains as well.                                                                                                                                          |
| report-uri="<URL>"    | If this optional parameter is specified, pin validation failures are reported to the given URL.                                                                                                                                              |

### Example

`Public-Key-Pins:
pin-sha256="d6qzRu9zOECb90Uez27xWltNsj0e1Md7GkYYkVoZWmM=";
pin-sha256="E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g=";
report-uri="http://example.com/pkp-report"; max-age=10000;
includeSubDomains`

### References

  - <https://tools.ietf.org/html/rfc7469>
  - <https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning#HTTP_pinning>
  - <https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning>
  - <https://developer.mozilla.org/en-US/docs/Web/Security/Public_Key_Pinning>
  - <https://raymii.org/s/articles/HTTP_Public_Key_Pinning_Extension_HPKP.html>
  - <https://labs.detectify.com/2016/07/05/what-hpkp-is-but-isnt/>
  - <https://blog.qualys.com/ssllabs/2016/09/06/is-http-public-key-pinning-dead>
  - <https://scotthelme.co.uk/im-giving-up-on-hpkp/>
  - <https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ>

\==

<div id="xfo">

X-Frame-Options

</div>

\==

X-Frame-Options response header improve the protection of web
applications against
[Clickjacking](https://www.owasp.org/index.php/Clickjacking). It
declares a policy communicated from a host to the client browser on
whether the browser must not display the transmitted content in frames
of other web pages.

### Values

| Value              | Description                                             |
| ------------------ | ------------------------------------------------------- |
| deny               | No rendering within a frame.                            |
| sameorigin         | No rendering if origin mismatch.                        |
| allow-from: DOMAIN | Allows rendering if framed by frame loaded from DOMAIN. |

### Example

`X-Frame-Options: deny`

### References

  - <https://tools.ietf.org/html/rfc7034>
  - <https://tools.ietf.org/html/draft-ietf-websec-x-frame-options-01>
  - <https://tools.ietf.org/html/draft-ietf-websec-frame-options-00>
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options>
  - <https://www.owasp.org/index.php/Clickjacking>
  - <https://blogs.msdn.microsoft.com/ieinternals/2010/03/30/combating-clickjacking-with-x-frame-options/>

\==

<div id="xxxsp">

X-XSS-Protection

</div>

\==

This header enables the [Cross-site scripting
(XSS)](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\))
filter in your browser.

### Values

| Value                                                                                        | Description                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                                                                                            | Filter disabled.                                                                                                                                                                  |
| 1                                                                                            | Filter enabled. If a cross-site scripting attack is detected, in order to stop the attack, the browser will sanitize the page.                                                    |
| 1; mode=block                                                                                | Filter enabled. Rather than sanitize the page, when a XSS attack is detected, the browser will prevent rendering of the page.                                                     |
| 1; report=[http://\[YOURDOMAIN\]/your_report_URI](http://%5BYOURDOMAIN%5D/your_report_URI) | Filter enabled. The browser will sanitize the page and report the violation. This is a Chromium function utilizing CSP violation reports to send details to a URI of your choice. |

### Example

`X-XSS-Protection: 1; mode=block`

### References

  - <https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)>
  - <https://www.virtuesecurity.com/blog/understanding-xss-auditor/>
  - <https://www.veracode.com/blog/2014/03/guidelines-for-setting-security-headers>
  - <http://zinoui.com/blog/security-http-headers#x-xss-protection>

\==

<div id="xcto">

X-Content-Type-Options

</div>

\==

Setting this header will prevent the browser from [interpreting files as
something else than declared by the content
type](https://en.wikipedia.org/wiki/Content_sniffing) in the HTTP
headers.

### Values

| Value   | Description                                                                                 |
| ------- | ------------------------------------------------------------------------------------------- |
| nosniff | Will prevent the browser from MIME-sniffing a response away from the declared content-type. |

### Example

`X-Content-Type-Options: nosniff`

### References

  - <https://msdn.microsoft.com/en-us/library/gg622941%28v=vs.85%29.aspx>
  - <https://blogs.msdn.microsoft.com/ie/2008/09/02/ie8-security-part-vi-beta-2-update/>

\==

<div id="csp">

Content-Security-Policy

</div>

\==

A Content Security Policy (CSP) requires careful tuning and precise
definition of the policy. If enabled, CSP has significant impact on the
way browsers render pages (e.g., inline JavaScript disabled by default
and must be explicitly allowed in policy). CSP prevents a wide range of
attacks, including [Cross-site
scripting](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\))
and other cross-site injections.

### Values

| Directive                 | Description                                                                                                                                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| base-uri                  | Define the base uri for relative uri.                                                                                                                                                                  |
| default-src               | Define loading policy for all resources type in case of a resource type dedicated directive is not defined (fallback).                                                                                 |
| script-src                | Define which scripts the protected resource can execute.                                                                                                                                               |
| object-src                | Define from where the protected resource can load plugins.                                                                                                                                             |
| style-src                 | Define which styles (CSS) the user applies to the protected resource.                                                                                                                                  |
| img-src                   | Define from where the protected resource can load images.                                                                                                                                              |
| media-src                 | Define from where the protected resource can load video and audio.                                                                                                                                     |
| frame-src                 | Deprecated and replaced by child-src. Define from where the protected resource can embed frames.                                                                                                       |
| child-src                 | Define from where the protected resource can embed frames.                                                                                                                                             |
| frame-ancestors           | Define from where the protected resource can be embedded in frames.                                                                                                                                    |
| font-src                  | Define from where the protected resource can load fonts.                                                                                                                                               |
| connect-src               | Define which URIs the protected resource can load using script interfaces.                                                                                                                             |
| manifest-src              | Define from where the protected resource can load manifest.                                                                                                                                            |
| form-action               | Define which URIs can be used as the action of HTML form elements.                                                                                                                                     |
| sandbox                   | Specifies an HTML sandbox policy that the user agent applies to the protected resource.                                                                                                                |
| script-nonce              | Define script execution by requiring the presence of the specified nonce on script elements.                                                                                                           |
| plugin-types              | Define the set of plugins that can be invoked by the protected resource by limiting the types of resources that can be embedded.                                                                       |
| reflected-xss             | Instructs a user agent to activate or deactivate any heuristics used to filter or block reflected cross-site scripting attacks, equivalent to the effects of the non-standard X-XSS-Protection header. |
| block-all-mixed-content   | Prevent user agent from loading mixed content.                                                                                                                                                         |
| upgrade-insecure-requests | Instructs user agent to download insecure resources using HTTPS.                                                                                                                                       |
| referrer                  | Define information user agent must send in Referer header.                                                                                                                                             |
| report-uri                | Specifies a URI to which the user agent sends reports about policy violation.                                                                                                                          |
| report-to                 | Specifies a group (defined in Report-To header) to which the user agent sends reports about policy violation.                                                                                          |

### Example

`Content-Security-Policy: script-src 'self'`

### References

  - <https://www.w3.org/TR/CSP/>
  - <https://developer.mozilla.org/en-US/docs/Web/Security/CSP>
  - <https://www.owasp.org/index.php/Content_Security_Policy>
  - <https://scotthelme.co.uk/content-security-policy-an-introduction/>
  - <https://report-uri.io>
  - <http://www.cspplayground.com/home>
  - <http://content-security-policy.com>

\==

<div id="xpcdp">

X-Permitted-Cross-Domain-Policies

</div>

\==

A cross-domain policy file is an XML document that grants a web client,
such as Adobe Flash Player or Adobe Acrobat (though not necessarily
limited to these), permission to handle data across domains. When
clients request content hosted on a particular source domain and that
content make requests directed towards a domain other than its own, the
remote domain needs to host a cross-domain policy file that grants
access to the source domain, allowing the client to continue the
transaction. Normally a meta-policy is declared in the master policy
file, but for those who can’t write to the root directory, they can also
declare a meta-policy using the X-Permitted-Cross-Domain-Policies HTTP
response header.

### Values

| Value           | Description                                                                                                             |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| none            | No policy files are allowed anywhere on the target server, including this master policy file.                           |
| master-only     | Only this master policy file is allowed.                                                                                |
| by-content-type | \[HTTP/HTTPS only\] Only policy files served with Content-Type: text/x-cross-domain-policy are allowed.                 |
| by-ftp-filename | \[FTP only\] Only policy files whose file names are crossdomain.xml (i.e. URLs ending in /crossdomain.xml) are allowed. |
| all             | All policy files on this target domain are allowed.                                                                     |

### Example

`X-Permitted-Cross-Domain-Policies: none`

### References

  - <https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html>
  - <https://www.adobe.com/devnet/adobe-media-server/articles/cross-domain-xml-for-streaming.html>
  - <https://www.perpetual-beta.org/weblog/security-headers.html#rule-8470-2-establish-a-cross-domain-meta-policy>
  - <https://danielnixon.org/http-security-headers/>
  - <https://rorsecurity.info/portfolio/new-http-headers-for-more-security>
  - <https://github.com/twitter/secureheaders/issues/88>

\==

<div id="rp">

Referrer-Policy

</div>

\==

The Referrer-Policy HTTP header governs which referrer information, sent
in the Referer header, should be included with requests made.

### Values

| Value                           | Description                                                                                                                                                                                                             |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| no-referrer                     | The Referer header will be omitted entirely. No referrer information is sent along with requests.                                                                                                                       |
| no-referrer-when-downgrade      | This is the user agent's default behavior if no policy is specified. The origin is sent as referrer to a-priori as-much-secure destination (HTTPS-\>HTTPS), but isn't sent to a less secure destination (HTTPS-\>HTTP). |
| origin                          | Only send the origin of the document as the referrer in all cases. The document https://example.com/page.html will send the referrer https://example.com/.                                                              |
| origin-when-cross-origin        | Send a full URL when performing a same-origin request, but only send the origin of the document for other cases.                                                                                                        |
| same-origin                     | A referrer will be sent for same-site origins, but cross-origin requests will contain no referrer information.                                                                                                          |
| strict-origin                   | Only send the origin of the document as the referrer to a-priori as-much-secure destination (HTTPS-\>HTTPS), but don't send it to a less secure destination (HTTPS-\>HTTP).                                             |
| strict-origin-when-cross-origin | Send a full URL when performing a same-origin request, only send the origin of the document to a-priori as-much-secure destination (HTTPS-\>HTTPS), and send no header to a less secure destination (HTTPS-\>HTTP).     |
| unsafe-url                      | Send a full URL (stripped from parameters) when performing a a same-origin or cross-origin request.                                                                                                                     |

### Example

`Referrer-Policy: no-referrer`

### References

  - <https://www.w3.org/TR/referrer-policy/>
  - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy>

\==

<div id="ect">

Expect-CT

</div>

\==

The Expect-CT header is used by a server to indicate that browsers
should evaluate connections to the host emitting the header for
[Certificate Transparency](https://www.certificate-transparency.org)
compliance.

### Values

| Value      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| report-uri | The optional report-uri directive indicates the URL to which the browser should report Expect-CT failures.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| enforce    | The optional enforce directive is a valueless directive that, if present, signals to the browser that compliance to the CT Policy should be enforced (rather than report-only) and that the browser should refuse future connections that violate its CT Policy. When both the enforce directive and report-uri directive are present, the configuration is referred to as an "enforce-and-report" configuration, signalling to the browser both that compliance to the CT Policy should be enforced and that violations should be reported. |
| max-age    | The max-age directive specifies the number of seconds after the reception of the Expect-CT header field during which the browser should regard the host from whom the message was received as a Known Expect-CT Host.                                                                                                                                                                                                                                                                                                                        |

### Example

`Expect-CT: max-age=86400, enforce,
report-uri="`<https://foo.example/report>`"`

### References

  - <https://tools.ietf.org/html/draft-ietf-httpbis-expect-ct-02>
  - <http://httpwg.org/http-extensions/expect-ct.html>
  - <https://scotthelme.co.uk/a-new-security-header-expect-ct/>

\==

<div id="fp">

Feature-Policy

</div>

\==

The Feature-Policy header allows developers to selectively enable and
disable use of various browser features and APIs..

### Values

| Value                | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| accelerometer        | Controls access to accelerometer sensors on the device.    |
| ambient-light-sensor | Controls access to ambient light sensors on the device.    |
| autoplay             | Controls access to autoplay through play() and autoplay.   |
| camera               | Controls access to video input devices.                    |
| encrypted-media      | Controls whether requestMediaKeySystemAccess() is allowed. |
| fullscreen           | Controls whether requestFullscreen() is allowed.           |
| geolocation          | Controls access to Geolocation interface.                  |
| gyroscope            | Controls access to gyroscope sensors on the device.        |
| magnetometer         | Controls access to magnetometer sensors on the device.     |
| microphone           | Controls access to audio input devices.                    |
| midi                 | Controls access to requestMIDIAccess() method.             |
| payment              | Controls access to PaymentRequest interface.               |
| picture-in-picture   | Controls access to Picture in Picture.                     |
| speaker              | Controls access to audio output devices.                   |
| usb                  | Controls access to USB devices.                            |
| vibrate              | Controls access to vibrate() method.                       |
| vr                   | Controls access to VR displays.                            |

### Example

`Feature-Policy: vibrate 'none'; geolocation 'none'`

### References

  - <https://wicg.github.io/feature-policy/>
  - <https://github.com/WICG/feature-policy/blob/master/features.md>
  - <https://scotthelme.co.uk/a-new-security-header-feature-policy/>

# Compatibility Matrix

## Browser Support

|                                              | Internet Explorer | Edge | Firefox | Chrome | Safari | Opera | Android |
| -------------------------------------------- | ----------------- | ---- | ------- | ------ | ------ | ----- | ------- |
| HTTP Strict Transport Security (HSTS)        | 11                |      | 13      |        | 47     |       | 49      |
| Public Key Pinning Extension for HTTP (HPKP) | NS                |      | NS      |        | 47     |       | 49      |
| X-Frame-Options                              | 8                 |      | 13      |        | 47     |       | 49      |
| X-XSS-Protection                             | 8                 |      |         |        | NS     |       | 4+      |
| X-Content-Type-Options                       | 8                 |      |         |        | 51     |       | 1.0     |
| Content-Security-Policy                      | 11                |      | 13      |        | 47     |       | 49      |
| X-Permitted-Cross-Domain-Policies            |                   |      |         |        |        |       |         |
| Referrer-Policy                              | NS                |      | NS      |        | 50     |       | 56      |
| Expect-CT                                    |                   |      |         |        |        |       | 61      |
| Feature-Policy                               |                   |      |         |        |        |       |         |

NS = Not Supported

\+ = Specified version and above

## References

  - HTTP Strict Transport Security (HSTS)
      - <https://blogs.windows.com/msedgedev/2015/06/09/http-strict-transport-security-comes-to-internet-explorer-11-on-windows-8-1-and-windows-7/>
      - <https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>
      - <https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet>
      - <http://caniuse.com/#search=HSTS>
  - Public Key Pinning Extension for HTTP (HPKP)
      - <http://caniuse.com/#search=Public%20Key%20Pinning>
      - <https://groups.google.com/a/chromium.org/forum/m/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ>
  - X-Frame-Options
      - <http://caniuse.com/#search=X-Frame-Options>
  - X-XSS-Protection
      - <https://wiki.mozilla.org/Security/Features/XSS_Filter>
      - <https://blogs.msdn.microsoft.com/ieinternals/2011/01/31/controlling-the-xss-filter/>
  - X-Content-Type-Options
      - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options>
  - Content-Security-Policy
      - <http://caniuse.com/#search=Content%20Security%20Policy>
  - X-Permitted-Cross-Domain-Policies
      - <https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html>
  - Referrer-Policy
      - <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy>
  - Expect-CT
      - <https://www.chromestatus.com/feature/5677171733430272>
  - Feature-Policy
      - \[update needed\]

# Stats

Coming soon... for now check [this](https://oshp.bsecteam.com).

# Technical Resources

This section cover a list of tools to analyze, develop and administrate
HTTP secure headers in order to help achieve more secure and trustworthy
web systems.

<table>
<thead>
<tr class="header">
<th><p>ead</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> A security scanner for HTTP response headers. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> Python script to get some response headers from Alexa top sites file and store in a MySQL database. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt"> There are services out there that will analyse the HTTP response headers of other sites but I also wanted to add a rating system to the results. The HTTP response headers that this site analyses provide huge levels of protection and it's important that sites deploy them. Hopefully, by providing an easy mechanism to assess them, and further information on how to deploy missing headers, we can drive up the usage of security based headers across the web. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt"> A Mozilla project designed to help developers, system administrators, and security professionals configure their sites safely and securely. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt"> An online service that will retrieve and analyse headers syntax and proper configuration in a comprehensive way. It will be able for instance to highlight Public-Key-Pins that matches one certificate of the chain or if Content-Security-Policy contains values that could be unsafe or too permissive. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt"> Just another web scanner for HTTP response headers. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt"> Chrome extension that allows the inspection of security aspects of a site's HTTP headers, cookies and other key security settings. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt"> While each project you launch may have a different feature set, they often share many of the same performance, SEO and security requirements. This tool aims to automate the process of checking your list of requirements shortly before launch or directly after a deployment. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt"> Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML. </font></p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><p>ead</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt"> Security related headers all in one gem. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> SHIM is a HTTP module that provides protection for many vulnerabilities by injecting security-specific HTTP headers into ASP.NET web applications. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> Spring Security’s support for adding various security headers to the response. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> A PHP class aiming to make the use of browser security features more accessible. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> Security related HTTP headers for Rack applications. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> Node.js (express). </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> A CSP plugin for hapi. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> NWebsec consists of several security libraries for ASP.NET applications. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> django-csp + commonware; django-security. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> Secure is a lightweight package that adds optional security headers and cookie attributes for Python web frameworks. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> Package secureheader adds some HTTP header fields widely considered to improve safety of HTTP requests. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> This Plug will automatically apply several security headers to the Plug.Conn response. By design SecureHeaders will attempt to apply the most strict security policy. Although, security headers are configurable and are validated to avoid misconfiguration. </font></p></td>
</tr>
<tr class="even">
<p><font size="2" style="font-size: 9pt”"> A bundle for applying default web security functionality to a dropwizard application. </font></p></td>
</tr>
<tr class="odd">
<p><font size="2" style="font-size: 9pt”"> This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file. </font></p></td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><p>ead</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
</tr>
<tr class="even">
<p>&lt;font size="2" style="“font-size:9pt""&gt; Puppet module to enable, configure and manage secure http headers on web servers. </font></p></td>
</tr>
</tbody>
</table>

# Top Websites Examples

HTTP response headers from the top websites in the world.

Command used to extract the headers:

`curl -L -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36" -s -D -
https://www.example.com -o /dev/null`

## Google

    $ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.google.com -o /dev/null
    HTTP/1.1 302 Found
    Location: https://www.google.com.br/?gws_rd=cr&dcr=0&ei=rtcKWpnkNYaawATUn6agCg
    Cache-Control: private
    Content-Type: text/html; charset=UTF-8
    P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
    Date: Tue, 14 Nov 2017 11:46:54 GMT
    Server: gws
    Content-Length: 273
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN
    Set-Cookie: NID=117=GENZIllQGZFmhCBmap1YThta_hUvvZ9Xm517XXWpF9eCKNqW6_luvZm1b_ai7BN4lAA2pP2Z22BveHqjUrqZxpY38NKSYLKWFGrVh6tGAHcbNw6OHQ_F77bNJWV0BZOZ; expires=Wed, 16-May-2018 11:46:54 GMT; path=/; domain=.google.com; HttpOnly
    Alt-Svc: quic=":443"; ma=2592000; v="41,39,38,37,35"

    HTTP/1.1 200 OK
    Date: Tue, 14 Nov 2017 11:46:55 GMT
    Expires: -1
    Cache-Control: private, max-age=0
    Content-Type: text/html; charset=UTF-8
    Strict-Transport-Security: max-age=3600
    P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
    Server: gws
    X-XSS-Protection: 1; mode=block
    X-Frame-Options: SAMEORIGIN
    Set-Cookie: 1P_JAR=2017-11-14-11; expires=Thu, 14-Dec-2017 11:46:55 GMT; path=/; domain=.google.com.br
    Set-Cookie: NID=117=fR73jhascV3B9fbiVfYdvGlilR_tgYNhela9rXdCavJiJoYpkNSTq0NtFqNSV8im602zM7Of-S1GUr_ncSuT3p6tzlw3e6_9ccqPttSuniTHWZEgBtUL1VXTgXBdjKMe; expires=Wed, 16-May-2018 11:46:55 GMT; path=/; domain=.google.com.br; HttpOnly
    Alt-Svc: quic=":443"; ma=2592000; v="41,39,38,37,35"
    Accept-Ranges: none
    Vary: Accept-Encoding
    Transfer-Encoding: chunked

## Facebook

    $ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.facebook.com -o /dev/null
    HTTP/1.1 200 OK
    X-XSS-Protection: 0
    Pragma: no-cache
    content-security-policy: default-src * data: blob:;script-src *.facebook.com *.fbcdn.net *.facebook.net *.google-analytics.com *.virtualearth.net *.google.com 127.0.0.1:* *.spotilocal.com:* 'unsafe-inline' 'unsafe-eval' fbstatic-a.akamaihd.net fbcdn-static-b-a.akamaihd.net *.atlassolutions.com blob: data: 'self';style-src data: blob: 'unsafe-inline' *;connect-src *.facebook.com *.fbcdn.net *.facebook.net *.spotilocal.com:* *.akamaihd.net wss://*.facebook.com:* https://fb.scanandcleanlocal.com:* *.atlassolutions.com attachment.fbsbx.com ws://localhost:* blob: *.cdninstagram.com 'self' chrome-extension://boadgeojelhgndaghljhdicfkmllpafd chrome-extension://dliochdbjfkdbacpmhlcpmleaejidimm;
    Cache-Control: private, no-cache, no-store, must-revalidate
    X-Frame-Options: DENY
    expect-ct: max-age=10, report-uri="http://reports.fb.com/expectct/"
    Strict-Transport-Security: max-age=15552000; preload
    X-Content-Type-Options: nosniff
    Expires: Sat, 01 Jan 2000 00:00:00 GMT
    Set-Cookie: fr=0Bf96eRMD0zCulvzh..BaCtgp.jl.AAA.0.0.BaCtgp.AWVGQojt; expires=Mon, 12-Feb-2018 11:48:57 GMT; Max-Age=7776000; path=/; domain=.facebook.com; secure; httponly
    Set-Cookie: sb=KdgKWqMf8J84KfUg99AxaG1B; expires=Thu, 14-Nov-2019 11:48:57 GMT; Max-Age=63072000; path=/; domain=.facebook.com; secure; httponly
    Vary: Accept-Encoding
    Content-Type: text/html; charset=UTF-8
    X-FB-Debug: llncdeFRYCCoWkXqx2VCdUGtdHZvjsr6OA7JNrtEe18ZuZAqcKCH4km9SSkNTHIcuXmzwRMzyBQt0Uz7T6ltQg==
    Date: Tue, 14 Nov 2017 11:48:57 GMT
    Transfer-Encoding: chunked
    Connection: keep-alive

## Twitter

    $ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.twitter.com -o /dev/null
    HTTP/1.1 301 Moved Permanently
    content-length: 0
    date: Tue, 14 Nov 2017 11:50:11 GMT
    location: https://twitter.com/
    server: tsa_d
    set-cookie: personalization_id="v1_nyz+ctxxDiBbh4s6VjzQIg=="; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
    set-cookie: guest_id=v1%3A151066021116455299; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
    strict-transport-security: max-age=631138519
    x-connection-hash: d9a9eea848268dae67e7743d5bfd2dd5
    x-response-time: 135

    HTTP/1.1 200 OK
    cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0
    content-length: 345977
    content-security-policy: script-src https://connect.facebook.net https://cm.g.doubleclick.net https://ssl.google-analytics.com https://graph.facebook.com 'nonce-f/+1f61E6Z0qq8p+L4UIQw==' https://twitter.com 'unsafe-eval' https://*.twimg.com https://api.twitter.com https://analytics.twitter.com https://publish.twitter.com https://ton.twitter.com https://syndication.twitter.com https://www.google.com https://t.tellapart.com https://platform.twitter.com https://www.google-analytics.com blob: 'self'; frame-ancestors 'self'; font-src https://twitter.com https://*.twimg.com data: https://ton.twitter.com https://fonts.gstatic.com https://maxcdn.bootstrapcdn.com https://netdna.bootstrapcdn.com 'self'; media-src https://rmpdhdsnappytv-vh.akamaihd.net https://prod-video-eu-central-1.pscp.tv https://v.cdn.vine.co https://dwo3ckksxlb0v.cloudfront.net https://twitter.com https://amp.twimg.com https://smmdhdsnappytv-vh.akamaihd.net https://*.twimg.com https://prod-video-eu-west-1.pscp.tv https://rmmdhdsnappytv-vh.akamaihd.net https://prod-video-us-west-2.pscp.tv https://prod-video-us-west-1.pscp.tv https://prod-video-ap-northeast-1.pscp.tv https://smdhdsnappytv-vh.akamaihd.net https://ton.twitter.com https://rmdhdsnappytv-vh.akamaihd.net https://mmdhdsnappytv-vh.akamaihd.net https://smpdhdsnappytv-vh.akamaihd.net https://prod-video-sa-east-1.pscp.tv https://mdhdsnappytv-vh.akamaihd.net https://prod-video-ap-southeast-2.pscp.tv https://mtc.cdn.vine.co https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv blob: 'self' https://prod-video-ap-southeast-1.pscp.tv https://mpdhdsnappytv-vh.akamaihd.net https://dev-video-eu-west-1.pscp.tv; connect-src https://rmpdhdsnappytv-vh.akamaihd.net https://prod-video-eu-central-1.pscp.tv https://graph.facebook.com https://*.giphy.com https://dwo3ckksxlb0v.cloudfront.net https://vmaprel.snappytv.com https://smmdhdsnappytv-vh.akamaihd.net https://*.twimg.com https://embed.pscp.tv https://api.twitter.com https://prod-video-eu-west-1.pscp.tv https://rmmdhdsnappytv-vh.akamaihd.net https://prod-video-us-west-2.pscp.tv https://pay.twitter.com https://prod-video-us-west-1.pscp.tv https://analytics.twitter.com https://vmap.snappytv.com https://*.twprobe.net https://prod-video-ap-northeast-1.pscp.tv https://smdhdsnappytv-vh.akamaihd.net https://syndication.twitter.com https://sentry.io https://rmdhdsnappytv-vh.akamaihd.net https://media.riffsy.com https://mmdhdsnappytv-vh.akamaihd.net https://embed.periscope.tv https://smpdhdsnappytv-vh.akamaihd.net https://prod-video-sa-east-1.pscp.tv https://vmapstage.snappytv.com https://upload.twitter.com https://proxsee.pscp.tv https://mdhdsnappytv-vh.akamaihd.net https://prod-video-ap-southeast-2.pscp.tv https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv 'self' https://vmap.grabyo.com https://prod-video-ap-southeast-1.pscp.tv https://mpdhdsnappytv-vh.akamaihd.net https://dev-video-eu-west-1.pscp.tv; style-src https://fonts.googleapis.com https://twitter.com https://*.twimg.com https://translate.googleapis.com https://ton.twitter.com 'unsafe-inline' https://platform.twitter.com https://maxcdn.bootstrapcdn.com https://netdna.bootstrapcdn.com 'self'; object-src https://twitter.com https://pbs.twimg.com; default-src 'self'; frame-src https://staticxx.facebook.com https://twitter.com https://*.twimg.com https://5415703.fls.doubleclick.net https://player.vimeo.com https://pay.twitter.com https://www.facebook.com https://ton.twitter.com https://syndication.twitter.com https://vine.co twitter: https://www.youtube.com https://platform.twitter.com https://upload.twitter.com https://s-static.ak.facebook.com https://4337974.fls.doubleclick.net https://8122179.fls.doubleclick.net 'self' https://donate.twitter.com; img-src https://prod-video-eu-central-1.pscp.tv https://prod-profile.pscp.tv https://graph.facebook.com https://prod-thumbnail.pscp.tv https://*.giphy.com https://twitter.com https://*.twimg.com https://ad.doubleclick.net https://prod-video-eu-west-1.pscp.tv data: https://prod-video-us-west-2.pscp.tv https://prod-video-us-west-1.pscp.tv https://prod-video-ap-northeast-1.pscp.tv https://lumiere-a.akamaihd.net https://fbcdn-profile-a.akamaihd.net https://www.facebook.com https://ton.twitter.com https://*.fbcdn.net https://syndication.twitter.com https://media.riffsy.com https://www.google.com https://prod-profile.periscope.tv https://prod-video-sa-east-1.pscp.tv https://stats.g.doubleclick.net https://platform.twitter.com https://prod-video-ap-southeast-2.pscp.tv https://api.mapbox.com https://www.google-analytics.com https://dev-video-us-west-2.pscp.tv https://prod-video-us-east-1.pscp.tv blob: https://prod-thumbnail-small.pscp.tv https://prod-thumbnail-small.periscope.tv 'self' https://prod-thumbnail.periscope.tv https://prod-video-ap-southeast-1.pscp.tv https://dev-video-eu-west-1.pscp.tv; report-uri https://twitter.com/i/csp_report?a=NVQWGYLXFVZXO2LGOQ%3D%3D%3D%3D%3D%3D&ro=false;
    content-type: text/html;charset=utf-8
    date: Tue, 14 Nov 2017 11:50:11 GMT
    expires: Tue, 31 Mar 1981 05:00:00 GMT
    last-modified: Tue, 14 Nov 2017 11:50:11 GMT
    pragma: no-cache
    server: tsa_d
    set-cookie: fm=0; Expires=Tue, 14 Nov 2017 11:50:02 UTC; Path=/; Domain=.twitter.com; Secure; HTTPOnly
    set-cookie: _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMOCXbpfAToMY3NyZl9p%250AZCIlOTk3MjYzYzc1NDhkOTA1ZTlhZTIyNGE2Zjk5Nzg0NTk6B2lkIiU0ODIw%250AZWRkNjc4Njg2M2IzYmI3ZTA3N2YxMTA4YzE5Nw%253D%253D--7abf7eef950088f9f728686ce29881ef501487dd; Path=/; Domain=.twitter.com; Secure; HTTPOnly
    set-cookie: personalization_id="v1_rrHzrB5h0Qs1Oz4uhOjFJg=="; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
    set-cookie: guest_id=v1%3A151066021139105511; Expires=Thu, 14 Nov 2019 11:50:11 UTC; Path=/; Domain=.twitter.com
    set-cookie: ct0=ba98c8a6cb4c664151a98c8bd9eb4b4d; Expires=Tue, 14 Nov 2017 17:50:11 UTC; Path=/; Domain=.twitter.com; Secure
    status: 200 OK
    strict-transport-security: max-age=631138519
    x-connection-hash: 769f9dcd87b9274776136b99b3181a44
    x-content-type-options: nosniff
    x-frame-options: SAMEORIGIN
    x-response-time: 359
    x-transaction: 007d216900cbc2ad
    x-twitter-response-tags: BouncerCompliant
    x-ua-compatible: IE=edge,chrome=1
    x-xss-protection: 1; mode=block

## Github

    $ curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36" -s -D - https://www.github.com -o /dev/null
    HTTP/1.1 301 Moved Permanently
    Content-length: 0
    Location: https://github.com/

    HTTP/1.1 200 OK
    Server: GitHub.com
    Date: Tue, 14 Nov 2017 11:51:27 GMT
    Content-Type: text/html; charset=utf-8
    Transfer-Encoding: chunked
    Status: 200 OK
    Cache-Control: no-cache
    Vary: X-PJAX
    X-UA-Compatible: IE=Edge,chrome=1
    Set-Cookie: logged_in=no; domain=.github.com; path=/; expires=Sat, 14 Nov 2037 11:51:27 -0000; secure; HttpOnly
    Set-Cookie: _gh_sess=eyJzZXNzaW9uX2lkIjoiODI5ZGZjZDhlZDFlMjBjZTBhMTljMjk5ZDU1ZDBlODgiLCJsYXN0X3JlYWRfZnJvbV9yZXBsaWNhcyI6MTUxMDY2MDI4NzMxNywiX2NzcmZfdG9rZW4iOiIvTjkya2RHLzJJN2dtbU12eWQ3UGJDeTJ0aU1tZHJrci8wVzlpMi9yajFZPSJ9--5920790d2e11e8d4a32177a14ac25fae6e8f9789; path=/; secure; HttpOnly
    X-Request-Id: b31804a05047fd1326fe28cf3d6f33aa
    X-Runtime: 0.036845
    Expect-CT: max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"
    Content-Security-Policy: default-src 'none'; base-uri 'self'; block-all-mixed-content; child-src render.githubusercontent.com; connect-src 'self' uploads.github.com status.github.com collector.githubapp.com api.github.com www.google-analytics.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com wss://live.github.com; font-src assets-cdn.github.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; img-src 'self' data: assets-cdn.github.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com; media-src 'none'; script-src assets-cdn.github.com; style-src 'unsafe-inline' assets-cdn.github.com
    Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
    Public-Key-Pins: max-age=0; pin-sha256="WoiWRyIOVNa9ihaBciRSC7XHjliYS9VwUGOIud4PB18="; pin-sha256="RRM1dGqnDFsCJXBTHky16vi1obOlCgFFn/yOhI/y+ho="; pin-sha256="k2v657xBsOVe1PQRwOsHsw3bsGT2VzIqz5K+59sNQws="; pin-sha256="K87oWBWM9UZfyddvDfoxL+8lpNyoUB2ptGtn0fv6G2Q="; pin-sha256="IQBnNBEiFuhj+8x6X8XLgh01V9Ic5/V3IRQLNFFc7v4="; pin-sha256="iie1VXtL7HzAMF+/PVPR9xzT80kQxdZeJ+zduCB3uj0="; pin-sha256="LvRiGEjRqfzurezaWuj8Wie2gyHMrW5Q06LspMnox7A="; includeSubDomains
    X-Content-Type-Options: nosniff
    X-Frame-Options: deny
    X-XSS-Protection: 1; mode=block
    X-Runtime-rack: 0.043225
    X-GitHub-Request-Id: 9AB0:25783:6A523:B814E:5A0AD8BE

# Best Practices

Please note the best practices below suggest methods to change webserver
configuration to add headers. Security headers can also be successfully
added to your application at the software level as well in almost every
web language. Many web frameworks add some of these headers
automatically.

## Response Headers

  - [HTTP Strict Transport Security (HSTS)](#hsts_bp "wikilink")
  - [Public Key Pinning Extension for HTTP (HPKP)](#hpkp_bp "wikilink")
  - [X-Frame-Options](#xfo_bp "wikilink")
  - [X-XSS-Protection](#xxxsp_bp "wikilink")
  - [X-Content-Type-Options](#xcto_bp "wikilink")
  - [Content-Security-Policy](#csp_bp "wikilink")
  - [X-Permitted-Cross-Domain-Policies](#xpcdp_bp "wikilink")
  - [Referrer-Policy](#rp_bp "wikilink")
  - [Expect-CT](#ect_bp "wikilink")
  - [Feature-Policy](#fp_bp "wikilink")

\==

<div id="hsts_bp">

HTTP Strict Transport Security (HSTS)

</div>

\==

  - Apache

<!-- end list -->

  -
    Edit your apache configuration file and add the following to your
    VirtualHost.
    :`Header always set Strict-Transport-Security "max-age=63072000;
    includeSubdomains"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    Edit your nginx configuration file and add the following snippet.
    :`add_header Strict-Transport-Security "max-age=63072000;
    includeSubdomains";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    Edit your lighttpd configuration file and add the following
    snippet.
    :`setenv.add-response-header = ("Strict-Transport-Security" =>
    "max-age=63072000; includeSubdomains",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#strict-transport-security>

\==

<div id="hpkp_bp">

Public Key Pinning Extension for HTTP (HPKP)

</div>

\==

  - Apache

<!-- end list -->

  -
    Edit your apache configuration file and add the following to your
    VirtualHost.
    :`Header set Public-Key-Pins
    "pin-sha256=\"klO23nT2ehFDXCfx3eHTDRESMz3asj1muO+4aIdjiuY=\";
    pin-sha256=\"633lt352PKRXbOwf4xSEa1M517scpD3l5f79xMD9r9Q=\";
    max-age=2592000; includeSubDomains"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    Edit your nginx configuration file and add the following snippet.
    :`add_header Public-Key-Pins
    "pin-sha256=\"klO23nT2ehFDXCfx3eHTDRESMz3asj1muO+4aIdjiuY=\";
    pin-sha256=\"633lt352PKRXbOwf4xSEa1M517scpD3l5f79xMD9r9Q=\";
    max-age=2592000; includeSubDomains";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    Edit your lighttpd configuration file and add the following
    snippet.
    :`setenv.add-response-header = ("Public-Key-Pins" =>
    "pin-sha256=\"klO23nT2ehFDXCfx3eHTDRESMz3asj1muO+4aIdjiuY=\";
    pin-sha256=\"633lt352PKRXbOwf4xSEa1M517scpD3l5f79xMD9r9Q=\";
    max-age=2592000; includeSubDomains",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#public-key-pinning>

\==

<div id="xfo_bp">

X-Frame-Options

</div>

\==

  - Apache

<!-- end list -->

  -
    Add this line below into your site's configuration to configure
    Apache to send X-Frame-Options header for all pages.
    :`Header set X-Frame-Options "DENY"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    Add snippet below into configuration file to send X-Frame-Options
    header.
    :`add_header X-Frame-Options "DENY";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    Add snippet below into configuration file to send X-Frame-Options
    header.
    :`setenv.add-response-header = ("X-Frame-Options" => "DENY",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#x-frame-options>

\==

<div id="xxxsp_bp">

X-XSS-Protection

</div>

\==

Add appropriate snippet into configuration file.

  - Apache

<!-- end list -->

  -
    `Header set X-XSS-Protection "1; mode=block"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    `add_header X-XSS-Protection "1;mode=block";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    `setenv.add-response-header = ("X-XSS-Protection" => "1;
    mode=block",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#x-xss-protection>

\==

<div id="xcto_bp">

X-Content-Type-Options

</div>

\==

Add appropriate snippet into configuration file.

  - Apache

<!-- end list -->

  -
    `Header set X-Content-Type-Options "nosniff"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    `add_header X-Content-Type-Options "nosniff";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    `setenv.add-response-header = ("X-Content-Type-Options" =>
    "nosniff",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#x-content-type-options>

\==

<div id="csp_bp">

Content-Security-Policy

</div>

\==

Add appropriate snippet into configuration file.

  - Apache

<!-- end list -->

  -
    `Header set Content-Security-Policy "script-src 'self'; object-src
    'self'"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    `add_header Content-Security-Policy "script-src 'self'; object-src
    'self'";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    `setenv.add-response-header = ("Content-Security-Policy" =>
    "script-src 'self'; object-src 'self'",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    Visit
    <https://scotthelme.co.uk/hardening-your-http-response-headers/#content-security-policy>

\==

<div id="xpcdp_bp">

X-Permitted-Cross-Domain-Policies

</div>

\==

Add appropriate snippet into configuration file.

  - Apache

<!-- end list -->

  -
    `Header set X-Permitted-Cross-Domain-Policies "none"`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    `add_header X-Permitted-Cross-Domain-Policies "none";`

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    `setenv.add-response-header = ("X-Permitted-Cross-Domain-Policies"
    => "none",)`

<!-- end list -->

  - IIS

<!-- end list -->

  -
    \[update needed\]

\==

<div id="rp_bp">

Referrer-Policy

</div>

\==

  - Apache

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - nginx

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - IIS

<!-- end list -->

  -
    \[update needed\]

\==

<div id="ect_bp">

Expect-CT

</div>

\==

  - Apache

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - nginx

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - IIS

<!-- end list -->

  -
    \[update needed\]

\==

<div id="fp_bp">

Feature-Policy

</div>

\== Disables camera, microphone, and payment API. More features can be
added to restrict if desired (vr, midi, etc).

  - Apache

<!-- end list -->

  -
    `Header set Feature-Policy: camera: 'none'; payment: 'none';
    microphone: 'none'`

<!-- end list -->

  - nginx

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - lighttpd

<!-- end list -->

  -
    \[update needed\]

<!-- end list -->

  - IIS

<!-- end list -->

  -
    \[update needed\]

# FAQs

  - What is HTTP header?
    HTTP header fields are part of HTTP message defined in RFC 2616 that
    consists of requests from client to server and responses from server
    to client that define parameters for the communication process
    including: language, compression support, security and a lot of
    resources.

<!-- end list -->

  - Is there a standard for HTTP headers?
    A core set of fields is standardized by the Internet Engineering
    Task Force (IETF) in RFCs 7230, 7231, 7232, 7233, 7234, and 7235.
    The permanent registry of header fields and repository of
    provisional registrations are maintained by the IANA. Additional
    field names and permissible values may be defined by each
    application. Non-standard header fields were conventionally marked
    by prefixing the field name with X- but this convention was
    deprecated in June 2012 because of the inconveniences it caused when
    non-standard fields became standard. An earlier restriction on use
    of Downgraded- was lifted in March 2013.

<!-- end list -->

  - Why I need worry about that?
    Like other initiatives supported by OWASP, this project have the
    objetive to help all community to conceive, develop, acquire,
    operate and maintain applications that can be trusted as provide
    useful information about the use relative of secure http headers by
    applications and platforms supported.

<!-- end list -->

  - Where can apply secure features presented by this project?
    The effectiveness provides by secure http headers demands that
    application or some component of infrastructure indicate proper
    header and correspondent value as like use of some client that
    implement that feature.

<!-- end list -->

  - When I consider apply this improvements?
    The short response it's right now. However we believe in approach
    more responsible. So we recommend conducting a planning and
    preliminary study, as well the incremental inclusion of insurance
    headers.

<!-- end list -->

  -
    Headers like: [Public Key Pinning Extension for HTTP
    (HPKP)](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning#HTTP_pinning),
    [HTTP Strict Transport Security
    (HSTS)](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security)
    and [Content Security Policy
    (CSP)](https://www.owasp.org/index.php/Content_Security_Policy) need
    a special attention in order not to cause any incident. Some real
    cases about to use of secure headers can be seen:

<!-- end list -->

  -
    \- [Secure websites shun HTTP Public Key
    Pinning](http://news.netcraft.com/archives/2016/03/22/secure-websites-shun-http-public-key-pinning.html)
    \- [HTTP Public Key Pinning: You’re doing it
    wrong\!](http://news.netcraft.com/archives/2016/03/30/http-public-key-pinning-youre-doing-it-wrong.html)
    \- [CSP On Reporting and
    Filtering](https://blogs.dropbox.com/tech/2015/09/on-csp-reporting-and-filtering/)
    \- [Content Security Policy
    (CSP)](https://developer.chrome.com/extensions/contentSecurityPolicy)

<!-- end list -->

  - Who can be responsible to apply secure features?
    The responsability to provides more secure environment it's a effort
    that envolve developers, system administrators, vendors of web
    browsers and end user.

<!-- end list -->

  -
    Like this the success of secure headers strategy depends of proper
    client, in general a web browser, and web application or some
    infrastructure component configured appropriately.

<!-- end list -->

  - How can I apply secure http headers?
    The use of secure headers can occur directly through of handling
    http response headers or using some framework, in addition to
    conducting appropriate configuration in web server.

<!-- end list -->

  -
    The OWASP: Secure Headers project provides a list of resources and
    examples to help understand, analyze and configure secure headers.

<!-- end list -->

  - What's the costs relative to apply this actions?
    There's no costs in to use secure headers. However some effort to
    configure and manage properly configuration will be necessary.

# Acknowledgements

## Contributors

OWASP Secure Headers Project is developed by a worldwide team of
volunteers. The primary contributors to date have been:

  - [Ricardo Iramar](https://www.owasp.org/index.php/User:Riramar)
  - [Jim Manico](https://www.owasp.org/index.php/User:Jmanico)
  - [Alexandre
    Menezes](https://www.owasp.org/index.php/Special:Contributions/Amenezes)

# Road Map and Getting Involved

Involvement in the development and promotion of OWASP Secure Headers
Project is actively encouraged\! You do not have to be a security expert
in order to contribute. If you want to help send an email to
<ricardo.iramar@owasp.org>.

## To Do

  - Perform public to scan websites and view stats regarding these
    headers. Automated scanning of the top 1m sites on the web;
    filtering of said sites to view stats across industries and
    countries; published database dumps for public consumption/tools;
    scanning of individual sites; comparing multiple scanned sites.
  - Consistent reports regarding this secure headers, their usage, any
    changes to existing headers.
  - Reorganize "Best Practices" tab and include a section for related
    security best practices around headers (e.g. "Remove Server Header"
    and "Remove X-Powered-By Header").
  - Create a parser to grab the headers from <https://scans.io> and
    populate the MySQL database.

## Doing

  - Producing open source, easily implemented, well documented code
    libraries that enable these headers for a variety of platforms.
    We'll prioritize creating and publicizing Node.JS, PHP, Ruby, and
    Java, but will eventually reach out towards edge cases like Go,
    Python and others. The key is to make this accessible as possible to
    developers.
  - Including how to set properly secure headers on IIS.
  - Improve constantly hsecscan tool to detect bad practices and provide
    link to the best practices above.

## Done

  - Creating secure best practices implementations including how to set
    properly secure headers on the most common platforms (eg. Apache,
    NGINX and Lighttpd).
  - Divide the "Tools_and_Libraries" tab into two differents tab
    (Scanners and Libraries).
  - Include link to attack pages.
  - Include Top Websites Examples tab.
  - Move the Best Practices to another tab.
  - Include a new tab only for browser versions compatibility.
  - Include X-Permitted-Cross-Domain-Policies under Headers and Best
    Practices tab.
  - Include Expect-CT header and update HPKP.
  - Include Feature-Policy.

__NOTOC__ <headertabs></headertabs>

[Category:OWASP Project](Category:OWASP_Project "wikilink")
