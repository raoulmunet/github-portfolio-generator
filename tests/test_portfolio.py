from github_portfolio_generator import Repo, render_markdown

def test_filter_and_forks():
    repos = [
        Repo('ora-impact', 'https://github.com/u/ora-impact', 'Impact', 'Python', 2, None, '2026-09-26T10:00:00Z', False),
        Repo('forked', 'https://github.com/u/forked', None, None, 0, None, '2026-09-25T10:00:00Z', True),
    ]
    text = render_markdown('u', repos, prefix='ora-')
    assert 'ora-impact' in text
    assert 'forked' not in text
