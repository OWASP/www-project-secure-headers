---
title: casestudies
displaytext: Case Studies
layout: null
tab: true
order: 8
tags: headers
---

# Case Studies

📋 This section list the entities referencing the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/).

📩 Feel free to contact project leaders if your company or software (open source or not) was using the OSHP project.

🔎 **Google dork** used to identity references was `allintext:"OWASP Secure Headers Project" -site:owasp.org -site:github.com -site:youtube.com -site:twitter.com -site:linkedin.com`.

## How to create a link to the OSHP site?

🌎 Use the following absolute URL syntax to create a reference link to a specific location of the OSHP site. The presence of the `index.html` file is mandatory otherwise any anchor specified is not effective:

```text
https://owasp.org/www-project-secure-headers/index.html#[TAB-ID]_[HEADER-ID-INSIDE-TAB]
```

💡 Where:

* `[TAB-ID]`: ID of the tab that can be obtained with the link to it.
* `[HEADER-ID-INSIDE-TAB]`: Href value of the link to the section inside the tab.

👀 Example of reference link to the section about the header **Clear-Site-Data** in the **Response Headers** tab:

```text
https://owasp.org/www-project-secure-headers/index.html#div-headers_clear-site-data
```

👀 Example of reference link to the section **PHP** in the **Technical Resources** tab:

```text
https://owasp.org/www-project-secure-headers/index.html#div-technical_php
```

## Company

* [Cloud.gov](https://cloud.gov/docs/management/headers/).
* [Amazon AWS](https://docs.aws.amazon.com/whitepapers/latest/secure-content-delivery-amazon-cloudfront/improving-security-by-enabling-security-specific-headers.html).
* [Salesforce](https://help.salesforce.com/s/articleView?language=en_US&id=cc.b2c_declarative_security_via_http_headers.htm&type=5).
* [Black Hills Information Security](https://www.blackhillsinfosec.com/fixing-content-security-policies-with-cloudflare-workers/).
* [Progress](https://www.progress.com/documentation/sitefinity-cms/110/predefined-security-headers-in-http-response).
* [Bloomreach](https://documentation.bloomreach.com/14/library/concepts/security/configure-security-response-headers.html).
* [Tableau](https://help.tableau.com/current/server-linux/en-us/security_http_headers.htm).
* [42Crunch](https://docs.42crunch.com/latest/content/extras/protection_security_headers.htm).
* [SAP](https://help.sap.com/docs/SAP_UPSCALE_COMMERCE/4620dd88ff9047c89ffb7fa897207a46/30af09ca9e394505a85661fa530d1263.html).
* [SecureAuth](https://docs.secureauth.com/2104/en/identity-platform-http-security-header-best-practices.html).
* [Detectify](https://support.detectify.com/support/solutions/articles/48001048949-https-stripping).
* [ImmuniWeb](https://www.immuniweb.com/websec/about).
* [Zoom](https://developers.zoom.us/docs/zoom-apps/security/owasp/).
* [NexusGuard](https://blog.nexusguard.com/hardening-web-applications-using-secure-http-headers).
* [VeraCode](https://docs.veracode.com/r/enable-security-headers).
* [Ivanti](https://forums.ivanti.com/s/article/HTTP-Security-Headers-X-Frame-Options-X-XSS-Protection-X-Content-Type-Options).

## Software

* [Nmap](https://github.com/nmap/nmap/blob/master/scripts/http-security-headers.nse).
* [Spring Security](https://docs.spring.io/spring-security/reference/features/exploits/headers.html).
