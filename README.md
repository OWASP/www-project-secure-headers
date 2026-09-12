![OSHP Logo](mainsite/assets/images/oshp_logo.png)

[![OWASP Production](https://img.shields.io/badge/owasp-production%20project-800080.svg)](https://www.owasp.org/projects)

# Introduction

📦 This repository contains all the content of the **[OWASP Secure Headers Project](https://owasp.org/projects/secure-headers-project)** (also named **OSHP**).

# OSHP Web URL

> ℹ️ The url `https://owasp.org/www-project-secure-headers/` redirect to the *web rendering* url.

* Project page on the OWASP site: <https://owasp.org/projects/secure-headers-project>
* Web rendering of the main site: <https://owasp.github.io/www-project-secure-headers/>

# OSHP ecosystem

🗺️ The OSHP project is composed of the following projects:

* **Main site**: It is the core of the OSHP and provide the information about HTTP security headers.
  * Called `mainsite`.
  * Content is [here](mainsite/).
    * It is **the master data in markdown** and is the content that is updated.
  * Web rendered content is [here](https://owasp.github.io/www-project-secure-headers/) and is based on the **the master data in markdown**.
* **Validator**: Venom tests suite to validate an HTTP security response headers configuration against OSHP recommendation.
  * Called `validator`.
  * Content is [here](subprojects/validator/).
* **Statistics**: Statistics about HTTP response security headers usage mentioned by the OSHP.
  * Called `statistics`.
  * Content is [here](subprojects/statistics/).

# Repository structure

* The base of the repository contains the **main site**.
* The other projects are stored in the folder [subprojects](subprojects/): Each sub projects have it own folder.
* The project official logo is stored into the folder [logo](logo) as well as into the [OWASP Swag](https://github.com/OWASP/owasp-swag) GitHub repository.
* The folder [ci](ci) (**CI** for **C**ontinuous **I**ntegration) contains materials to generate or update content using GitHub actions [workflows](.github/workflows/).

# GitHub actions

📝 The naming convention used is `[project_call_name]_[action]_[target].yml` where:

* `[project_call_name]` is the project call name defined above.
* `[action]` can be `(validate|monitor|generate)`.

🔋 Health status:

|Status|File|
|:---|:---|
|![mainsite_generate_headers-json-files.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_generate_headers-json-files.yml/badge.svg)|[📄](.github/workflows/mainsite_generate_headers-json-files.yml)|
|![mainsite_generate_stats-related-files.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_generate_stats-related-files.yml/badge.svg)|[📄](.github/workflows/mainsite_generate_stats-related-files.yml)|
|![mainsite_generate_technical-references-dashboard.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_generate_technical-references-dashboard.yml/badge.svg)|[📄](.github/workflows/mainsite_generate_technical-references-dashboard.yml)|
|![mainsite_monitor_oshp-site-references.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_monitor_oshp-site-references.yml/badge.svg)|[📄](.github/workflows/mainsite_monitor_oshp-site-references.yml)|
|![mainsite_monitor_oshp-gha-workflows.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_monitor_oshp-gha-workflows.yml/badge.svg)|[📄](.github/workflows/mainsite_monitor_oshp-gha-workflows.yml)|
|![mainsite_validate_external-links.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_validate_external-links.yml/badge.svg)|[📄](.github/workflows/mainsite_validate_external-links.yml)|
|![mainsite_validate_owasp-nest-metadata.yaml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/mainsite_validate_owasp-nest-metadata.yaml/badge.svg)|[📄](.github/workflows/mainsite_validate_owasp-nest-metadata.yaml)|
|![statistics_generate_datasource.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/statistics_generate_datasource.yml/badge.svg)|[📄](.github/workflows/statistics_generate_datasource.yml)|
|![validator_validate_tests-suite.yml](https://github.com/OWASP/www-project-secure-headers/actions/workflows/validator_validate_tests-suite.yml/badge.svg)|[📄](.github/workflows/validator_validate_tests-suite.yml)|

# Issue and discussions

💬 Both are handled using the following GitHub features:

* [Issues](https://github.com/OWASP/www-project-secure-headers/issues).
* [Discussions](https://github.com/OWASP/www-project-secure-headers/discussions).

# Content editor

👩‍💻 Content editing is done with [Visual Studio Code](https://code.visualstudio.com/).

📦 A [workspace file](project.code-workspace) is provided with [recommended extensions](.vscode/extensions.json).

# Social media communication

📩 This template is used to announce news on social media about OSHP update:

```text
📡 OWASP Secure Headers Project: [MESSAGE].

#appsec #appsecurity #owasp_shp

[PRINT_SCREEN_IN_PNG_FORMAT_WHEN_APPLICABLE]

📖 [LINK_TO_OSHP_SECTION]

💡 Source used:

[LINK_TO_SOURCE_USED]
```

# Project leaders

🧑‍💻 [Ricardo Iramar](mailto:ricardo.iramar@owasp.org)

🧑‍💻 [Dominique Righetto](mailto:dominique.righetto@owasp.org)

# Contributors

💌 Contributors to OSHP, before the migration of the project to [GitHub](https://github.com/OWASP/www-project-secure-headers):

* [Alexandre Menezes](mailto:alexandre.fmenezes@owasp.org)
* [Adam Averay](https://github.com/adamaveray)
* [Jim Manico](https://github.com/jmanico)

💌 Visit this [page](https://github.com/OWASP/www-project-secure-headers/graphs/contributors) for updated information about the contributors since the migration of the project to GitHub.

# Licensing

📑 This project content is free to use. It is licensed under the [Apache 2.0 License](LICENSE.txt).

# Usage of GenIA

> [!CAUTION]
> 📍 The content is created by a human, and GenIA is used as an assistant.

## Rules

🧑‍💻 We limit the usage of GenIA models to the following cases:

* Correcting spelling and grammar errors in English.
* Technical assistance with script development or proof-of-concepts (POCs).
* Brainstorming to generate ideas for the OSHP project.
* Searching for technical documentation.
* Validating our understanding of the technical aspects of a header.

⛔ GenIA must never author or directly draft the technical description, security rationale, or recommended configuration text for a header that gets published on the site:

* A human must write and vouch for that content.
* GenIA may only help research or validate it.

## Help commands

* The claude code command [`validate-md-content`](.claude/commands/validate-md-content.md) was created to help validating the content of a markdown file against predefined rules.
  * Usage from a claude session is `/validate-md-content [markdown-file-to-validate]`.
