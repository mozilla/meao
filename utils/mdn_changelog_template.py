#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates the Kuma Report Template. Requires 3rd-party libraries
requests and requests_cache, and the Client ID and Secret from
your GitHub OAuth app. Usage:

kuma_report_template.py <client_id> <client_secret> > _drafts/kuma_report.md
"""
from __future__ import unicode_literals, print_function
from argparse import ArgumentParser
from cgi import escape
from collections import defaultdict, Counter, OrderedDict
from datetime import date, datetime, timedelta
from textwrap import wrap
import pprint
import re
import sys

try:
    import requests
    import requests_cache
except ImportError:
    print("*** Requires requests and requests_cache ***")
    raise

# Owner / Repository -> Friendly name
repos = {
    ('mozilla', 'kuma'): 'Kuma',
    ('mdn', 'interactive-examples'): 'Interactive Examples',
    ('mdn', 'kumascript'): 'KumaScript',
    ('mdn', 'browser-compat-data'): 'BCD',
    ('mdn', 'doc-linter-webextension'): 'Doc Linter WebExtension',
    ('mdn', 'data'): 'Data',
    ('mozmeao', 'infra'): 'Infra'
}


template = """\
---
layout: post
title: Kuma Report, %(month)s %(year)d
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in %(month)s in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- [Item 1](#item1-%(month_id_suffix)s)
- [Item 2](#item2-%(month_id_suffix)s)
- [Item 3](#item3-%(month_id_suffix)s)
- [Shipped tweaks and fixes](#tweaks-%(month_id_suffix)s)
  by merging %(total)s pull requests,
  including %(prs_from_new_users)s pull requests
  from %(new_users)s new contributors.

Here's the plan for %(next_month)s:

- [Plan 1](#plan1-%(month_id_suffix)s)
- [Plan 2](#plan2-%(month_id_suffix)s)
- [Plan 3](#plan3-%(month_id_suffix)s)

<!--more-->

Done in %(month)s
===

<a name="item1-%(month_id_suffix)s">Item 1
---
Here's the first item, including lots of images.

<a name="item2-%(month_id_suffix)s">Item 2
---
The second item is also important.

<a name="item3-%(month_id_suffix)s">Item 3
---
Everyone stopped reading.

<a name="tweaks-%(month_id_suffix)s">Shipped Tweaks and Fixes
---
There were %(total)s PRs merged in %(month)s:

%(pr_counts_text)s

Many of these were from external contributors, including several first-time
contributions. Here are some of the highlights:

%(pr_details)s

Planned for %(next_month)s
===
Intro

<a name="plan1-%(month_id_suffix)s">Plan 1
---
Main effort

<a name="plan2-%(month_id_suffix)s">Plan 2
---
Second effort

<a name="plan3-%(month_id_suffix)s">Plan 3
---
Thing we promised last month
"""


def get_report(client_id, client_secret):
    """Create the Kuma Report template for the month."""
    month = pick_month()
    next_month = month + timedelta(days=28)
    while next_month.month == month.month:
        next_month += timedelta(days=1)
    last_day = next_month - timedelta(days=1)

    pr_data = get_pr_data(repos.keys(), client_id, client_secret)
    user_data = get_user_data(pr_data, client_id, client_secret)
    pr_counts_text, pr_counts = get_pr_counts(pr_data, month, last_day)
    pr_details, total, new_users, new_prs = get_pr_details(
        pr_data, user_data, month, last_day, pr_counts)

    params = {
        'month': month.strftime('%B'),
        'next_month': next_month.strftime('%B'),
        'month_id_suffix': month.strftime('%b-%y').lower(),
        'year': month.year,
        'total': total,
        'pr_counts_text': pr_counts_text,
        'pr_details': pr_details,
        'prs_from_new_users': new_prs,
        'new_users': new_users
    }

    return template % params


def pick_month():
    """Pick the report month based on current date.

    The month is picked by which end-of-month is closest.
    For example, on Oct 20th and November 5th, October is picked.
    The return is the 1st of the selected month, such as Oct 1, 2017.
    """
    today = date.today()
    month = date(today.year, today.month, 1)
    if today.day < 14:
        # Use last month
        month -= timedelta(days=27)
        while month.day != 1:
            month -= timedelta(days=1)
    return month


def get_pr_data(repos, client_id, client_secret):
    """Get the data for pull requests merged during the time period."""
    pr_data = []
    for owner, repo in repos:
        repo_prs = get_pr_data_for_repo(
            owner, repo, client_id, client_secret)
        pr_data.extend(repo_prs)
    return pr_data


class PullRequest(object):
    """Represents a merged  GitHub pull request."""
    def __init__(self, owner, repo, github_response):
        """Initialize from the GitHub API response."""
        self.owner = owner
        self.repo = repo
        self.number = github_response['number']
        self.username = github_response['user']['login']
        self.user_url = github_response['user']['url']
        self.title = github_response['title']
        self.merged_at = self.to_datetime(github_response['merged_at'])
        self.created_at = self.to_datetime(github_response['created_at'])

    def to_datetime(self, raw_date_str):
        """Convert a GitHub date string to a datetime."""
        if raw_date_str is None:
            return ''
        dateformat = '%Y-%m-%dT%H:%M:%S'
        date_str = raw_date_str
        if raw_date_str.endswith('Z'):
            date_str = date_str[:-1]
        dt = datetime.strptime(date_str, dateformat)
        return dt


def get_pr_data_for_repo(owner, repo, client_id, client_secret):
    """Get the data for pull requests merged in a repo."""
    prs = []
    is_last = False
    url_params = {'owner': owner, 'repo': repo}
    url_pat = 'https://api.github.com/repos/%(owner)s/%(repo)s/pulls'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'state': 'closed',
    }
    next_url = None
    first = True
    resp = requests.get(url_pat % url_params, params=payload)
    while not is_last:
        # Request next_url if this is not the first request
        if first:
            first = False
        else:
            resp = requests.get(next_url)
        print(resp.url, file=sys.stderr)

        # Abort if the return is an error
        out = resp.json()
        if 'message' in out:
            pprint.pprint(out, file=sys.stderr)
            raise Exception(resp.text)

        # Process the PRs
        for pr in resp.json():
            if pr['merged_at']:
                # Record the PR
                pr_obj = PullRequest(owner, repo, pr)
                prs.append((owner, repo, pr_obj.number, pr_obj))

        # Process the links and get the next URL
        links = get_links(resp.headers['Link'])
        next_url = links.get('next')
        is_last = next_url is None

    prs.sort()
    return prs


class User(object):
    """Represents a GitHub user."""
    def __init__(self, github_response):
        """Initialize from the GitHub API response."""
        self.username = github_response['login']
        self.fullname = github_response['name'] or self.username
        self.prs = defaultdict(list)
        self.pr_merge_range = dict()

    def add_pr(self, pr_obj):
        """Add a merged PullRequest."""
        key = (pr_obj.owner, pr_obj.repo)
        self.prs[key].append(pr_obj)
        if key in self.pr_merge_range:
            start, end = self.pr_merge_range[key]
            if pr_obj.merged_at < start:
                start = pr_obj.merged_at
            if pr_obj.merged_at > end:
                end = pr_obj.merged_at
        else:
            start, end = pr_obj.merged_at, pr_obj.merged_at
        self.pr_merge_range[key] = (start, end)

    def is_new(self, owner, repo, start, end):
        """Is the user a new contributor in this range?"""
        key = (owner, repo)
        if key not in self.pr_merge_range:
            return False
        merge_start, merge_end = self.pr_merge_range[key]
        return start <= merge_start.date() <= end


def get_user_data(prs, client_id, client_secret):
    """Get user data from PR data."""
    users = {}
    for owner, repo, number, pr in prs:
        username = pr.username

        # Initialize the User if needed
        if username not in users:
            print(pr.user_url, file=sys.stderr)
            payload = {
                'client_id': client_id,
                'client_secret': client_secret
            }
            resp = requests.get(pr.user_url, params=payload)

            # Abort if the return is an error
            out = resp.json()
            if 'message' in out:
                pprint.pprint(out, file=sys.stderr)
                raise Exception(resp.text)

            user = User(out)
            users[username] = user

        users[username].add_pr(pr)

    return users


re_link_spec = re.compile(r"""(?x)   # Be verbose
    <(?P<url>[^>]*)>;       # An URL wrapped in <>
    \srel="(?P<rel>[^"]*)"  # rel="type"
""")


def get_links(link_header):
    """Process the links from a GitHub API Link: header."""
    links = {rel: url for url, rel in re_link_spec.findall(link_header)}
    return links


def get_pr_counts(pr_data, start, end):
    """Create links to merged PR lists, with counts."""

    # Count all the PRs per repo that are in the range
    counts = Counter()
    for owner, repo, number, obj in pr_data:
        if start <= obj.merged_at.date() <= end:
            counts[(owner, repo)] += 1

    # Create Markdown links to the GitHub paginated view
    line_tmpl = ("- [%(count)s %(owner)s/%(repo)s PR%(s)s]"
                 "(https://github.com/%(owner)s/%(repo)s/pulls?"
                 "page=1&q=is:pr+is:closed"
                 "+merged:\"%(start)s..%(end)s\"&utf8=✓)")
    lines = []
    repo_counts = OrderedDict()
    for key, count in counts.most_common():
        repo_counts[key] = count
        owner, repo = key
        lines.append(line_tmpl % {
            'count': count,
            's': '' if count == 1 else 's',
            'owner': owner,
            'repo': repo,
            'start': start.isoformat(),
            'end': end.isoformat()
        })

    return "\n".join(lines), repo_counts


def md_escape(raw):
    """Escape text for Markdown."""
    md_unsafe = (
        ('[', '&#91;'),
        (']', '&#93;'),
    )
    escaped = escape(raw)
    for unsafe, safer in md_unsafe:
        escaped = escaped.replace(unsafe, safer)
    return escaped


def get_pr_details(pr_data, user_data, start, end, counts):
    """Create summaries of the PRs merged."""
    entry_tmpl = (
        "- %(title_wrap)s\n"
        "  ([%(repo_short)s PR %(number)s]"
        "(https://github.com/%(owner)s/%(repo)s/pull/%(number)s)),\n"
        "  from%(first_time)s\n"
        "  [%(fullname)s](https://github.com/%(username)s).")
    entries = []
    new_usernames = set()
    new_prs = 0
    for key in counts:
        for owner, repo, number, pr in pr_data:
            if key == (owner, repo) and (start <= pr.merged_at.date() <= end):
                title_wrap = '  '.join(wrap(md_escape(pr.title), 75))
                user = user_data[pr.username]
                is_new = user.is_new(owner, repo, start, end)
                if is_new:
                    new_usernames.add(pr.username)
                    new_prs += 1
                entries.append(entry_tmpl % {
                    'repo_short': repos[key],
                    'number': number,
                    'owner': owner,
                    'repo': repo,
                    'title_wrap': title_wrap,
                    'first_time': ' first-time contributor' if is_new else '',
                    'fullname': user.fullname,
                    'username': pr.username,
                })
    details = "\n".join(entries)
    total = len(entries)
    return details, total, len(new_usernames), new_prs


def get_args():
    parser = ArgumentParser(
        description='Generates the Kuma Report template.',
        epilog=("To create an OAuth app, see "
                " https://github.com/settings/developers"))
    parser.add_argument('client_id', type=str, help='GitHub OAuth2 client ID')
    parser.add_argument('client_secret', type=str,
                        help='GitHub OAuth2 client secret')
    parser.add_argument('--cachefile', type=str,
                        help='cache file for GitHub requests',
                        default='github_cache')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    requests_cache.install_cache(args.cachefile)
    report = get_report(args.client_id, args.client_secret)
    print("Done!", file=sys.stderr)
    print(report.encode('utf8'))
