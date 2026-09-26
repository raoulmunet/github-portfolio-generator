# github-portfolio-generator

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

## License

MIT.
