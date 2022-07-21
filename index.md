---
title: OWASP Secure Headers Project
level: 2
url: https://owasp.org/www-project-secure-headers
type: documentation
layout: col-sidebar
tags: headers
---

## Introduction

[![OWASP Incubator](https://img.shields.io/badge/owasp-incubator-blue.svg)](https://owasp.org/projects)
[![External Links Validity Check](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml)

The OWASP Secure Headers Project (also called OSHP) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

HTTP headers are well-known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

The OWASP Secure Headers Project aim to provide elements about the following aspects regarding HTTP security headers:

* [Guidance](https://owasp.org/www-project-secure-headers/#div-headers) about the recommended HTTP security headers that can be leveraged.
* [Guidance](https://owasp.org/www-project-secure-headers/#div-bestpractices) about the HTTP headers that should be removed.
* [Tools](https://owasp.org/www-project-secure-headers/#div-technical) to validate an HTTP security header configuration.
* [Code](https://owasp.org/www-project-secure-headers/#div-technical) libraries that can be leveraged to configure recommended HTTP security headers.
* [Statistics](https://github.com/oshp/oshp-stats) about usage of the recommended HTTP security headers.
* [REST API](https://github.com/OWASP/www-project-secure-headers/discussions/58) allowing to obtain the recommended configuration for different web server.

All the tools provided by the OSHP are gathered under this [GitHub organization](https://github.com/oshp/).

A presentation of the project is available on the [OWASP Spotlight Youtube playlist](https://www.youtube.com/watch?v=N4F3VWQYU9E).

## Migration

The OWASP Secure Headers Project was migrated from the [old website](https://wiki.owasp.org/index.php/OWASP_Secure_Headers_Project) to the [GitHub OWASP organization](https://github.com/OWASP/www-project-secure-headers).

The following projects are now **archived**, they are initiatives that are now replaced by new projects:

* [headers](https://github.com/oshp/headers).
* [headers-ui-container](https://github.com/oshp/headers-ui-container).

## Security headers usage statistics

We provide statistics, updated every month, about HTTP response security headers usage mentioned by the OWASP Secure Headers Project.

They are available through [this GitHub project](https://github.com/oshp/oshp-stats).

## Security headers usage validator

We provide a [venom](https://github.com/ovh/venom) tests suite to validate an HTTP security response header configuration against OWASP Secure Headers Project recommendation.

It is available through [this GitHub project](https://github.com/oshp/oshp-validator).

## Discussions and information

We use the GitHub [discussions](https://github.com/OWASP/www-project-secure-headers/discussions) area for discussions about the project as well as spreading global information about it.

## Contributors

* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://twitter.com/manicode)

## Licensing

OWASP Secure Headers is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
