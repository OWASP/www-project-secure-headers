[Index](00_index.md) | [Response Headers](01_headers.md) | [Browser Support](02_browser_support.md) | [Best Practices](03_best_practices.md) | [Technical Resources](04_technical_resources.md) | [Code Snippets](05_code_snippets.md) | [Miscellaneous](06_misc.md) | [Statistics](07_statistics.md) | [Case Studies](08_case_studies.md) | [Logo](09_logo.md) | [Monitoring Technical References Dashboard](10_monitoring_technical_references_dashboard.md)

---

## Introduction

![OSHP Logo](assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/righettod/toolbox-pentest-web)

🎯 The **OWASP Secure Headers Project** (also called **OSHP**) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

🤔 HTTP headers are well known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

📚 The OWASP Secure Headers Project aim to provide elements about the following aspects regarding HTTP security headers:

* Guidance about the recommended HTTP security headers that can be leveraged (**[best practices](03_best_practices.md)** section).
* Guidance about the HTTP headers that should be removed (**[best practices](03_best_practices.md)** section).
* [Tools](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator) to validate an HTTP security header configuration.
* Code libraries that can be leveraged to configure recommended HTTP security headers (**[technical resources](04_technical_resources.md)** section).
* [Statistics](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/statistics) about usage of the recommended HTTP security headers (**[statistics](07_statistics.md)** section).

📺 A presentation of the project is available on the following locations:

* [OWASP Spotlight Youtube playlists](https://www.youtube.com/watch?v=N4F3VWQYU9E).
* [Application Security Podcast Youtube playlists](https://www.youtube.com/watch?v=0SNU9clVhKU).
* [NoLimitSecu Podcast](https://www.nolimitsecu.fr/owasp-secure-headers-project/) (*French*).

## Security headers usage statistics

📈 We provide statistics, updated every month, about HTTP response security headers usage mentioned by the OWASP Secure Headers Project:

* They are available through [this subproject](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/statistics) and the **[statistics](07_statistics.md)** section.

## Security headers usage validator

✅ We provide a [venom](https://github.com/ovh/venom) tests suite to validate an HTTP security response header configuration against *OWASP Secure Headers Project* recommendation:

* It is available through [this subproject](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator).

🧪 We also provide a *online mock endpoint* returning an HTTP response, for which, all HTTP response headers recommended by the OSHP will be set:

* It is automatically deployed on `https://oshp-validator-mock.onrender.com`
* Technical details about this endpoint are [here](https://github.com/OWASP/www-project-secure-headers/tree/master/subprojects/validator#tests-suite-mock-service).

## Security headers reference files

📖 As mentioned in previous sections, we provide the collection of HTTP response security headers to add as well as HTTP response headers to remove, both in table form.

💡 Additionally, we provide this information as two JSON files to enable automation in the context of a provisioning workflow:

* Collection of [HTTP response security headers to add](../ci/headers_add.json).
* Collection of [HTTP response headers to remove](../ci/headers_remove.json).

📡 These json files are automatically updated.

## Technical references health dashboard

📍 We automatically generate and monitor this **[dashboard](10_monitoring_technical_references_dashboard.md)** to identify any dead project referenced in the **[technical resources](04_technical_resources.md)** section.

## Discussions, information and roadmap

💬 We use the GitHub [discussions feature](https://github.com/OWASP/www-project-secure-headers/discussions) for discussions about the project as well as spreading global information about it.

👩‍💻 The work on the OSHP projects and associated components is tracked using the GitHub [project feature](https://github.com/orgs/OWASP/projects/44).

## Create a link to the OSHP site

📖 This is documented into the **[case studies](08_case_studies.md)** section.

## Project leaders

🧑‍💻 [Ricardo Iramar](mailto:ricardo.iramar@owasp.org)

🧑‍💻 [Dominique Righetto](mailto:dominique.righetto@owasp.org)

## Contributors

💌 Contributors to OSHP, before the migration of the project to [GitHub](https://github.com/OWASP/www-project-secure-headers):

* [Alexandre Menezes](mailto:alexandre.fmenezes@owasp.org)
* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://github.com/jmanico)

💌 Visit this [page](https://github.com/OWASP/www-project-secure-headers/graphs/contributors) for updated information about the contributors since the migration of the project to GitHub.

## Licensing

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
