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

**GitHub:** <https://github.com/mozilla/http-observatory/>

**GitHub:** <https://github.com/mozilla/http-observatory-website/>

### Recx Security Analyser

Chrome extension that allows the inspection of security aspects of a site's HTTP headers, cookies and other key security settings.

**Site:** <https://chrome.google.com/webstore/detail/recx-security-analyser/ljafjhbjenhgcgnikniijchkngljgjda>

### KickOff

While each project you launch may have a different feature set, they often share many of the same performance, SEO and security requirements. This tool aims to automate the process of checking your list of requirements shortly before launch or directly after a deployment.

**Site:** <https://github.com/frickelbruder/kickoff>

### testssl.sh

Easy to use shell script which tests not only SSL/TLS encryption but also checks common headers and analyzes those. Output is screen, JSON, CSV and HTML.

**Site:** <https://github.com/drwetter/testssl.sh>

### DrHEADer

DrHEADer helps with the audit of security headers received in response to a single request or a list of requests.

**Site:** <https://github.com/Santandersecurityresearch/DrHeader>

### API-Security

This is a Python based API-Security framework containing ApiSecurityHeader.py script which will check the above mentioned Security response headers are present and contains the required value.

**Site:** <https://github.com/AmitKulkarni9/API-Security>

### Venom Test Suites

Test suites for [Venom](https://github.com/ovh/venom) checking the presence and the value for the different response headers proposed by the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/).

**GitHub:** <https://gist.github.com/righettod/f63548ebd96bed82269dcc3dfea27056>

## Development Libraries

### secureheaders (Ruby)

Security related headers all in one gem.

**Github:** <https://github.com/twitter/secureheaders>

### Security Header Injection Module (SHIM) (ASP.NET)

SHIM is a HTTP module that provides protection for many vulnerabilities by injecting security-specific HTTP headers into ASP.NET web applications.

**Site:** <https://shim.codeplex.com/>

### Spring Security (Java)

Spring Security’s support for adding various security headers to the response.

**Site:** <https://docs.spring.io/spring-security/site/docs/current/reference/html/headers.html>

### SecureHeaders (PHP)

A PHP class aiming to make the use of browser security features more accessible.

**Site:** <https://github.com/aidantwoods/SecureHeaders>

### rack-secure_headers (Rack)

Security related HTTP headers for Rack applications.

**Site:** <https://github.com/frodsan/rack-secure_headers>

### helmet and hood (Node.js + express)

**Site:** <https://github.com/helmetjs/helmet>
**Site:** <https://github.com/seanmonstar/hood>

### blankie (hapi)

A CSP plugin for hapi.

**Site:** <https://github.com/nlf/blankie>

### NWebsec (ASP.NET)

NWebsec consists of several security libraries for ASP.NET applications.

**Site:** <https://docs.nwebsec.com>

### django-csp + commonware; django-security (Python)

django-csp + commonware; django-security.

**Site:** <https://github.com/mozilla/django-csp>  
**Site:** <https://github.com/jsocol/commonware/>  
**Site:** <https://github.com/sdelements/django-security>

### Secure (Python)

Secure is a lightweight package that adds optional security headers and cookie attributes for Python web frameworks.

**Site:** <https://github.com/cakinney/secure>

### secureheader (Go)

Package secureheader adds some HTTP header fields widely considered to improve safety of HTTP requests.

**Site:** <https://github.com/kr/secureheader>

### secure_headers (Elixir)

This Plug will automatically apply several security headers to the Plug.Conn response. By design SecureHeaders will attempt to apply the most strict security policy. Although, security headers are configurable and are validated to avoid misconfiguration.

**Site:** <https://github.com/anotherhale/secure_headers>

### dropwizard-web-security (Dropwizard)

A bundle for applying default web security functionality to a dropwizard application.

**Site:** <https://github.com/palantir/dropwizard-web-security>

### ember-cli-content-security-policy (Ember.js)

This addon makes it easy to use Content Security Policy (CSP) in your project. It can be deployed either via a Content-Security-Policy header sent from the Ember CLI Express server, or as a meta tag in the index.html file.

**Site:** <https://github.com/rwjblue/ember-cli-content-security-policy/>


## Operation Tools

### http_hardening

Puppet module to enable, configure and manage secure http headers on web servers.

**Supported Web Servers:**

- Apache HTTP Server
- NGINX
- Lighttpd

**Github:** <https://github.com/amenezes/http_hardening>  
**Puppet Forge:** <https://forge.puppet.com/amenezes/http_hardening>
