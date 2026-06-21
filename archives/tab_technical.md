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
  * [Java](#java)
  * [NodeJS](#nodejs)
  * [PHP](#php)
  * [Python](#python)
  * [Ruby](#ruby)
  * [Swift](#swift)
  * [Rust](#rust)

## Presentations

* [Trap bad guys in your browser with HTTP security headers](https://speakerdeck.com/righettod/trap-bad-guys-in-your-browser-with-http-security-headers).
* [How the Content-Security-Policy HTTP response header can save your romantic evening?](https://speakerdeck.com/righettod/how-the-content-security-policy-http-response-header-can-save-your-romantic-evening)

## Analysis Tools

| Tool | Description | Ref |
| --- | --- | --- |
| **hsecscan** | A security scanner for HTTP response headers. | [👩‍💻](https://github.com/riramar/hsecscan) |
| **humble** | A humble, and fast, security-oriented HTTP headers analyzer. | [👩‍💻](https://github.com/rfc-st/humble) |
| **testssl.sh** | Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML. | [👩‍💻](https://github.com/drwetter/testssl.sh) |
| **DrHEADer** | DrHEADer helps with the audit of security headers received in response to a single request or a list of requests. | [👩‍💻](https://github.com/Santandersecurityresearch/DrHeader) |
| **csp-evaluator** | NPM module allowing developers and security experts to check if a Content Security Policy serves as a strong mitigation against XSS attacks. | [👩‍💻](https://github.com/google/csp-evaluator) |
| **mdn-http-observatory** | Service by Mozilla that checks web sites for security-relevant headers. | [👩‍💻](https://github.com/mdn/mdn-http-observatory) |
| **shcheck** | A basic tool to check security headers of a website. | [👩‍💻](https://github.com/santoru/shcheck) |

## Development Libraries

### Java

| Library | Description | Ref |
| --- | --- | --- |
| **Spring Security** | Spring Security's support for adding various security headers to the response. | [🌎](https://docs.spring.io/spring-security/reference/features/exploits/headers.html) |

### DotNet

| Library | Description | Ref |
| --- | --- | --- |
| **NetEscapades.AspNetCore.SecurityHeaders** | Small package to allow adding security headers to ASP.NET Core websites. | [👩‍💻](https://github.com/andrewlock/NetEscapades.AspNetCore.SecurityHeaders) |
| **OwaspHeaders.Core** | .NET Core middleware for injecting the OWASP recommended HTTP Headers for increased security | [👩‍💻](https://github.com/GaProgMan/OwaspHeaders.Core) |

### Ruby

| Library | Description | Ref |
| --- | --- | --- |
| **secure_headers** | Security related headers all in one gem. | [👩‍💻](https://github.com/github/secure_headers) |

### PHP

| Library | Description | Ref |
| --- | --- | --- |
| **secure-headers** | PHP Secure Headers for Laravel and non-Laravel projects. | [👩‍💻](https://github.com/bepsvpt/secure-headers) |
| **laravel-csp** | Package to set content security policy headers in a Laravel app. | [👩‍💻](https://github.com/spatie/laravel-csp) |
| **security-headers** | Provides an implementation for configuring HTTP security headers in web applications developed in PHP (Spanish). | [👩‍💻](https://github.com/OWASP/www-project-randomized-header-channel-for-csrf-protection/tree/main/resources/security-headers) |

### NodeJS

| Library | Description | Ref |
| --- | --- | --- |
| **helmet** | Module to help secure Express apps with various HTTP headers. | [👩‍💻](https://github.com/helmetjs/helmet) |
| **ember-cli-content-security-policy** | This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file. | [👩‍💻](https://github.com/rwjblue/ember-cli-content-security-policy/) |
| **Next.js** | Next.js's support for adding various security headers to the response. | [🌎](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers) |

### Python

| Library | Description | Ref |
| --- | --- | --- |
| **django-csp and django-security** | Content Security Policy for Django. A collection of models, views, middlewares, and forms to help secure a Django project. | [👩‍💻](https://github.com/mozilla/django-csp) / [👩‍💻](https://github.com/sdelements/django-security) |
| **Secweb** | Secweb is a pack of security middlewares for fastApi and starlette server it includes CSP, HSTS, and many more. | [👩‍💻](https://github.com/tmotagam/Secweb) |
| **secure** | Lightweight library to add security headers to Django, Flask, FastAPI, and more. | [👩‍💻](https://github.com/TypeError/secure) |

### Go

| Library | Description | Ref |
| --- | --- | --- |
| **secure** | HTTP middleware for Go that facilitates some quick security wins. | [👩‍💻](https://github.com/unrolled/secure) |

### Swift

| Library | Description | Ref |
| --- | --- | --- |
| **VaporSecurityHeaders** | A Middleware library for adding security headers to your Vapor application. | [👩‍💻](https://github.com/brokenhandsio/VaporSecurityHeaders) |

### Rust

| Library | Description | Ref |
| --- | --- | --- |
| **rust-helmet** | HTTP security headers middleware for multiple Rust web frameworks. | [👩‍💻](https://github.com/danielkov/rust-helmet) |
