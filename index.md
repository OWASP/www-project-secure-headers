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

![OSHP Logo](assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)

[![External Links Validity Check](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml)

[![Update headers reference JSON files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml)

[![Update monitoring technical references dashboard](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml)

[![Perform_monitoring_oshp_site_references](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml)

[![update_tab_stats_related_files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/tab-stats-headers-generate-related-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/tab-stats-headers-generate-related-files.yml)

🎯 The **OWASP Secure Headers Project** (also called **OSHP**) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

🤔 HTTP headers are well known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

📚 The OWASP Secure Headers Project aim to provide elements about the following aspects regarding HTTP security headers:

* [Guidance](https://owasp.org/www-project-secure-headers/index.html#div-bestpractices_configuration-proposal) about the recommended HTTP security headers that can be leveraged.
* [Guidance](https://owasp.org/www-project-secure-headers/index.html#div-bestpractices_prevent-information-disclosure-via-http-headers) about the HTTP headers that should be removed.
* [Tools](https://github.com/oshp/oshp-validator) to validate an HTTP security header configuration.
* [Code](https://owasp.org/www-project-secure-headers/index.html#div-technical) libraries that can be leveraged to configure recommended HTTP security headers.
* [Statistics](https://github.com/oshp/oshp-stats) about usage of the recommended HTTP security headers.

🏭 All the tools provided by the OSHP are gathered under this [GitHub organization](https://github.com/oshp/).

📺 A presentation of the project is available on the following locations:

* [OWASP Spotlight Youtube playlists](https://www.youtube.com/watch?v=N4F3VWQYU9E).
* [Application Security Podcast Youtube playlists](https://www.youtube.com/watch?v=0SNU9clVhKU).
* [NoLimitSecu Podcast](https://www.nolimitsecu.fr/owasp-secure-headers-project/) (*French*).

## Migration

🌎 The OWASP Secure Headers Project was migrated from the [old website](https://wiki.owasp.org/index.php/OWASP_Secure_Headers_Project) to the [GitHub OWASP organization](https://github.com/OWASP/www-project-secure-headers).

📦 The following projects are now **archived**, they are initiatives that are now replaced by new projects:

* [headers](https://github.com/oshp/headers).
* [headers-ui-container](https://github.com/oshp/headers-ui-container).

## Security headers usage statistics

📈 We provide statistics, updated every month, about HTTP response security headers usage mentioned by the OWASP Secure Headers Project:

* They are available through [this GitHub project](https://github.com/oshp/oshp-stats) and the tab named [Statistics](https://owasp.org/www-project-secure-headers/index.html#div-statistics).

## Security headers usage validator

✅ We provide a [venom](https://github.com/ovh/venom) tests suite to validate an HTTP security response header configuration against OWASP Secure Headers Project recommendation:

* It is available through [this GitHub project](https://github.com/oshp/oshp-validator).

🧪 We also provide a *online mock endpoint* returning an HTTP response, for which, all HTTP response headers recommended by the OSHP will be set:

* It is automatically deployed on `https://oshp-validator-mock.onrender.com`
* Technical details about this endpoint are [here](https://github.com/oshp/oshp-validator#tests-suite-mock-service).

## Security headers reference files

📖 As mentioned in previous sections, we provide the collection of HTTP response security headers to add as well as HTTP response headers to remove, both in table form.

💡 Additionally, we provide this information as two JSON files to enable automation in the context of a provisioning workflow:

* Collection of [HTTP response security headers to add](ci/headers_add.json).
* Collection of [HTTP response headers to remove](ci/headers_remove.json).

📡 These json files are automatically updated.

## Technical references health dashboard

📍 We automatically generate and monitor this **[dashboard](https://github.com/OWASP/www-project-secure-headers/blob/master/monitoring_technical_references_dashboard.md)** to identify any dead project referenced in the **[Technical Resources](https://owasp.org/www-project-secure-headers/#div-technical)** tab.

## Discussions, information and roadmap

💬 We use the GitHub [discussions feature](https://github.com/OWASP/www-project-secure-headers/discussions) for discussions about the project as well as spreading global information about it.

👩‍💻 The work on the OSHP projects and associated components is tracked using the GitHub [project feature](https://github.com/orgs/OWASP/projects/44).

## Create a link to the OSHP site

📖 This is documented into the **[Case Studies](https://owasp.org/www-project-secure-headers/index.html#div-casestudies)** tab.

## Contributors

💌 Contributors to OSHP, before the migration of the project to [GitHub](https://github.com/OWASP/www-project-secure-headers):

* [Alexandre Menezes](mailto:alexandre.fmenezes@owasp.org)
* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://github.com/jmanico)

💌 Visit this [page](https://github.com/OWASP/www-project-secure-headers/graphs/contributors) for updated information about the contributors since the migration of the project to GitHub.

## Licensing

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
