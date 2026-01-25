# OWASP Secure Headers Project statistics

[![Gather data](https://github.com/oshp/oshp-stats/actions/workflows/update-datasource.yml/badge.svg?branch=main)](https://github.com/oshp/oshp-stats/actions/workflows/update-datasource.yml)

📊 [Statistics](https://owasp.org/www-project-secure-headers/index.html#div-statistics) about HTTP response security headers usage mentioned by the [OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) (OSHP).

💾 This project gather data, about the usage of HTTP response security headers, into a [SQLITE database](data/data.db) to allow the generation of statistics in a second time.

💡 See this [issue](https://github.com/OWASP/www-project-secure-headers/issues/61) for details.

# Data source

> [!TIP]
> 💡 MAJESTIC was used instead of the **CISCO Top 1 million sites CSV file** because it contain less malware domains.

* [MAJESTIC Top 1 million sites list](https://blog.majestic.com/development/majestic-million-csv-daily/).
* [CISCO Top 1 million sites CSV file](http://s3-us-west-1.amazonaws.com/umbrella-static/index.html).

```bash
# Download the MAJESTIC Top 1 million sites CSV file
$ wget http://downloads.majestic.com/majestic_million.csv
# Transform the downloaded file to an input source that use the same format 
# than the CISCO Top 1 million sites CSV file
$ cat majestic_million.csv | awk -F  "," 'NR>1 {print $1 "," $3}' > data/input.csv
$ rm majestic_million.csv
```

# Scripts

> [!NOTE]
> 📦 They are all stored in the [scripts](scripts) folder and they are Python 3.x based.

> [!IMPORTANT]
> ⚠️ Usage of the script [generate_stats_md_file](scripts/generate_stats_md_file.py) was replaced by a [workflow](https://github.com/OWASP/www-project-secure-headers/blob/master/.github/workflows/tab-stats-headers-generate-related-files.yml) on the main OSHP site..

💻 [Visual Studio Code](https://code.visualstudio.com/) is used for the scripts development. A Visual Studio Code [workspace file](project.code-workspace) is provided for the project with [recommended extensions](.vscode/extensions.json).

📑 Files:

* [gather_data](scripts/gather_data.py): Script gathering the information about HTTP security headers usage in a [SQLITE database](data/data.db) based on the "MAJESTIC Top 1 million sites CSV file" data source.
* [generate_stats_md_file](scripts/generate_stats_md_file.py): Script using the gathered data to generate/update the markdown file [stats](stats.md), with [mermaid pie charts](https://mermaid-js.github.io/mermaid/#/pie) with differents statistics about HTTP security headers usage (⚠️**not used anymore**).

# Data

> [!NOTE]
> 📦 They are all stored in the [data](data) folder.

📑 Files:

* [input.csv](data/input.csv): MAJESTIC Top 1 million sites list formated as one entry `ranking,domain` by line.
* [data.db](data/data.db): SQLITE database with information about HTTP security headers usage.

# Data and statistics update

> [!NOTE]
> 💡 Only the first **150000** entries of the CSV datasource are used to fit the processing timeframe allowed for a github action workfows using the free tiers.

💻 The update is scheduled in the following way:

* The **first day** of every month the data database is updated via this [workflow](.github/workflows/update-datasource.yml).
* The **fifth day** of every month the statistic data is updated via this [workflow](https://github.com/OWASP/www-project-secure-headers/blob/master/.github/workflows/tab-stats-headers-generate-related-files.yml).

# Note

* [DB Browser for SQLite](https://github.com/sqlitebrowser/sqlitebrowser) can be used to access to the raw data of the [SQLITE DB](data/data.db).
