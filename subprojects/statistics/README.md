# OWASP Secure Headers Project Statistics

📊 [Statistics](https://owasp.org/www-project-secure-headers/index.html#div-statistics) about HTTP response security headers usage mentioned by the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) (OSHP).

💾 This project gather data, about the usage of HTTP response security headers, into a [SQLITE database](data/data.db) to allow the generation of statistics in a second time.

💡 See this [issue](https://github.com/OWASP/www-project-secure-headers/issues/61) for details.

# Data source

> [!TIP]
> 💡 MAJESTIC was used instead of the **CISCO Top 1 million sites CSV file** because it contain less malware domains.

* [MAJESTIC Top 1 million sites list](https://blog.majestic.com/development/majestic-million-csv-daily/).
* [CISCO Top 1 million sites CSV file](http://s3-us-west-1.amazonaws.com/umbrella-static/index.html).

The `gather_data.py` script will automatically download and parse the Majestic CSV if `data/input.csv` is not present.

# Scripts

> [!NOTE]
> 📦 They are all stored in the [scripts](scripts) folder and they are Python 3.x based.

> [!IMPORTANT]
> ⚠️ Usage of the script [generate_stats_md_file](scripts/generate_stats_md_file.py) was replaced by a [workflow](../../.github/workflows/mainsite_generate_stats-related-files.yml) on the main OSHP site.

💻 [Visual Studio Code](https://code.visualstudio.com/) is used for the scripts development. A Visual Studio Code [workspace file](../../project.code-workspace) is provided for the project with [recommended extensions](../../.vscode/extensions.json).

📑 Files:

* [gather_data](scripts/gather_data.py): Script gathering the information about HTTP security headers usage in a [SQLITE database](data/data.db) based on the "MAJESTIC Top 1 million sites CSV file" data source.
* [generate_stats_md_file](scripts/generate_stats_md_file.py): Script using the gathered data to generate/update the markdown file [stats](stats.md), with [mermaid pie charts](https://mermaid-js.github.io/mermaid/#/pie) with differents statistics about HTTP security headers usage (⚠️**not used anymore**).

# Data

> [!NOTE]
> 📦 During execution, these files are generated and stored locally in the `data` folder. For distribution, they are published as GitHub Release assets attached to this repository.

📑 Files:

* `input.csv`: MAJESTIC Top 1 million sites list formated as one entry `ranking,domain` by line.
* `data.db`: SQLITE database with information about HTTP security headers usage.

# Data and statistics update

> [!NOTE]
> 💡 Only the first **250000** entries of the CSV datasource are used to fit the processing timeframe allowed for a github action workfows using the free tiers.

💻 The update is scheduled in the following way:

1. The **first day** of every month the database is updated via this [workflow](../../.github/workflows/statistics_generate_datasource.yml).
2. Once the data database is updated then the statistic data is updated via this [workflow](../../.github/workflows/mainsite_generate_stats-related-files.yml).

# Note

* [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) can be used to access to the raw data of the [SQLITE DB](data/data.db).
