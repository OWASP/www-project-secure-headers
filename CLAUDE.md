# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is the content repository for the **OWASP Secure Headers Project (OSHP)**, published at <https://owasp.org/secure-headers-project/>. It is a **documentation project**, not an application: there is no build step, no test suite to run, and no server to start. The bulk of the work here is editing Markdown content and the small set of Python/Bash scripts that generate derived files from that content via GitHub Actions.

## Repository structure

* `mainsite/` — the core site content, numbered Markdown files rendered as tabs on the OWASP site (`00_index.md` through `10_monitoring_technical_references_dashboard.md`). This is excluded from Jekyll processing by `_config.yml` and instead consumed by the OWASP CMS.
* `subprojects/validator/` — a [Venom](https://github.com/ovh/venom) test suite (`tests_suite.yml`) that validates a live site's HTTP security response headers against OSHP recommendations, plus a mock endpoint (`test_suite_mock.py`) deployed at `https://oshp-validator-mock.onrender.com` used to test the suite itself.
* `subprojects/statistics/` — Python scripts (`scripts/gather_data.py`, `scripts/generate_stats_md_file.py`) that build a SQLite dataset (`data/data.db`) of HTTP security header usage across the Majestic Top 1M sites list, published as GitHub Release assets and consumed by `ci/stats_manage_generation.sh`.
* `ci/` — standalone Python/Bash scripts run by GitHub Actions workflows to generate or validate content (see below). Scripts here import shared constants from `ci/common.py`.
* `.github/workflows/` — the GitHub Actions workflows that drive nearly all repo automation.
* `archives/` — historical/retired content, not actively maintained.
* `logo/` — official project logo assets (also mirrored in the OWASP swag repo).

## Content generation pipeline (important: derived files must not be hand-edited)

Several files in `mainsite/` and `ci/` are **generated from other Markdown files** by CI scripts and committed back by a bot (`GHActionBot`). When editing content, know which file is the source of truth:

* `ci/headers_add.json` and `ci/headers_remove.json` are generated from the tables in `mainsite/03_best_practices.md`, delimited by HTML comment markers `<!-- HEADERS_ADD_TABLE_START/END -->` and `<!-- HEADERS_REMOVE_TABLE_START/END -->`. Source of truth: `mainsite/03_best_practices.md`. Regenerate with:

  ```bash
  cd ci && python headers_generate_json_files.py
  ```

* `mainsite/10_monitoring_technical_references_dashboard.md` is generated from the GitHub repo links in `mainsite/04_technical_resources.md` (queries the GitHub API for each repo's last-push date). Source of truth: `mainsite/04_technical_resources.md`. Regenerate with:

  ```bash
  cd ci && python monitoring_technical_references_generate_dashboard.py [github_token]
  ```

* `mainsite/07_statistics.md` and the pie-chart images under `mainsite/assets/tab_stats_generated_images/` are generated from `subprojects/statistics/data/data.db` via `ci/stats_manage_generation.sh`, which calls `ci/stats_generate_md_file.py` then `ci/stats_generate_png_files.sh` (Mermaid CLI, config in `ci/stats_mermaid_config.json`). Do not hand-edit `07_statistics.md`.

Because of this, if you edit `mainsite/03_best_practices.md` or `mainsite/04_technical_resources.md`, mention that the corresponding generated file(s)/workflow will pick up the change on the next push (the workflows below trigger on `paths:` matching these source files) rather than manually editing the generated output.

## Common commands

Install script dependencies (top-level scripts under `ci/`):

```bash
pip install -r requirements.txt
```

Validate all external links in every Markdown file in the repo (mirrors `mainsite_validate_external-links.yml`; config is `markdown-link-check_config.json`; a link can be marked `[text](url "SKIP_VALIDATION")` to skip it):

```bash
python ./ci/validate_md_links.py -c markdown-link-check_config.json
```

Check that "Case Studies" sites still mention OSHP (needs `pip install requests playwright` and `playwright install --with-deps chromium`):

```bash
cd ci && python monitoring_oshp_site_references.py [github_token]
```

Lint the Venom test suite:

```bash
cd subprojects/validator && yamllint --strict tests_suite.yml
```

Run the Venom validator test suite against a target site:

```bash
cd subprojects/validator
venom run --var="target_site=https://mysite.com" --var="logout_url=/logout" tests_suite.yml
```

Run it against the hosted mock endpoint (what CI does):

```bash
cd subprojects/validator
venom run --var="target_site=https://oshp-validator-mock.onrender.com" --var="logout_url=/" tests_suite.yml
```

Re-align Markdown table column widths in a file (repo-root helper script, no dependencies):

```bash
python pad-md-tables.py mainsite/03_best_practices.md
```

## Markdown conventions

* Every `mainsite/*.md` page starts with the shared top navigation link line, kept as `TOP_NAVIGATION_LINKS` in `ci/common.py` — keep it in sync if a page is added/renamed/reordered.
* `.markdownlint.json` disables `MD013` (line length), `MD033` (inline HTML), `MD025` (multiple H1s), `MD059` (descriptive link text), and `MD024` (duplicate headings) — don't "fix" these in existing content.
* Tables that are consumed by generation scripts (see markers above) must keep their pipe-delimited column structure intact; use `pad-md-tables.py` after editing to keep columns visually aligned rather than reformatting by hand.
* A link can opt out of external-link validation with the `"SKIP_VALIDATION"` title marker, e.g. `[Duck Duck Go](https://duckduckgo.com "SKIP_VALIDATION")`.
* **Rule: after modifying any `.md` file, always run `python pad-md-tables.py <path/to/file.md>` on it before finishing the task**, so table columns stay vertically aligned. Run it from the repo root, once per modified Markdown file.

## Custom Claude Code commands

* `/validate-md-content <markdown-file>` (`.claude/commands/validate-md-content.md`) — checks a Markdown file for spelling/grammar errors, markdown syntax problems, invalid technical statements, and broken pipe-table column counts, then reports findings by line number. It is read-only (`allowed-tools: Read, Glob, Grep`) and does not edit the file, in keeping with the GenAI usage rule below.

## Ownership

`.github/CODEOWNERS` routes all `*.md` PRs to `@riramar` (Ricardo Iramar) — Dominique Righetto (this repo's usual operator) does not have write access and works via PRs like any other contributor.

## Usage of GenAI (strict — see README.md "Usage of GenIA")

The project restricts GenAI/assistant use to these cases only:

* Correcting spelling and grammar errors in English.
* Technical assistance with script development or proof-of-concepts (POCs).
* Brainstorming to generate ideas for the OSHP project.
* Searching for technical documentation.
* Validating our understanding of the technical aspects of a header.

Content is authored by a human; GenAI acts only as an assistant. Concretely: do not author new `mainsite/*.md` prose content (header descriptions, best-practice guidance, case studies, etc.) wholesale — propose edits/suggestions for the human to review and commit, and prefer fixing spelling/grammar, scripts/POCs, and research over drafting original project content. If a request falls outside these cases, say so and ask before proceeding.

**Hard rule: never author or directly draft the technical description, security rationale, or recommended configuration text for an HTTP header that would get published** (this applies especially to `mainsite/01_headers.md` and `mainsite/03_best_practices.md`). A human must write and vouch for that content; only help research or validate it (e.g. point out sources, sanity-check claims, flag inconsistencies) rather than producing the prose yourself.
