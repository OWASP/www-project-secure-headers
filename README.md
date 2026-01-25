> [!IMPORTANT]
> The OWASP Foundation has decided to migrate its content to a new CMS. As a result, OSHP content is frozen for the duration of the migration. You can find more information and explanations [here](https://github.com/OWASP/www-project-secure-headers/discussions/273).

![OSHP Logo](assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)

# Introduction

📦 This repository contains all the content of the **OWASP Secure Headers Project** (also named **OSHP**).

🎯 The OSHP describes HTTP response headers that your application can use to increase the security of your application. Once set, these HTTP response headers can restrict modern browsers from running into easily preventable vulnerabilities. The OSHP intends to raise awareness and use of these headers.

# OSHP ecosystem

🗺️ The OSHP project is composed of the following projects:

* **Main site**: It is the core of the OSHP and provide the information about HTTP security headers
  * Called `mainsite`.
* **Validator**: Venom tests suite to validate an HTTP security response headers configuration against OSHP recommendation.
  * Called `validator`.
* **Statistics**: Statistics about HTTP response security headers usage mentioned by the OSHP.
  * Called `statistics`.

## Repository structure

> [!TIP]
> 🔬[Technical References Dashboard](monitoring_technical_references_dashboard.md).

* The base of the repository contains the **main site**.
* The other projects are stored in the folder [subprojects](subprojects/): Each sub projects have it own folder.
* The folder [ci](ci) (**CI** for **C**ontinuous **I**ntegration) contains materials to generate the following content.
  * Generation of the both JSON files containing the header recommended to add and remove:
    * Processing is performed by this GitHub action [workflow](.github/workflows/mainsite_headers-generate-json-files.yml) every time the file [tab_bestpractices.md](tab_bestpractices.md) is modified.
  * Generation of the [markdown file](monitoring_technical_references_dashboard.md) with the update health state of all GitHub repositories mentioned in the tab named **[Technical](tab_technical.md)**:
    * Processing is performed by this GitHub action [workflow](.github/workflows/mainsite_monitoring-technical-references-generate-dashboard.yml) every week with a cron expression indicating `At 00:00 on Sunday` or every time the file [tab_technical.md](tab_technical.md) is modified.
  * Generation of the file [tab_statistics.md](tab_statistics.md) as well as [all related PNG files](assets/tab_stats_generated_images):
    * Processing is performed by this GitHub action [workflow](.github/workflows/mainsite_tab-stats-headers-generate-related-files.yml) every month with a cron expression indicating `At 00:00 on day-of-month 5` or every time any of the following files is modified:
      * [ci/tab_stats_manage_generation.sh](ci/tab_stats_manage_generation.sh).
      * [ci/tab_stats_generate_md_file.py](ci/tab_stats_generate_md_file.py).
      * [ci/tab_stats_generate_png_files.sh](ci/tab_stats_generate_png_files.sh).
      * The specified cron expression was selected because the database containing the data used by the script [tab_stats_generate_md_file.py](ci/tab_stats_generate_md_file.py) is updated on the first day of each month by this [workflow](.github/workflows/statistics_update-datasource.yml).
* The project official logo is stored into the folder [logo](logo) as well as into the [OWASP Swag](https://github.com/OWASP/owasp-swag) GitHub repository.

## Issue and discussions

💬 Both are handled using the following GitHub features:

* [Issues](https://github.com/OWASP/www-project-secure-headers/issues).
* [Discussions](https://github.com/OWASP/www-project-secure-headers/discussions).

## Content editor

👩‍💻 Content editing is done with [Visual Studio Code](https://code.visualstudio.com/).

📦 A [workspace file](project.code-workspace) is provided with [recommended extensions](.vscode/extensions.json).

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

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](LICENSE.txt).
