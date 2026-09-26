from __future__ import annotations
import argparse
from pathlib import Path
from .core import fetch_repos, render_markdown

def main(argv=None):
    p = argparse.ArgumentParser(description='Generate a Markdown GitHub portfolio.')
    p.add_argument('username')
    p.add_argument('--prefix')
    p.add_argument('--include-forks', action='store_true')
    p.add_argument('--output')
    a = p.parse_args(argv)
    text = render_markdown(a.username, fetch_repos(a.username), a.prefix, a.include_forks)
    if a.output:
        Path(a.output).write_text(text, encoding='utf-8')
    else:
        print(text, end='')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
