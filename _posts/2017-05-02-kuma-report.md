---
layout: post
title: Kuma Report, April 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in April in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- Explored faster paths to AWS
- Maintained quality with new robots
- Improved the macros dashboard
- Goodbye BrowserCompat API, Hello Browser Compat Data
- Shipped tweaks and fixes

Here's the plan for May:

- Experiment with on-site interactive examples
- More legacy cleanup and fixes
- Ship the sample database

<!--more-->

Done in April
===

Explored Faster Paths to AWS
---
The
[AWS Migration Plan](https://docs.google.com/document/d/1-s343yxBMiugPQm5w2ho7EcSAcaLU4uOF6p2MLgbS1I/edit?usp=sharing)
details how Kuma and its backing services will need to evolve to fit into a
cloud architecture. However, there are good reasons to make the switch quickly
with a non-ideal architecture. We can minimize the painful transition where we
are supporting both the current datacenter and AWS. Some changes are
difficult to do now, and could be easier in the single AWS environment.

[jgmize](https://github.com/jgmize) and
[metadave](https://github.com/metadave),
the MozMEAO Site Reliability Engineers (SREs), are leading this effort to find
a faster path to AWS. You can follow their work in the
[MDN AWS Architecture Eval & Recommendation milestone](https://github.com/mozmar/infra/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22MDN+AWS+Architecture+Eval+%26+Recommendation%22)
in the [mozmar/infra repository](https://github.com/mozmar/infra). MDN
developers are still involved when a code change is needed, like
[escattone's](https://github.com/escattone) work to
[disable the contributor bar in maintenance mode](https://github.com/mozilla/kuma/pull/4196).

Maintained Quality with New Robots
---
Linters are pedantic robots that find syntax errors, style mistakes, and
language misuse. They can be jerks about the small stuff so that code reviewers
can focus on the ideas in the new code. We added several new linters to our
development process:

* [ESLint](http://eslint.org) can be used to check Kuma's JavaScript. Our JS
  needs work.
  ([PR 4199](https://github.com/mozilla/kuma/pull/4199))
* [EJSLint](https://github.com/ryanzim/ejs-lint) checks for invalid EJS
  templates in KumaScript PRs.
  ([PR 154](https://github.com/mozilla/kumascript/pull/154))
* [JSON Lint](https://github.com/zaach/jsonlint) checks for invalid JSON
  in KumaScript PRs.
  ([PR 159](https://github.com/mozilla/kumascript/pull/159))

Improved the Macros Dashboard
---
We've shipped an improved
[macros dashboard](https://developer.mozilla.org/en-US/dashboards/macros)
which lets KumaScript authors see how often macros are used, access the macro
source, and find documents that use the macro.  There are over 90 macros not
used on any page, so there are opportunities for deprecating and removing
macros.

Goodbye BrowserCompat API, Hello Browser Compat Data
---
[BrowserCompat](https://browsercompat.readthedocs.io/en/latest/) was a 2014
project to build an API to serve browser compatibility data, for MDN and for
other users.  An API was a development-heavy solution, and we had to abandon it
in 2016 when we lost resources.  This month,
[stephaniehobson](https://github.com/stephaniehobson) removed the MDN assets
supporting this project, so we can start shutting down the service.

For the next iteration of this idea, we're hand-coding JSON structures with
the Browser Compatibility data, and working to make MDN the first consumer of
this data.  You can follow the project on the
[browser-compat-data repository](https://github.com/mdn/browser-compat-data).

Shipped Tweaks and Fixes
---
Here's some other highlights from the
[41 merged Kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-04-01+..2017-05-01%22&utf8=✓)
in April:

- [PR 4181](https://github.com/mozilla/kuma/pull/4181):
  For page watch emails for a first translation, show a diff to the original
  English text, and prepare for more email changes
  ([jwhitlock](https://github.com/jwhitlock)).
- [PR 4182](https://github.com/mozilla/kuma/pull/4182):
  Banned user profiles are now 404 Not Found, not 403 Forbidden
  ([safwanrahman](https://github.com/safwanrahman)).
- [PR 4190](https://github.com/mozilla/kuma/pull/4190):
  The Insert Live Sample editor action inserts better section titles
  ([sheppy](https://github.com/a2sheppy)).


There are some new contributors in the
[16 merged KumaScript PRs](https://github.com/mozilla/kumascript/pulls?utf8=✓&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-04-01..2017-05-01%22%20)
in April:

- [PR 150](https://github.com/mozilla/kumascript/pull/150):
  Fix a French typo
  ([Porkepix](https://github.com/Porkepix])).
- [PR 158](https://github.com/mozilla/kuma/pull/158):
  Update HTML 5.1 and 5.2 specifications
  ([PointedEars](https://github.com/PointedEars])).

Planned for May
===
Here's what we're planning to ship in May:

Experiment with On-site Interactive Examples
---
In April, we shipped a first iteration of changing examples on MDN.
[wbamberg](https://github.com/wbamberg) and
[Elchi3](https://github.com/Elchi3) created alternate versions of JavaScript
and CSS reference pages with short examples at the top of the page. We've
added an A/B test to see if there is a behavioral difference for users
seeing these examples.

In May,
[schalkneethling](https://github.com/schalkneethling) will refine
wbamberg's prototype code to add interactive examples for
[CSS](https://github.com/mdn/css-examples) and
[JavaScript](https://github.com/mdn/js-examples).
This will allow users to test their understanding by making changes to the
short examples and seeing the results without leaving MDN. We'll also
ship this as an A/B test, and analyze the results before planning further
rollouts.

More Legacy Cleanup and Fixes
---
We're planning on reducing and removing more legacy features, to simplify the
Kuma project and make room for new development:

* Remove the Vagrant development environment.
* Remove the Ansible provisioning system, used by Vagrant and TravisCI.
* Rework Zones, moving the styles to standard assets and simplifying
  configuration.
* Fix several bugs and misfeatures in client-side drafts.
* Rewrite more tests in the
  [py.test](https://docs.pytest.org/en/latest/) style.
* Improve the KumaScript engine, macros, and development process.

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We don't want to break the tradition: the
sample database will ship in May, for the anniversary of the project. See
[PR 4076](https://github.com/mozilla/kuma/pull/4076) for the remaining
tasks.
