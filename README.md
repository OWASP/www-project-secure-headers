# OWASP Secure Headers Project

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)
[![External Links Validity Check](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml)
[![Update headers reference JSON files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml)
[![Update monitoring technical references dashboard](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml) [![Perform_monitoring_oshp_site_references](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml)

🎯 The **OWASP Secure Headers Project** (also named **OSHP**) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

## Introduction

📚 HTTP headers are well known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

📚 We aim to publish reports on header usage stats, developments and changes, code libraries that make these headers easily accessible to developers on a range of platforms, and data sets concerning the general usage of these headers.

🌐 The OWASP Secure Headers Project was migrated to a [new OWASP website](https://owasp.org/www-project-secure-headers/).

📁 You can still access the old website [here](https://wiki.owasp.org/index.php/OWASP_Secure_Headers_Project).

## Logo

🎨 The project official logo is stored into the folder [logo](logo) as well as into the [OWASP Swag](https://github.com/OWASP/owasp-swag) GitHub repository.

## Issue and discussions

💬 Both are handled using the following GitHub features:

* [Issues](https://github.com/OWASP/www-project-secure-headers/issues).
* [Discussions](https://github.com/OWASP/www-project-secure-headers/discussions).

## Content editor

👩‍💻 Content editing is done with [Visual Studio Code](https://code.visualstudio.com/).

A [workspace file](project.code-workspace) is provided with [recommended extensions](.vscode/extensions.json).

## Automatically generated content

🏭 The folder [ci](ci) (**CI** for **C**ontinuous **I**ntegration) contains materials to generate the following content.

📝 Generate the both JSON files containing the header recommended to add and remove:

* Generation is performed by this GitHub action [workflow](.github/workflows/headers-generate-json-files.yml) every time the file [tab_bestpractices.md](tab_bestpractices.md) is modified.

📝 Generate the [markdown file](monitoring_technical_references_dashboard.md) with the update health state of all GitHub repositories mentioned in the tab named **[Technical](tab_technical.md)**:

* Generation is performed by this GitHub action [workflow](.github/workflows/monitoring-technical-references-generate-dashboard.yml) every time the file [tab_technical.md](tab_technical.md) is modified.

## Social media communication

📩 This template is used to announce news on social media about OSHP update:

```text
📡 OWASP Secure Headers Project: [MESSAGE].

#appsec #appsecurity #oshp

[PRINT_SCREEN_IN_PNG_FORMAT_WHEN_APPLICABLE]

📖 [LINK_TO_OSHP_SECTION]

💡 Source used:

[LINK_TO_SOURCE_USED]
```

## Contributors

💌 Contributors to OSHP, before the migration of the project to [GitHub](https://github.com/OWASP/www-project-secure-headers):

* [Alexandre Menezes](mailto:alexandre.fmenezes@owasp.org)
* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://github.com/jmanico)

💌 Visit this [page](https://github.com/OWASP/www-project-secure-headers/graphs/contributors) for updated information about the contributors since the migration of the project to GitHub.

## Licensing

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
