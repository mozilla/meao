---
layout: post
title: Kuma Report, July 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in July in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- Shipped the new design to all users
- Shipped the sample database
- Shipped tweaks and fixes

Here's the plan for August:
- Continue the redesign and interactive examples
- Update localization of macros
- Establish maintenance mode in AWS

<!--more-->

Done in July
===

Shipped the New Design to All Users
---
In June, we revealed the new MDN web docs design to beta testers. In July,
[Stephanie Hobson](https://github.com/stephaniehobson) and [Schalk
Neethling](https://github.com/schalkneethling) fixed many bugs, adjusted
styles, shipped the homepage redesign, and answered a lot of feedback.
The new design was shipped to all MDN Web Docs users on July 25, and the old
design files were retired.

The redesign was a big change, with some interesting problems that called for
creative solutions.  For details, see Stephanie's blog post,
[The MDN Redesign “Behind the Scenes”](https://hacks.mozilla.org/2017/07/the-mdn-redesign-behind-the-scenes/).

Shipped the Sample Database
---
The sample database project, started in May 2016, finally shipped in July.

Data is an important part of Kuma development. With the code and backing
services you get the home page, and not much else. To develop features or test
changes, you often need wiki pages, historical revisions, waffle flags,
constance settings, tags, search topics, users and groups.  Staff developers
could download a 2 GB anonymized production database, wait 30 minutes for it to
load, and then they would have a useful dev environment.  Contributors had to
manually copy data from production, and usually didn't bother. The sample
database has a small but representative data set, suitable for 90% of
development tasks, and takes less than a minute to download and install.

The sample database doesn't have all the data on MDN, to keep it small.
There are now
[scraping tools](https://kuma.readthedocs.io/en/latest/data.html)
for adding more production data to your development database.
This is especially useful for development and testing of
[KumaScript macros](https://github.com/mdn/kumascript/tree/master/macros),
which often require specific pages.

Finally, integration testing is challenging because non-trivial testing
requires some known data to be present, such as specific pages and editor
accounts. Now, a testing deployment can combine new code with the sample
database, and automated browser-based tests can verify new and old
functionality. Some tests can change the data, and the sample data can
be reloaded to a known state for the next test.

Shipped Tweaks and Fixes
---
There were many PRs merged in July:

- [44 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)
- [36 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)
- [29 mdn/kumascript PRs](https://github.com/mozilla/kumascript/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)
- [22 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)
- [22 mdn/doc-linter-webextension PRs](https://github.com/mdn/doc-linter-webextension/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)
- [4 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-07-01..2017-08-01%22&utf8=✓)

Some highlights:

- [Kuma PR 4338](https://github.com/mozilla/kuma/pull/4338):
  Move the locale files from kuma to their own repository,
  [mozilla-l10n/mdn-l10n](https://github.com/mozilla-l10n/mdn-l10n),
  from [John Whitlock](https://github.com/jwhitlock).
  This will allow for the higher volume of locale changes when KumaScript
  string are added, without requiring unnecessary source builds.
- [Interactive Examples PR 156](https://github.com/mdn/interactive-examples/pull/156/files):
  Update to publishing to S3, fixing
  [issue #54](https://github.com/mdn/interactive-examples/issues/54), from
  [Schalk Neethling](https://github.com/schalkneethling).
  The S3 bucket, resources, and process were set up by
  [Dave Parfitt](https://github.com/metadave), with details in
  [mozmeao/infra issue #362](https://github.com/mozmeao/infra/issues/362).
- [Kumascript PR 220](https://github.com/mdn/kumascript/pull/220):
  Update specification names and URLs. This is the first contribution from
  [Domenic Denicola](https://github.com/domenic).
- [Kumascript PR 231](https://github.com/mdn/kumascript/pull/231):
  Add Ukrainian (uk) translations for the Glossary macro. Another first
  contribution, from
  [Віталій Крутько](https://github.com/asmforce).
- [Kumascript PR 241](https://github.com/mdn/kumascript/pull/241):
  Fix API calls such as ``page.subpagesExpand``, making more macros
  work in the Docker development and production environments, from
  [Ryan Johnson](https://github.com/escattone)
- [Kumascript PR 248](https://github.com/mdn/kumascript/pull/248):
  The first of many PRs adding Brazilian Portuguese (pt-BR) from
  first time contributor
  [Fernandolrs](https://github.com/Fernandolrs).
- [Browser Compat Data PR 278](https://github.com/mdn/browser-compat-data/pull/278):
  Edge does support iterator, according to the first-time contributor
  [Flor Braz](https://github.com/florbraz).
- [Browser Compat Data PR 286](https://github.com/mdn/browser-compat-data/pull/286):
  There's no such thing as IE 15, according to first-time contributor
  [Caleb Eggensperger](https://github.com/calebegg).
- [Browser Compat Data PR 301](https://github.com/mdn/browser-compat-data/pull/301):
  Add MS Edge support for localization, from first-time contributor
  [Yordan Darakchiev](https://github.com/iordan93).
- [Data PR 99](https://github.com/mdn/data/pull/99):
  Add schema validation for groups parameter, from
  [Sebastian Zartner](https://github.com/SebastianZ)

Planned for August
===

Continue the redesign and the interactive examples
---
We've established the new look-and-feel of MDN on the homepage and article
pages, and will continue to tweak the design for corner cases and bugs. For the
next phase, we'll look at the content of article pages, and consider better
ways to display information and to navigate within and between pages. It is
harder to change these aspects than global headers and footers, so it may be
a while before you see the fruits of this design process.

Work continues on the interactive examples. They have gone through several
review and bug fix cycles, and have a working production deployment system.
There's been interest and work to enable contributions
([Issue 99](https://github.com/mdn/interactive-examples/issues/99)).
In August, we'll launch user testing, and enable the new examples for beta
testers.  See the 
[projects page](https://github.com/mdn/interactive-examples/projects)
for the remaining work.

Update Localization of Macros
---
Currently, KumaScript macros use in-macro localization strings and
utility functions like
[getLocalString](https://github.com/mozilla/kumascript/blob/master/macros/MDN-Common.ejs#L52)
to localize output for three to five languages.  Meanwhile, user interface strings in
Kuma are translated in
[Pontoon](https://pontoon.mozilla.org/projects/mdn/) into 57 languages. We'd
like to use a similar workflow for strings in macros.

In August, we'll assemble the toolchain for localizing strings at render time,
and for extracting the localizable strings for translation in Pontoon.
Converting the macros to use localizable strings will be a long process, but
there's a lot of community interest in translations, so we should get some
help.

Establish Maintenance Mode in AWS
---
Over the past 12 months, we've made some changes to MDN development, such as
switching to a Docker development environment, moving Kumascript macros to
Github, and getting our browser-based integration tests working. There are
benefits to each of these, but they were chosen because they move us closer to
our long term goal of serving MDN from AWS. We've slowly filled out our
[tech tree](https://en.wikipedia.org/wiki/Technology_tree) from our
[AWS plan](https://docs.google.com/document/d/1q0rNBieya_9NPqjWYX93_QwEge-K2wqLPPvdtZGyinE/edit):

![AWS Plan, July 2017]({{ site.baseurl }}/public/images/kuma/aws_plan_2017_07.svg)

In August, we plan to prepare a maintenance mode deployment in AWS, and send
some production traffic to it.  This will allow us to model the resources
needed when the production environment is hosted in AWS. It will also keep MDN
data available while the production database is transferred, when we finalize
the transition.
