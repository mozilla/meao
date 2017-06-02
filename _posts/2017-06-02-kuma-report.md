---
layout: post
title: Kuma Report, May 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in May in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- Refactored zone CSS
- Improved drafts
- Moved redirects into Kuma
- Retired old features
- Let data be data
- Shipped tweaks and fixes

Here's the plan for June:

- Ship on-site interactive examples
- Ship brand updates to beta users
- Add KumaScript macro tests
- Ship the sample database

<!--more-->

Done in May
===

Refactored Zone CSS
---
Some MDN sections look different, like the [archive of old
pages](https://developer.mozilla.org/en-US/docs/Archive).  Others also appear
at non-standard URLs, like the [Firefox
pages](https://developer.mozilla.org/en-US/Firefox). Kuma uses manually
maintained Zones to accomplish this, and it is a source of bugs and
inconsistent experiences.

We took a big step toward better zones by refactoring the custom styles.
[escattone](https://github.com/escattone) did the
backend work ([PR 4209](https://github.com/mozilla/kuma/pull/4209))
so that styles are automatically applied across translations.
[stephaniehobson](https://github.com/stephaniehobson) did the front-end work,
moving the CSS from the database to the
repository ([PR 4206](https://github.com/mozilla/kuma/pull/4206)),
then splitting them into per-zone CSS files
([PR 4224](https://github.com/mozilla/kuma/pull/4224),
 [PR 4229](https://github.com/mozilla/kuma/pull/4229)).

The zone CSS is now up to the quality standard of the rest of our CSS, and
the experience across translations is more consistent. It wasn't easy,
taking 10 total PRs, but [Sass](http://sass-lang.com) and other front-end tools
made the transition smoother than it would have been a year ago. Custom Zone
URLs are still painful, but we'll tackle those soon.

Improved Drafts
---
We have a
[papercut process](https://trello.com/b/z4bvVB4R/mdn-backlog-by-team-member%2Fstakeholder)
to determine the most annoying bugs. Recently, bugs around the drafts feature
rose to the top. The draft feature saves the editor content to local storage,
to add a layer of safety from browser crashes and session timeouts.

[stephaniehobson](https://github.com/stephaniehobson) has been working on [PR
4186](https://github.com/mozilla/kuma/pull/4186) for a few weeks, and it was
recently merged to master. This PR fixes 6 known bugs, including the
``document_saved`` query parameter. This code will be be deployed next
week.

Moved Redirects into Kuma
---
In production, many basic redirects are handled using
[Apache RewriteRules](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html#RewriteRule).
This helped with the transition from DekiWiki to Kuma in 2012. As we move
to AWS, we'd like to move this functionality into Kuma. This makes it easier
to test and modify redirects, reduces differences between development and
deployment, and reduces or eliminates the need for Apache or another web server.

[pmac](https://github.com/pmac) recently released
[django-redirect-url](https://github.com/pmac/django-redirect-urls), which
packages the redirects code used by
[bedrock](https://github.com/mozilla/bedrock/).
[metadave](https://github.com/metadave) integrated this library
([PR 4217](https://github.com/mozilla/kuma/pull/4217)), and translated
production Apache rules into Kuma code
([PR 4220](https://github.com/mozilla/kuma/pull/4220)).
The functional tests exposed an Apache configuration difference between staging
and production, which our WebOps team fixed. The work continues in
[PR 4231](https://github.com/mozilla/kuma/pull/4231).

Now that we have a redirects framework in Kuma, we may use it to help retire
the custom zone URLs.

Retired Old Features
---
I removed some features that have been deprecated in the last year:

* [Vagrant](https://www.vagrantup.com), used from 2011 to 2016 for a
  development environment, is replaced by [Docker](https://www.docker.com)
  ([PR 4214](https://github.com/mozilla/kuma/pull/4214) and
   [4216](https://github.com/mozilla/kuma/pull/4216)).
* [Ansible](https://www.ansible.com), used from 2016 to 2017 for
  provisioning development and testing environments, is also replaced by
  Docker.
  ([PR 4239](https://github.com/mozilla/kuma/pull/4239) and
   [4242](https://github.com/mozilla/kuma/pull/4242)).
* KumaScript macro editing on Kuma, used from 2012 to 2016, has moved to the
  [KumaScript repo](https://github.com/mozilla/kumascript/tree/master/macros)
  ([PR 4208](https://github.com/mozilla/kuma/pull/4208),
   [4232](https://github.com/mozilla/kuma/pull/4232), and
   [4233](https://github.com/mozilla/kuma/pull/4233)).

The changes removed 7,600 lines from the Kuma project, and means that we don't
have to explain this bit of history to new contributors. We're using more of
the native services of [TravisCI](https://travis-ci.org/mozilla/kuma), which
makes our ``py27`` build 30% faster, and lets us experiment with alternate
environments and services.

Let Data be Data
---
There's a lot of data on MDN, contributed over more than 10 years. A lot of
that data is trapped in formats like HTML that made it easy to contribute,
but hard to maintain and remix. We want to formalize this data in
machine-parsable formats, so that MDN and others can use it in new and
exciting ways.

[mdn/browser-compat-data](https://github.com/mdn/browser-compat-data) is a
growing repository of Browser Compatibility data extracted from MDN.
There were
[36 merged PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-05-01+..2017-06-01%22&utf8=✓)
in May, and we're using it on some of the compatibility tables on MDN.

[mdn/data](https://github.com/mdn/data) contains general data for Web
technologies, starting with CSS data such as properties, selectors, and
types. There were
[12 merged PRs](https://github.com/mdn/data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-05-01+..2017-06-01%22&utf8=✓)
in May, and after some recent updates
([PR 162](https://github.com/mozilla/kuma/pull/162) by
 [jwhitlock](https://github.com/jwhitlock) and
 [PR 183](https://github.com/mozilla/kuma/pull/183) by
 [Elchi3](https://github.com/Elchi3)) we're using the master branch
on MDN again.

With these data sources rapidly changing, there is pressure on KumaScript to
move quickly and break less things. They can be loaded as npm
packages (``npm install mdn/browser-compat-data`` and
``npm install mdn/data``), and with
[escattone's](https://github.com/escattone)
[PR 183](https://github.com/mozilla/kuma/pull/183), we're loading some of the
data this way. He also has switched from
[nodeunit](https://github.com/caolan/nodeunit) to
[Mocha](http://mochajs.org)
([PR 188](https://github.com/mozilla/kuma/pull/188)), in preparation for
automated testing of KumaScript macros.

Shipped Tweaks and Fixes
---
Here's some other highlights from the
[37 merged Kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-05-01+..2017-06-01%22&utf8=✓)
in May:

- [PR 4210](https://github.com/mozilla/kuma/pull/4210):
  Upgrade [py.test](https://github.com/pytest-dev/pytest), a testing framework,
  as well as related py.test plugins
  ([jwhitlock](https://github.com/jwhitlock)).
- [PR 4240](https://github.com/mozilla/kuma/pull/4240):
  Add liveness and readiness endpoints, so that Kubernetes can dynamically
  start and stop Kuma pods
  ([escattone](https://github.com/escattone)).
- [PR 4237](https://github.com/mozilla/kuma/pull/4237):
  Upgrade [Bleach](https://github.com/mozilla/bleach), an HTML sanitizing
  library
  ([jwhitlock](https://github.com/jwhitlock)).

Here's some other highlights from the
[19 merged KumaScript PRs](https://github.com/mozilla/kumascript/pulls?utf8=✓&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-05-01..2017-06-01%22%20)
in May:

- [PR 173](https://github.com/mozilla/kumascript/pull/173):
  Update the WebExtension compatibility tables for browser-compat-data changes
  ([wbamberg](https://github.com/wbamberg))
- [PR 174](https://github.com/mozilla/kumascript/pull/174) and
  [PR 178](https://github.com/mozilla/kumascript/pull/178):
  Updates to the AddonSidebar
  (first contributions from
  [rebloor](https://github.com/rebloor)).
- [PR 187](https://github.com/mozilla/kumascript/pull/187):
  Update the LegacyAddonsNotice
  (first contribution from
  [andrewtruongmoz](https://github.com/andrewtruongmoz)).

Planned for June
===
Mozilla is gathering in San Francisco for an
[All-Hands meeting](https://wiki.mozilla.org/All_Hands/SanFrancisco)
at the end of June, which leaves 3 week for development work.
Here's what we're planning to ship in June:

Ship On-site Interactive Examples
---
We ran an A/B test on popular pages, showing half the users pages with small
examples on top, and half without. We looked at the analytics, and we did not
see a significant change in user behavior.  We did get feedback that the
samples are useful, especially for those reminding themselves how a familiar
technology works.

We're going ahead with the next phase. We're going to make the new
version the default, and start experimenting with interactive
examples. Instead of looking for changes in site usage, we'll focus on
interaction and performance.
[schalkneethling](https://github.com/schalkneethling) is leading this next
phase, and you can follow the work at 
[mdn/interactive-examples](https://github.com/mdn/interactive-examples).

Ship Brand Updates to Beta Users
---
Mozilla had a [open design process](https://blog.mozilla.org/opendesign/) to
develop a new brand identity, and has a [website](https://mozilla.ninja)
detailing the results. This new brand is rolling out across Mozilla websites.
We've also been thinking about the brand, mission, and focus of MDN, which has
evolved over the last five years.

In June, we'll start talking about the MDN brand, and will start shipping some
of the new elements to beta users, such as updated logos, headers, and footers.

Add KumaScript Macro Tests
---
Currently, maintainers review KumaScript macro changes by manually testing
them in development environments. This works for small changes, but big
changes and complex macros are hard to test manually. In June,
[escattone](https://github.com/escattone) will start adding regression tests
for some key macros. When we have a working framework and some good examples,
we'll start asking staff and contributors to add tests for other macros, and to
submit updated tests with PRs.

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We don't want to break the tradition, so we'll
bend it a little. The first bit of the supporting code, a ``scrape_user``
command, has been merged, and the rest of the code will ship in July.
See [PR 4248](https://github.com/mozilla/kuma/pull/4248) for the
``scrape_document`` command, and
[PR 4076](https://github.com/mozilla/kuma/pull/4076) for the remaining tasks.
