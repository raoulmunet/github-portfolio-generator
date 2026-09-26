from __future__ import annotations
from dataclasses import dataclass
import json
import os
from urllib.parse import quote
from urllib.request import Request, urlopen

@dataclass(frozen=True)
class Repo:
    name: str
    html_url: str
    description: str | None
    language: str | None
    stars: int
    homepage: str | None
    updated_at: str
    fork: bool

def fetch_repos(username: str, token: str | None = None) -> list[Repo]:
    token = token or os.getenv('GITHUB_TOKEN')
    page = 1
    out = []
    while True:
        url = 'https://api.github.com/users/' + quote(username) + '/repos?per_page=100&page=' + str(page) + '&sort=updated'
        headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'github-portfolio-generator'}
        if token:
            headers['Authorization'] = 'Bearer ' + token
        with urlopen(Request(url, headers=headers), timeout=20) as response:
            data = json.load(response)
        if not data:
            break
        for x in data:
            out.append(Repo(x['name'], x['html_url'], x.get('description'), x.get('language'), x.get('stargazers_count', 0), x.get('homepage'), x.get('updated_at', ''), x.get('fork', False)))
        if len(data) < 100:
            break
        page += 1
    return out

def render_markdown(username: str, repos: list[Repo], prefix: str | None = None, include_forks: bool = False) -> str:
    selected = [r for r in repos if (include_forks or not r.fork) and (not prefix or r.name.startswith(prefix))]
    selected.sort(key=lambda r: r.updated_at, reverse=True)
    out = ['# ' + username + ' — GitHub Portfolio', '', 'Projects: ' + str(len(selected)), '']
    for r in selected:
        out += ['## ' + r.name, '', r.description or '_No repository description provided._', '', '- Language: ' + (r.language or 'Not specified'), '- Stars: ' + str(r.stars), '- Repository: ' + r.html_url]
        if r.homepage:
            out.append('- Demo / homepage: ' + r.homepage)
        out.append('')
    return '\n'.join(out).rstrip() + '\n'
