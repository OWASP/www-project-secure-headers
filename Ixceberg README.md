# Ixceberg Secure Headers Project
-----------
[![OWASP Lab](https://img.shields.io/badge/owasp-lab%20project-f7b73c.svg)](https://www.owasp.org/projects)
[![External Links Validity Check](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml)
[![Update headers reference JSON files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml)
[![Update monitoring technical references dashboard](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml)

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

💬 Both are handled with this dedicated [project](https://github.com/oshp/oshp-tracking):

* [Issues](https://github.com/oshp/oshp-tracking/issues).
* [Discussions](https://github.com/oshp/oshp-tracking/discussions).

## Content editor

👩‍💻 Content editing is done with [Visual Studio Code](https://code.visualstudio.com/).

A [workspace file](project.code-workspace) is provided with [recommended extensions](.vscode/extensions.json).

## Automatically generated content

🏭 The folder [ci](ci) (**CI** for **C**ontinuous **I**ntegration) contains materials to generate the following content.

📝 Generate the both JSON files containing the header recommended to add and remove:

* Generation is performed by this GitHub action [workflow](.github/workflows/headers-generate-json-files.yml) every time the file [tab_bestpractices.md](tab_bestpractices.md) is modified.

📝  Generate the [markdown file](monitoring_technical_references_dashboard.md) with the update health state of all GitHub repositories mentioned in the tab named **[Technical](tab_technical.md)**:

* Generation is performed by this GitHub action [workflow](.github/workflows/monitoring-technical-references-generate-dashboard.yml) every time the file [tab_technical.md](tab_technical.md) is modified.

## Contributors

* [IcebergVerse](https://github.com/IcebergVerse)
* [Iceberg_i19](https://twitter.com/Iceberg_i19)

## Licensing

📑 **OWASP Secure Headers Project** is free to use. It is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
