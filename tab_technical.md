---
title: technical
displaytext: Technical Resources
layout: null
tab: true
order: 3
tags: headers
---

# Technical Resources

This section provides a list of tools as well as documents to understand, analyze, develop and administer HTTP secure headers to help achieving more secure and trustworthy web systems.

* [Presentations](#presentations)
* [Analysis Tools](#analysis-tools)
* [Development Libraries](#development-libraries)
* [Operation Tools](#operation-tools)
* [Miscellaneous Hints](#miscellaneous-hints)

## Presentations

* [Trap bad guys in your browser with HTTP security headers](https://speakerdeck.com/righettod/trap-bad-guys-in-your-browser-with-http-security-headers).

## Analysis Tools

### hsecscan

A security scanner for HTTP response headers.

**GitHub:** <https://github.com/riramar/hsecscan>

### humble

A humble, and fast, security-oriented HTTP headers analyzer.

**GitHub:** <https://github.com/rfc-st/humble>

### headers

Python script to get some response headers from Alexa top sites files and store in a MySQL database.

**GitHub:** <https://github.com/oshp/headers/>

### SecurityHeaders.com

There are services out there that will analyze the HTTP response headers of other sites but I also wanted to add a rating system to the results. The HTTP response headers that this site analysis provides huge levels of protection and it's important that sites deploy them. Hopefully, by providing an easy mechanism to assess them, and further information on how to deploy missing headers, we can drive up the usage of security based headers across the web.

**Site:** <https://securityheaders.com/>

### Mozilla Observatory

A Mozilla project designed to help developers, system administrators, and security professionals configure their sites safely and securely.

**Site:** <https://observatory.mozilla.org/>

**GitHub:** <https://github.com/mozilla/http-observatory/>

**GitHub:** <https://github.com/mozilla/http-observatory-website/>

### Recx Security Analyser

Chrome extension that allows the inspection of security aspects of a site's HTTP headers, cookies and other key security settings.

**Site:** <https://chrome.google.com/webstore/detail/recx-security-analyser/ljafjhbjenhgcgnikniijchkngljgjda>

### testssl.sh

Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML.

**GitHub:** <https://github.com/drwetter/testssl.sh>

### DrHEADer

DrHEADer helps with the audit of security headers received in response to a single request or a list of requests.

**GitHub:** <https://github.com/Santandersecurityresearch/DrHeader>

### API-Security

This is a Python based API-Security framework containing ApiSecurityHeader.py script which will check the above-mentioned Security response headers are present and contains the required value.

**GitHub:** <https://github.com/AmitKulkarni9/API-Security>

### csp-evaluator

NPM module allowing developers and security experts to check if a Content Security Policy serves as a strong mitigation against XSS attacks.

**GitHub:** <https://github.com/google/csp-evaluator>

## Development Libraries

### Java

#### Spring Security

Spring Security’s support for adding various security headers to the response.

**Site:** <https://docs.spring.io/spring-security/reference/features/exploits/headers.html>

### .NET

#### NWebsec

NWebsec consists of several security libraries for ASP.NET applications.

**Site:** <https://docs.nwebsec.com>

#### NetEscapades.AspNetCore.SecurityHeaders

Small package to allow adding security headers to ASP.NET Core websites.

**GitHub**: <https://github.com/andrewlock/NetEscapades.AspNetCore.SecurityHeaders>

### Ruby

#### secure_headers

Security related headers all in one gem.

**GitHub:** <https://github.com/github/secure_headers>

### PHP

#### SecureHeaders

A PHP class aiming to make the use of browser security features more accessible.

**GitHub:** <https://github.com/aidantwoods/SecureHeaders>

#### secure-headers

PHP Secure Headers for Laravel and non-Laravel projects.

**GitHub**: <https://github.com/bepsvpt/secure-headers>

### RACK

#### rack-secure_headers

Security related HTTP headers for Rack applications.

**GitHub:** <https://github.com/frodsan/rack-secure_headers>

### NodeJS

#### helmet

Module to help secure Express apps with various HTTP headers.

**GitHub:** <https://github.com/helmetjs/helmet>

#### ember-cli-content-security-policy

This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file.

**GitHub:** <https://github.com/rwjblue/ember-cli-content-security-policy/>

### HAPI

#### blankie

A CSP plugin for hapi.

**GitHub:** <https://github.com/nlf/blankie>

### Python

#### django-csp and django-security

Content Security Policy for Django.

**GitHub:** <https://github.com/mozilla/django-csp>

A collection of models, views, middlewares, and forms to help secure a Django project.

**GitHub:** <https://github.com/sdelements/django-security>

#### Secure

Secure headers for Python web frameworks.

**GitHub:** <https://github.com/TypeError/secure>

### Go

#### helmet

HTTP security middleware for Go(lang) inspired by HelmetJS.

**GitHub:** <https://github.com/goddtriffin/helmet>

### Rust

Best-practice OWASP HTTP response headers for Rust.

**Site:** <https://docs.rs/crate/owasp-headers/latest>

## Operation Tools

### http_hardening

Puppet module to enable, configure and manage secure HTTP headers on web servers.

**Supported Web Servers:**

* Apache HTTP Server
* NGINX
* Lighttpd

**GitHub:** <https://github.com/amenezes/http_hardening>  

**Puppet Forge:** <https://forge.puppet.com/amenezes/http_hardening>

## Miscellaneous Hints

### Convert a Permissions-Policy back to Feature-Policy

As the [Permissions-Policy](https://github.com/w3c/webappsec-permissions-policy/blob/main/permissions-policy-explainer.md) header is still in development and is [not yet well supported](https://caniuse.com/permissions-policy), it can be interesting to use the two formats to increase the coverage of browsers according to their support level for **Permissions-Policy** and **[Feature-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy)** policy headers.

The following _python3_ code snippet can be useful to achieve such conversion.

📑 Source for the conversion rules was this [one](https://github.com/w3c/webappsec-permissions-policy/blob/main/permissions-policy-explainer.md#appendix-big-changes-since-this-was-called-feature-policy).

💻 Code snippet:

```python
permissions_policy = 'fullscreen=(), geolocation=(self "https://game.com" "https://map.example.com"), gyroscope=(self), usb=*'
feature_policy_directives = []
# Collect directives
permissions_policy_directives = permissions_policy.split(",")
# Process each directive
for permissions_policy_directive in permissions_policy_directives:
    # Remove leading and trailing spaces
    directive = permissions_policy_directive.strip(" ")
    # Remove all double quotes
    directive = directive.replace("\"", "")
    # Replace disabling expression () by the corresponding one in Feature-Policy
    directive = directive.replace("()", "'none'")
    # Quote keywords: self
    directive = directive.replace("self", "'self'")
    # Replace the equals affectation character by a space
    directive = directive.replace("=", " ")
    # Remove parenthesis
    directive = directive.replace("(", "").replace(")", "")
    # Add the current directive to the collection
    feature_policy_directives.append(directive)
# Convert the collection of directives to a string with ; as directives separator
feature_policy = "; ".join(feature_policy_directives)
print(feature_policy)
```

💻 Execution example:

```shell
$ python code.py
fullscreen 'none'; geolocation 'self' https://game.com https://map.example.com; gyroscope 'self'; usb *
```

### Test locally a Content-Security-Policy for weaknesses

It can be interesting to validate locally a **Content-Security-Policy** for presence of weaknesses prior to apply it on deployed web applications.

The following _JavaScript_ code snippet can be useful to achieve such validation by leveraging the [csp-evaluator](https://github.com/google/csp-evaluator) NPM module provided by Google.

💻 Code snippet:

```javascript
import {CspEvaluator} from "csp_evaluator/dist/evaluator.js";
import {CspParser} from "csp_evaluator/dist/parser.js";

const args = process.argv.slice(2)
if(args.length == 0){
    console.error("[!] Missing CSP!");
}else{
    const csp = args[0]
    console.info(`[+] CSP to evaluate:\n${csp}`);
    const parsed = new CspParser(csp).csp;
    console.info(`[+] Evaluation results:`);
    const results = new CspEvaluator(parsed).evaluate();
    results.forEach(elt => {
        let info = `[Directive '${elt.directive}' - Severity ${elt.severity}]: ${elt.description}`;
        console.info(info);
    });
}
```

💻 Execution example:

```shell
$ node code.js "default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content"
[+] CSP to evaluate:
default-src 'self'; object-src 'none'; frame-ancestors 'none'; upgrade-insecure-requests; block-all-mixed-content
[+] Evaluation results:
[Directive 'default-src' - Severity 50]: 'self' can be problematic if you host JSONP, Angular or user uploaded files.
```
