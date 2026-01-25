---
title: OWASP Secure Headers Project
level: 3.5
url: https://owasp.org/www-project-secure-headers
type: documentation
layout: col-sidebar
tags: headers
pitch: Provides technical information about HTTP security headers.
---

<script crossorigin="anonymous" type="application/javascript" src="assets/js/direct-link-handler.js"></script>
<link rel="stylesheet" href="assets/css/styles.css">

## Introduction

> ⚠️ **IMPORTANT**: The OWASP Foundation has decided to migrate its content to a new CMS. As a result, OSHP content is frozen for the duration of the migration. You can find more information and explanations [here](https://github.com/OWASP/www-project-secure-headers/discussions/273).

![OSHP Logo](assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)

🎯 The **OWASP Secure Headers Project** (also called **OSHP**) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

🤔 HTTP headers are well known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

📚 The OWASP Secure Headers Project aim to provide elements about the following aspects regarding HTTP security headers:

* Guidance about the recommended HTTP security headers that can be leveraged (**Best Practices** tab).
* Guidance about the HTTP headers that should be removed (**Best Practices** tab).
* [Tools](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator) to validate an HTTP security header configuration.
* Code libraries that can be leveraged to configure recommended HTTP security headers (**Technical Resources** tab).
* [Statistics](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/statistics) about usage of the recommended HTTP security headers (**Statistics** tab).

📺 A presentation of the project is available on the following locations:

* [OWASP Spotlight Youtube playlists](https://www.youtube.com/watch?v=N4F3VWQYU9E).
* [Application Security Podcast Youtube playlists](https://www.youtube.com/watch?v=0SNU9clVhKU).
* [NoLimitSecu Podcast](https://www.nolimitsecu.fr/owasp-secure-headers-project/) (*French*).

## Security headers usage statistics

📈 We provide statistics, updated every month, about HTTP response security headers usage mentioned by the OWASP Secure Headers Project:

* They are available through [this subproject](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/statistics) and the tab named **Statistics**.

## Security headers usage validator

✅ We provide a [venom](https://github.com/ovh/venom) tests suite to validate an HTTP security response header configuration against OWASP Secure Headers Project recommendation:

* It is available through [this subproject](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator).

🧪 We also provide a *online mock endpoint* returning an HTTP response, for which, all HTTP response headers recommended by the OSHP will be set:

* It is automatically deployed on `https://oshp-validator-mock.onrender.com`
* Technical details about this endpoint are [here](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator#tests-suite-mock-service).

## Security headers reference files

📖 As mentioned in previous sections, we provide the collection of HTTP response security headers to add as well as HTTP response headers to remove, both in table form.

💡 Additionally, we provide this information as two JSON files to enable automation in the context of a provisioning workflow:

* Collection of [HTTP response security headers to add](https://github.com/OWASP/www-project-secure-headers/blob/master/ci/headers_add.json).
* Collection of [HTTP response headers to remove](https://github.com/OWASP/www-project-secure-headers/blob/master/ci/headers_remove.json).

📡 These json files are automatically updated.

## Technical references health dashboard

📍 We automatically generate and monitor this **[dashboard](https://github.com/OWASP/www-project-secure-headers/blob/master/monitoring_technical_references_dashboard.md)** to identify any dead project referenced in the **Technical Resources** tab.

## Discussions, information and roadmap

💬 We use the GitHub [discussions feature](https://github.com/OWASP/www-project-secure-headers/discussions) for discussions about the project as well as spreading global information about it.

👩‍💻 The work on the OSHP projects and associated components is tracked using the GitHub [project feature](https://github.com/orgs/OWASP/projects/44).

## Create a link to the OSHP site

📖 This is documented into the **Case Studies** tab.

## Contributors

💌 Contributors to OSHP, before the migration of the project to [GitHub](https://github.com/OWASP/www-project-secure-headers):

* [Alexandre Menezes](mailto:alexandre.fmenezes@owasp.org)
* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://github.com/jmanico)

💌 Visit this [page](https://github.com/OWASP/www-project-secure-headers/graphs/contributors) for updated information about the contributors since the migration of the project to GitHub.

## Licensing

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
