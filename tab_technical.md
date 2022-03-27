---
title: technical
displaytext: Technical Resources
layout: null
tab: true
order: 3
tags: headers
---

# Technical Resources

This section covers a list of tools to analyze, develop and administrate HTTP secure headers to help achieve more secure and trustworthy web systems.

## Analysis Tools

### hsecscan

A security scanner for HTTP response headers.

**Github:** <https://github.com/riramar/hsecscan>

### headers

Python script to get some response headers from Alexa top sites file and store in a MySQL database.

**Github:** <https://github.com/oshp/headers/>

### SecurityHeaders.com

There are services out there that will analyse the HTTP response headers of other sites but I also wanted to add a rating system to the results. The HTTP response headers that this site analyses provide huge levels of protection and it's important that sites deploy them. Hopefully, by providing an easy mechanism to assess them, and further information on how to deploy missing headers, we can drive up the usage of security based headers across the web.

**Site:** <https://securityheaders.com/>

### Mozilla Observatory

A Mozilla project designed to help developers, system administrators, and security professionals configure their sites safely and securely.

**Site:** <https://observatory.mozilla.org/>

**Github:** <https://github.com/mozilla/http-observatory/>

**Github:** <https://github.com/mozilla/http-observatory-website/>

### Recx Security Analyser

Chrome extension that allows the inspection of security aspects of a site's HTTP headers, cookies and other key security settings.

**Site:** <https://chrome.google.com/webstore/detail/recx-security-analyser/ljafjhbjenhgcgnikniijchkngljgjda>

### testssl.sh

Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML.

**Github:** <https://github.com/drwetter/testssl.sh>

### DrHEADer

DrHEADer helps with the audit of security headers received in response to a single request or a list of requests.

**Github:** <https://github.com/Santandersecurityresearch/DrHeader>

### API-Security

This is a Python based API-Security framework containing ApiSecurityHeader.py script which will check the above mentioned Security response headers are present and contains the required value.

**Github:** <https://github.com/AmitKulkarni9/API-Security>

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

**Github**: <https://github.com/andrewlock/NetEscapades.AspNetCore.SecurityHeaders>

### Ruby

#### secure_headers

Security related headers all in one gem.

**Github:** <https://github.com/github/secure_headers>

### PHP

#### SecureHeaders

A PHP class aiming to make the use of browser security features more accessible.

**Github:** <https://github.com/aidantwoods/SecureHeaders>

#### secure-headers

PHP Secure Headers for Laravel and non-Laravel projects.

**Github**: <https://github.com/bepsvpt/secure-headers>

### RACK

#### rack-secure_headers

Security related HTTP headers for Rack applications.

**Github:** <https://github.com/frodsan/rack-secure_headers>

### NodeJS

#### helmet

Module to help secure Express apps with various HTTP headers.

**Github:** <https://github.com/helmetjs/helmet>

#### ember-cli-content-security-policy

This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file.

**Github:** <https://github.com/rwjblue/ember-cli-content-security-policy/>

### HAPI

#### blankie

A CSP plugin for hapi.

**Github:** <https://github.com/nlf/blankie>

### Python

#### django-csp and django-security

Content Security Policy for Django.

**Github:** <https://github.com/mozilla/django-csp>

A collection of models, views, middlewares, and forms to help secure a Django project.

**Github:** <https://github.com/sdelements/django-security>

#### Secure

Secure headers for Python web frameworks.

**Github:** <https://github.com/TypeError/secure>

### Go

#### helmet

HTTP security middleware for Go(lang) inspired by HelmetJS.

**Github:** <https://github.com/goddtriffin/helmet>

### Rust

Best-practice OWASP HTTP response headers for Rust.

**Site:** <https://docs.rs/crate/owasp-headers/latest>

## Operation Tools

### http_hardening

Puppet module to enable, configure and manage secure http headers on web servers.

**Supported Web Servers:**

- Apache HTTP Server
- NGINX
- Lighttpd

**Github:** <https://github.com/amenezes/http_hardening>  

**Puppet Forge:** <https://forge.puppet.com/amenezes/http_hardening>
