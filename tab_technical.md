---
title: technical
displaytext: Technical Resources
layout: null
tab: true
order: 4
tags: headers
---

# Technical Resources

📚 This section provides a list of tools as well as documents to understand, analyze, develop and administer HTTP secure headers to help achieving more secure and trustworthy web systems.

* 📺 [Presentations](#presentations)
* 🏭 [Analysis Tools](#analysis-tools)
* 👩‍💻 [Development Libraries](#development-libraries)
  * [DotNet](#dotnet)
  * [Go](#go)
  * [HAPI](#hapi)
  * [Java](#java)
  * [NodeJS](#nodejs)
  * [PHP](#php)
  * [Python](#python)
  * [Ruby](#ruby)
  * [Rust](#rust)

## Presentations

* [Trap bad guys in your browser with HTTP security headers](https://speakerdeck.com/righettod/trap-bad-guys-in-your-browser-with-http-security-headers).

## Analysis Tools

| Tool | Description | Ref |
| --- | --- | --- |
| **hsecscan** | A security scanner for HTTP response headers. | [👩‍💻](https://github.com/riramar/hsecscan) |
| **humble** | A humble, and fast, security-oriented HTTP headers analyzer. | [👩‍💻](https://github.com/rfc-st/humble) |
| **SecurityHeaders.com** | There are services out there that will analyze the HTTP response headers of other sites but I also wanted to add a rating system to the results. The HTTP response headers that this site analysis provides huge levels of protection and it's important that sites deploy them. Hopefully, by providing an easy mechanism to assess them, and further information on how to deploy missing headers, we can drive up the usage of security based headers across the web. | [🌎](https://securityheaders.com/) |
| **Mozilla Observatory** | A Mozilla project designed to help developers, system administrators, and security professionals configure their sites safely and securely. | [🌎](https://observatory.mozilla.org/) / [👩‍💻](https://github.com/mozilla/http-observatory/) / [👩‍💻](https://github.com/mozilla/http-observatory-website/) |
| **Recx Security Analyser** | Chrome extension that allows the inspection of security aspects of a site's HTTP headers, cookies and other key security settings. | [🌎](https://chrome.google.com/webstore/detail/recx-security-analyser/ljafjhbjenhgcgnikniijchkngljgjda) |
| **testssl.sh** | Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML. | [👩‍💻](https://github.com/drwetter/testssl.sh) |
| **DrHEADer** | DrHEADer helps with the audit of security headers received in response to a single request or a list of requests. | [👩‍💻](https://github.com/Santandersecurityresearch/DrHeader) |
| **csp-evaluator** | NPM module allowing developers and security experts to check if a Content Security Policy serves as a strong mitigation against XSS attacks. | [👩‍💻](https://github.com/google/csp-evaluator) |

## Development Libraries

### Java

| Library | Description | Ref |
| --- | --- | --- |
| **Spring Security** | Spring Security's support for adding various security headers to the response. | [🌎](https://docs.spring.io/spring-security/reference/features/exploits/headers.html) |

### DotNet

| Library | Description | Ref |
| --- | --- | --- |
| **NWebsec** | NWebsec consists of several security libraries for ASP.NET applications. | [🌎](https://docs.nwebsec.com) |
| **NetEscapades.AspNetCore.SecurityHeaders** | Small package to allow adding security headers to ASP.NET Core websites. | [👩‍💻](https://github.com/andrewlock/NetEscapades.AspNetCore.SecurityHeaders) |
| **OwaspHeaders.Core** | .NET Core middleware for injecting the OWASP recommended HTTP Headers for increased security | [👩‍💻](https://github.com/GaProgMan/OwaspHeaders.Core) |

### Ruby

| Library | Description | Ref |
| --- | --- | --- |
| **secure_headers** | Security related headers all in one gem. | [👩‍💻](https://github.com/github/secure_headers) |

### PHP

| Library | Description | Ref |
| --- | --- | --- |
| **SecureHeaders** | A PHP class aiming to make the use of browser security features more accessible. | [👩‍💻](https://github.com/aidantwoods/SecureHeaders) |
| **secure-headers** | PHP Secure Headers for Laravel and non-Laravel projects. | [👩‍💻](https://github.com/bepsvpt/secure-headers) |

### NodeJS

| Library | Description | Ref |
| --- | --- | --- |
| **helmet** | Module to help secure Express apps with various HTTP headers. | [👩‍💻](https://github.com/helmetjs/helmet) |
| **ember-cli-content-security-policy** | This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file. | [👩‍💻](https://github.com/rwjblue/ember-cli-content-security-policy/) |

### HAPI

| Library | Description | Ref |
| --- | --- | --- |
| **blankie** | A CSP plugin for hapi. | [👩‍💻](https://github.com/nlf/blankie) |

### Python

| Library | Description | Ref |
| --- | --- | --- |
| **django-csp and django-security** | Content Security Policy for Django. A collection of models, views, middlewares, and forms to help secure a Django project. | [👩‍💻](https://github.com/mozilla/django-csp) / [👩‍💻](https://github.com/sdelements/django-security) |
| **Secweb** | Secweb is a pack of security middlewares for fastApi and starlette server it includes CSP, HSTS, and many more. | [👩‍💻](https://github.com/tmotagam/Secweb) |

### Go

| Library | Description | Ref |
| --- | --- | --- |
| **helmet** | HTTP security middleware for Go(lang) inspired by HelmetJS. | [👩‍💻](https://github.com/goddtriffin/helmet) |

### Rust

| Library | Description | Ref |
| --- | --- | --- |
| **owasp-headers** | Best-practice OWASP HTTP response headers for Rust. | [🌎](https://docs.rs/crate/owasp-headers/latest) |
