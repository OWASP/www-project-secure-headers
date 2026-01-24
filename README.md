> [!IMPORTANT]
> The OWASP Foundation has decided to migrate its content to a new CMS. As a result, OSHP content is frozen for the duration of the migration. You can find more information and explanations [here](https://github.com/OWASP/www-project-secure-headers/discussions/273).

# OWASP Secure Headers Project

![OSHP Logo](assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)

[![External Links Validity Check](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/check-external-links.yml)

[![Update headers reference JSON files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/headers-generate-json-files.yml)

[![Update monitoring technical references dashboard](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-technical-references-generate-dashboard.yml)

[![Perform_monitoring_oshp_site_references](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/monitoring-oshp-site-references.yml)

[![update_tab_stats_related_files](https://github.com/OWASP/www-project-secure-headers/actions/workflows/tab-stats-headers-generate-related-files.yml/badge.svg?branch=master)](https://github.com/OWASP/www-project-secure-headers/actions/workflows/tab-stats-headers-generate-related-files.yml)

🎯 The **OWASP Secure Headers Project** (also named **OSHP**) describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OWASP Secure Headers Project intends to raise awareness and use of these headers.

## Introduction

📚 HTTP headers are well known and also despised. Seeking a balance between usability and security, developers implement functionality through the headers that can make applications more versatile or secure. But in practice how are the headers being implemented? What sites follow the best implementation practices? Big companies, small, all or none?

## Description

📚 We aim to publish reports on header usage stats, developments and changes, code libraries that make these headers easily accessible to developers on a range of platforms, and data sets concerning the general usage of these headers.

🌍 The OWASP Secure Headers Project was migrated to a [new OWASP website](https://owasp.org/www-project-secure-headers/).

## Logo

🎨 The project official logo is stored into the folder [logo](logo) as well as into the [OWASP Swag](https://github.com/OWASP/owasp-swag) GitHub repository.

## Issue and discussions

💬 Both are handled using the following GitHub features:

* [Issues](https://github.com/OWASP/www-project-secure-headers/issues).
* [Discussions](https://github.com/OWASP/www-project-secure-headers/discussions).

## Content editor

👩‍💻 Content editing is done with [Visual Studio Code](https://code.visualstudio.com/).

📦 A [workspace file](project.code-workspace) is provided with [recommended extensions](.vscode/extensions.json).

## Automatically generated content

> [!TIP]
> 🔬[Technical References Dashboard](monitoring_technical_references_dashboard.md).

🏭 The folder [ci](ci) (**CI** for **C**ontinuous **I**ntegration) contains materials to generate the following content.

📝 Generation of the both JSON files containing the header recommended to add and remove:

* Processing is performed by this GitHub action [workflow](.github/workflows/headers-generate-json-files.yml) every time the file [tab_bestpractices.md](tab_bestpractices.md) is modified.

📝 Generation of the [markdown file](monitoring_technical_references_dashboard.md) with the update health state of all GitHub repositories mentioned in the tab named **[Technical](tab_technical.md)**:

* Processing is performed by this GitHub action [workflow](.github/workflows/monitoring-technical-references-generate-dashboard.yml) every week with a cron expression indicating `At 00:00 on Sunday` or every time the file [tab_technical.md](tab_technical.md) is modified.

📝 Generation of the file [tab_statistics.md](tab_statistics.md) as well as [all related PNG files](assets/tab_stats_generated_images):

* Processing is performed by this GitHub action [workflow](.github/workflows/tab-stats-headers-generate-related-files.yml) every month with a cron expression indicating `At 00:00 on day-of-month 5` or every time any of the following files is modified:
  * [ci/tab_stats_manage_generation.sh](ci/tab_stats_manage_generation.sh).
  * [ci/tab_stats_generate_md_file.py](ci/tab_stats_generate_md_file.py).
  * [ci/tab_stats_generate_png_files.sh](ci/tab_stats_generate_png_files.sh).
* The specified cron expression was selected because the database containing the data used by the script [tab_stats_generate_md_file.py](ci/tab_stats_generate_md_file.py) is updated on the first day of each month by the project [oshp-stats](https://github.com/oshp/oshp-stats/):
  * See [here](https://github.com/oshp/oshp-stats/blob/main/.github/workflows/update-datasource.yml) for technical details.

## Social media communication

📩 This template is used to announce news on social media about OSHP update:

```text
📡 OWASP Secure Headers Project: [MESSAGE].

#appsec #appsecurity #owasp_shp

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
