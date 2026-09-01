---
description: Validate the content of a markdown file.
argument-hint: [markdown-file-to-validate]
allowed-tools: Read, Glob, Grep
---

Perform the following processing steps against the markdown file passed in parameter:

**Step 1** - Verify that the file is a markdown file, if it not the case then end the processing.

**Step 2** - Validate the following aspects:

* Spelling and grammar errors in English.
* Correct syntax of the markdown.
* Absence of invalid technical statement.
* For any pipe-delimited table in the file: every row (including the header and separator rows) has the same number of columns as the header row. Flag any row with a missing or extra `|`-delimited cell, since a broken column count in `mainsite/03_best_practices.md` would break the header JSON generation scripts in `ci/`.
* For every fenced code block (opening ` ``` ` fence): it must specify a language identifier or the literal word `text` when no specific language applies. Flag any opening fence that has no identifier at all.

**Step 3** - Report the findings as a list, one entry per finding, each with: the line number, the aspect it relates to (spelling/grammar, markdown syntax, technical statement, table structure, or code fence), and a one-sentence description of the issue. If no issues are found, state that explicitly instead of returning an empty response.

Always stricly follow the rules defined in the section **Usage of GenIA** of the file **README.md** located at the root folder of the project.
