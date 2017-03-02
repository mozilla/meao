---
layout: post
title: Kuma Report, February 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in February in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- Added Demo deployments in AWS
- Promoted the Sauce Labs partnership
- Packaged MDN data
- Shipped tweaks and fixes

Here's the plan for March:

- Ship read-only maintenance mode
- Test examples at the top of reference pages
- Ship the sample database

<!--more-->

Done in February
===

Demo Deployments in AWS
---
Thanks to [metadave](https://github.com/metadave) and 
[escattone](https://github.com/escattone), MDN staff can now
[deploy demo servers](https://kuma.readthedocs.io/en/latest/development.html#deis-workflow-demo-instances)
to AWS. [Bedrock](https://github.com/mozilla/bedrock) has had this
feature for a while, and it is extremely useful when demonstrating a change
for manual or automated testing. It is also one step closer to MDN being
hosted in AWS.

Sauce Labs Partnership
---
Sauce Labs provides a platform to test your website across many OS and browser
combinations, so that you can automate testing and find issues before your
users do.  Mozilla is partnering with Sauce Labs to provide a
[free trial](https://saucelabs.com/cross-browser-testing-tutorial) of the
service. We're promoting this offer on the
[home page](https://developer.mozilla.org)
and our
[introduction to automated testing](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Automated_testing).
This required cross-team collaboration from Vik Iya, Kadir Topal, Rachel Wong,
and Arcadio Lainez, and was implemented on MDN by
[jpetto](https://github.com/jpetto).

Packaged MDN data
---
The writers have continued to work on extracting MDN data to GitHub.
The [mdn/data](https://github.com/mdn/data) repo has grown an excited
community who are impatient to
[publish the data on npm](https://github.com/mdn/data/issues/5).
Thanks to
[Elchi3](https://github.com/Elchi3) and
[iamstarkov](https://github.com/iamstarkov), we have a
[package.json file](https://github.com/mdn/data/pull/36), and you can now
run ``npm install mdn/data``.  Further work is planned to publish on npm,
and to make this data (and the
[Browser Compatibility data](https://github.com/mdn/browser-compat-data))
useful on MDN and in other projects.

Shipped Tweaks and Fixes
---
Other highlights from the
[32 merged Kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-02-01+..2017-03-01%22&utf8=✓)
in February:

- [PR 4141](https://github.com/mozilla/kuma/pull/4141):
  Fix capitalization for Articles in need of review page
  ([Tckool](https://github.com/Tckool)'s first PR!).
- [PR 4136](https://github.com/mozilla/kuma/pull/4136):
  Remove TransactionTestCase, making tests twice as fast for
  local development
  ([safwanrahman](https://github.com/safwanrahman)).
- [PR 4057](https://github.com/mozilla/kuma/pull/4057),
  [PR 4067](https://github.com/mozilla/kuma/pull/4067),
  [PR 4080](https://github.com/mozilla/kuma/pull/4080), and
  [PR 4088](https://github.com/mozilla/kuma/pull/4088):
  Improve the page editing experience with CKEditor updates and tweaks
  ([a2sheppy](https://github.com/a2sheppy)).
- [PR 4099](https://github.com/mozilla/kuma/pull/4099):
  Remove Intern Tests, completing the transition to
  [py.test](http://docs.pytest.org/en/latest/) for browser-based tests
  ([stephaniehobson](https://github.com/stephaniehobson)).
- [PR 4125](https://github.com/mozilla/kuma/pull/4125):
  Expand docs for the MDN CI pipeline
  ([escattone](https://github.com/escattone)). We now have a short,
  documented process for running integration tests during deployments.
- [PR 4114](https://github.com/mozilla/kuma/pull/4114):
  Move font-loading to client-side, improving performance and simplifying the
  backend
  ([jpetto](https://github.com/jpetto)).
- [PR 4103](https://github.com/mozilla/kuma/pull/4103):
  Fix bugs with case-insensitive tags
  ([jwhitlock](https://github.com/jwhitlock)).

KumaScript continues to be busy, with
[19 merged PRs](https://github.com/mozilla/kumascript/pulls?utf8=✓&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-02-01..2017-03-01%22%20)
contributed by
[Elchi3](https://github.com/Elchi3),
[SebastianZ](https://github.com/SebastianZ),
[SphinxKnight](https://github.com/SphinxKnight),
[a2sheppy](https://github.com/a2sheppy),
[chrisdavidmills](https://github.com/chrisdavidmills),
and
[jpmedley](https://github.com/jpmedley). MDN staff and core volunteers
are becoming more experienced with GitHub, and at fixing git issues
over IRC.

Planned for March
===
We're headed to sunny
[Toronto, Ontario](https://www.mozilla.org/en-US/contact/spaces/toronto/)
for a Spring work week, where we'll plan Q2 2017 and beyond. We also plan to
ship some features in March:

Read-Only Maintenance Mode
---
[jpetto](https://github.com/jpetto) and
[escattone](https://github.com/escattone) have been working on Read-Only
Maintenance Mode, a Kuma configuration that works against a recent database
backup, displaying MDN data but not allowing login or page editing. We'll work
with [jgmize](https://github.com/jgmize) and
[metadave](https://github.com/metadave) to deploy this mode to AWS in March,
eventually testing with live MDN traffic during off-peak hours.

Examples at the top of reference pages
---
In the next few months, we're going to experiment with small, interactive
examples at the top of high-traffic reference pages, and collect qualitative
and quantitative data on visitor reactions. This includes an A/B
test of the changes, using the [Traffic
Cop](https://github.com/mozilla/trafficcop) library that we
[introduced](https://mozilla.github.io/meao/2017/01/16/traffic-cop/) a few
weeks ago.

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We don't want to break the tradition: the
sample database will ship in March. See
[PR 4076](https://github.com/mozilla/kuma/pull/4076) for the remaining
tasks.
