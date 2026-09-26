# github-portfolio-generator

[![tests](https://github.com/raoulmunet/github-portfolio-generator/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/github-portfolio-generator/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Generate a clean Markdown developer portfolio from public GitHub repositories.

> **Oracle compatibility:** Not applicable. This tool consumes GitHub repository metadata and is database-agnostic.

## Features

- fetches public repositories for a GitHub username
- ignores forks by default
- sorts by recent activity
- includes description, primary language, stars and homepage/demo link
- filters repositories by prefix, for example `ora-`
- outputs ready-to-publish Markdown
- supports `GITHUB_TOKEN` for higher GitHub API rate limits

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/github-portfolio-generator.git"
github-portfolio-generator raoulmunet
github-portfolio-generator raoulmunet --prefix ora- --output oracle-tools.md
```

## Authentication

Public repository access works without a token. For higher API limits:

```bash
export GITHUB_TOKEN=...
github-portfolio-generator raoulmunet
```

The token is read from the environment and is never written to generated output.

## Scope

This tool produces a factual portfolio from GitHub metadata. It does not invent project claims, skill levels or descriptions that are absent from the repositories.

## Related portfolio tools

- [Oracle Dev Tools](https://github.com/raoulmunet?tab=repositories&q=ora-&type=source) — the Oracle-focused tool suite.
- [repo-readme-architect](https://github.com/raoulmunet/repo-readme-architect) — bootstrap repository documentation from project structure.
- [github-portfolio-generator](https://github.com/raoulmunet/github-portfolio-generator) — build a factual Markdown portfolio from GitHub metadata.

## License

MIT.
