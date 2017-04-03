---
layout: post
title: Kuma Report, March 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in March in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- Shipped content experiments framework
- Merged read-only maintenance mode
- Shipped tweaks and fixes

Here's the plan for April:

- Clean up KumaScript macro development
- Improve and maintain CSS quality
- Ship the sample database

<!--more-->

Done in March
===

Content Experiments Framework
---
We're planning to experiment with small, interactive examples at the top of
high-traffic reference pages. We want to see the effects of this change,
by showing the new content to some of the users, and tracking their
behaviour.  We shipped ia new A/B testing framework, using the
[Traffic Cop](https://github.com/mozilla/trafficcop) library in the browser.
We'll use the framework for the examples experiment, starting in April.

Read-Only Maintenance Mode
---
We've merged a new maintenance mode configuration, which keeps Kuma running
when the database connection is read-only. Eventually, this will allow MDN
content to remain available when the database is being updated, and lead
to new distributed architectures. In the near term, we'll use it to
test our new AWS infrastructure running production backups, and eventually
against off-peak MDN traffic.

Shipped Tweaks and Fixes
---
Here's some other highlights from the
[15 merged Kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-03-01+..2017-04-01%22&utf8=✓)
in March:

- [PR 4134](https://github.com/mozilla/kuma/pull/4134):
  Change logout from a GET to a POST, possibly ending a long-standing
  [random logout annoyance](https://bugzilla.mozilla.org/show_bug.cgi?id=1325898)
  ([safwanrahman](https://github.com/safwanrahman)).
- [PR 4152](https://github.com/mozilla/kuma/pull/4152):
  Use gulp to process .scss files, speeding up local development
  ([jpetto](https://github.com/jpetto)).
- [PR 4153](https://github.com/mozilla/kuma/pull/4153):
  Import sample MDN DB when creating demo instance
  ([metadave](https://github.com/metadave))
- [PR 4154](https://github.com/mozilla/kuma/pull/4154):
  Add API service to demo deploys
  ([jgmize](https://github.com/jgmize)).
  These two PRs make demo instances useful for testing rendering.

KumaScript continues to be busy, with
[19 merged PRs](https://github.com/mozilla/kumascript/pulls?utf8=✓&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-03-01..2017-04-01%22%20).
There were some PRs from new contributors:

- [PR 134](https://github.com/mozilla/kumascript/pull/134):
  l10n LegacyAddonNotice.ejs to zh-CN
  ([yfdyh000](https://github.com/yfdyh000)).
- [PR 139](https://github.com/mozilla/kumascript/pull/139):
  Fix es7 and latest draft macros
  ([leobalter](https://github.com/leobalter)).
- [PR 140](https://github.com/mozilla/kumascript/pull/140):
  Add some pt-br translations
  ([leobalter](https://github.com/leobalter) again!).

Planned for April
===
We had a productive work week in Toronto. We decided that we need to make sure
we're paying down our technical debt regularly, while we continue supporting
improved features for MDN visitors. Here's what we're planning to ship in April:

Clean Up KumaScript Macro Development
---
KumaScript macros have moved to 
[GitHub](https://github.com/mozilla/kumascript/tree/master/macros),
but
[ghosts](https://developer.mozilla.org/en-US/docs/templates)
of the old way of doing things remain in Kuma, and the development process is
still tricky.  This month, we'll tackle some of the known issues:

* Remove the legacy macros from MDN (stuck in time at November 2016)
* Remove macro editing from MDN
* Update macro searching
* Start on a automated testing framework for KumaScript macros

Improve and Maintain CSS Quality
---
We're preparing for some future changes by getting our CSS in order. One of the
strategies will be to define style rules for our CSS, and check that existing
code is compliant with [stylelint](https://stylelint.io). We can then enforce
the style rules by detecting violations in pull requests.

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We don't want to break the tradition: the
sample database will ship in April. See
[PR 4076](https://github.com/mozilla/kuma/pull/4076) for the remaining
tasks.
