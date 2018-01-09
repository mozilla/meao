---
layout: post
title: Kuma Report, December 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in December in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):
- [Purged 162 KumaScript Macros](#macro-massacre-dec-17)
- [Increased availability of MDN](#availability-dec-17)
- [Improved Kuma deployments](#deployments-dec-17)
- [Added browser compatibility data](#bcd-dec-17)
- [Said goodbye to Stephanie Hobson](#stephanie-dec-17)
- [Shipped tweaks and fixes](#tweaks-dec-17)
  by merging 209 pull requests,
  including 13 pull requests
  from 11 new contributors.

Here's the plan for January:

- [Prepare for a CDN](#cdn-dec-17)
- [Ship more interactive examples](#more-interactive-dec-17)
- [Update Django to 1.11](#django-dec-17)
- [Plan for 2018](#2018-dec-17)

<!--more-->

Done in December
===

<a name="macro-massacre-dec-17">Purged 162 KumaScript Macros
---
We moved the KumaScript macros to
[GitHub](https://github.com/mdn/kumascript/tree/master/macros) in
[November 2016](https://groups.google.com/forum/#!msg/mozilla.dev.mdn/MJHUaWtF0mU/cKppYPz0CwAJ),
and added a
[new macro dashboard](https://developer.mozilla.org/en-US/dashboards/macros).
This gave us a clearer view of macros across MDN, and highlighted that there
were still many macros that were unused or lightly used. Reducing the total
macro count is important as we change the way we localize the output and add
automated tests to prevent bugs.

We scheduled some time
to remove these old macros at our Austin work week, when multiple people could
quickly double-check macro usage and merge the
[86 Macro Massacre](https://github.com/mdn/kumascript/issues?utf8=%E2%9C%93&q=label%3A%22Macro+massacre%22)
pull requests. Thanks to
[Florian Scholz](https://github.com/Elchi3),
[Ryan Johnson](https://github.com/escattone), and
[wbamberg](https://github.com/wbamberg), we've removed 162 old macros, or
25% of the total at the start of the month.

![macro-massacre](
 {{ site.baseurl }}/public/images/kuma/2017-12-macro-massacre.png
 "Macro Massacre tag on GitHub")

<a name="availability-dec-17">Increased Availability of MDN
---
We made some additional changes to keep MDN available and to reduce
alerts.  [Josh Mize](https://github.com/jgmize) added
rate limiting to several public endpoints, including the homepage and wiki
documents ([PR 4591](https://github.com/mozilla/kuma/pull/4591)).
The limits should be high enough for all regular visitors, and only
high-traffic scrapers should be blocked.

I adjusted our liveness tests, but kept the database query for now
([PR 4579](https://github.com/mozilla/kuma/pull/4579)).
We added new thresholds for liveness and readiness in November, and these
appear to be working well.

We continue to get alerts about MDN during high-traffic spikes. We'll continue
to work on availability in 2018.

<a name="deployments-dec-17">Improved Kuma Deployments
---
[Ryan Johnson](https://github.com/escattone) worked to make our Jenkins-based
tests more reliable. For example, Jenkins now confirms that MySQL is ready
before running tests that use the database
([PR 4581](https://github.com/mozilla/kuma/pull/4581)). This helped find an
issue with the database being reused, and we're doing a
better job of cleaning up after tests
([PR 4599](https://github.com/mozilla/kuma/pull/4599)).

Ryan continued developing branch-based deployments, making them more reliable
([PR 4587](https://github.com/mozilla/kuma/pull/4587))
and expanding to production deployments
([PR 4588](https://github.com/mozilla/kuma/pull/4588)).
We can now deploy to staging and production by merging to
``stage-push`` and ``prod-push`` for Kuma as well as KumaScript, and
we can monitor the deployment with bot notifications in ``#mdndev``.
This makes pushes easier and more reliable, and gets us closer to
an automated deployment pipeline.

<a name="bcd-dec-17">Added Browser Compatibility Data
---
[Daniel D. Beck](https://github.com/ddbeck) continued to convert CSS
compatibility data from the wiki to the repository, and 
[wrote 35](https://github.com/mdn/browser-compat-data/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+merged%3A%222017-12-01..2017-12-31%22+author%3Addbeck)
of the 57 PRs merged in December. Thanks to Daniel for doing the conversion
work, and thanks to
[Jean-Yves Perrier](https://github.com/teoli2003) for many reviews
and merges over the holiday break.

[Stephanie Hobson](https://github.com/stephaniehobson) continued to refine
the design of the new compatibility tables, including an icon for the Samsung
Internet Browser and an updated Firefox icon
([Kuma PR 4605](https://github.com/mozilla/kuma/pull/4605)).
[Florian Scholz](https://github.com/Elchi3) added a legend, to explain the
notation
([KumaScript PR 437](https://github.com/mdn/kumascript/pull/437)). We're
getting closer to shipping these to all users. Please give any feedback at
[Beta Testing New Compatibility Table](https://discourse.mozilla.org/t/beta-testing-new-compatability-tables/21269/5)
on Discourse.

<a name="stephanie-dec-17">Said Goodbye to Stephanie Hobson
---
[Stephanie Hobson](https://github.com/stephaniehobson)
is moving to the [bedrock](https://github.com/mozilla/bedrock)
team in January, where she'll help maintain and improve
[www.mozilla.org](https://www.mozilla.org/).
[Schalk Neethling](https://github.com/schalkneethling) will take over as the
primary front-end developer for MDN Web Docs.

Over the past 3&frac12; years, Stephanie has had a huge impact on MDN.  She
shared her expertise on accessibility, multi-language support, readable HTML
tables and all things Google Analytics. She advocated for the users during the
spam mitigations and Persona shutdown.  She'd argue for design changes from a
web developer's perspective, and back it up with surveys and interviews.

She's also a talented developer, authoring
[over 400 PRs](https://github.com/mozilla/kuma/pulls?page=17&q=is%3Apr+author%3Astephaniehobson&utf8=%E2%9C%93).
She's responsible for a lot of the changes on MDN in 2017:

![mdn-one-year](
 {{ site.baseurl }}/public/images/kuma/2017-12-mdn-one-year.png
 "MDN changed a lot in 2017, thanks to Stephanie Hobson")

Schalk has been working on MDN for most of 2017. He's been focused on the
[interactive examples project](https://github.com/mdn/interactive-examples)
that fully shipped in December. He's also been reviewing front-end PRs, and
his feedback and suggestion have improved the front-end code for months.
In December, Stephanie and Schalk worked closely to make a smooth transition,
which included getting all the JavaScript to pass
[eslint](https://eslint.org/) tests
([PR 4596](https://github.com/mozilla/kuma/pull/4596) and
[PR 4597](https://github.com/mozilla/kuma/pull/4597)).

We look forward to seeing what Stephanie will do on bedrock, and we look
forward to Schalk's work and fresh perspective on MDN Web Docs.

<a name="tweaks-dec-17">Shipped Tweaks and Fixes
---
There were 209 PRs merged in December (which was supposed to be a light month):

- [98 mdn/kumascript PRs](https://github.com/mdn/kumascript/pulls?page=1&q=is:pr+is:closed+merged:"2017-12-01..2017-12-31"&utf8=✓)
- [57 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is:pr+is:closed+merged:"2017-12-01..2017-12-31"&utf8=✓)
- [32 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is:pr+is:closed+merged:"2017-12-01..2017-12-31"&utf8=✓)
- [13 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is:pr+is:closed+merged:"2017-12-01..2017-12-31"&utf8=✓)
- [9 mozmeao/infra PRs](https://github.com/mozmeao/infra/pulls?page=1&q=is:pr+is:closed+merged:"2017-12-01..2017-12-31"&utf8=✓)

Several of these were from first-time contributors:

- Add Worklets and related specifications
  ([KumaScript PR 511](https://github.com/mdn/kumascript/pull/511)),
  from
  [Jedipedia](https://github.com/Jedipedia).
- spec2 macro: Make ESDraft a Draft instead of a Living Specification.
  ([KumaScript PR 522](https://github.com/mdn/kumascript/pull/522)),
  from
  [Mathias Schäfer](https://github.com/molily).
- IE11 partially supports `new Map(iterable)`
  ([BCD PR 691](https://github.com/mdn/browser-compat-data/pull/691)),
  from
  [Nathan Hunzaker](https://github.com/nhunzaker).
- Firefox 59 allows browserAction set* methods to accept null
  ([BCD PR 710](https://github.com/mdn/browser-compat-data/pull/710)),
  from
  [Oriol Brufau](https://github.com/Loirooriol).
- Add compat for module attribute of script element
  ([BCD PR 717](https://github.com/mdn/browser-compat-data/pull/717)),
  from
  [Davilink](https://github.com/Davilink).
- Safari 11 supports Cache-Control: immutable
  ([BCD PR 726](https://github.com/mdn/browser-compat-data/pull/726)),
  from
  [Rouven Weßling](https://github.com/realityking).
- Update data for comma-optional syntax for color
  ([BCD PR 745](https://github.com/mdn/browser-compat-data/pull/745)),
  from
  [csnardi](https://github.com/csnardi).
- Update browser compat data for mix-blend-mode CSS property
  ([BCD PR 757](https://github.com/mdn/browser-compat-data/pull/757)),
  from
  [owaisalhashimi](https://github.com/owaisalhashimi).
- fix bug 1420354 - Use rel="license" instead of rel="copyright"
  ([Kuma PR 4603](https://github.com/mozilla/kuma/pull/4603)),
  from
  [Mai Truong](https://github.com/maiquynhtruong).
- Correct spelling of broccoli in array-pop example
  ([Interactive Examples PR 365](https://github.com/mdn/interactive-examples/pull/365)),
  from
  [Leonid Kovalev](https://github.com/normalhuman).
- Adding a CSS interactive example for word-break property
  ([PR 368](https://github.com/mdn/interactive-examples/pull/368)),
  Adding an interactive example for the opacity CSS property
  ([PR 369](https://github.com/mdn/interactive-examples/pull/369)),
  and Clarify a bit the initial-choice attribute
  ([PR 370](https://github.com/mdn/interactive-examples/pull/370)),
  from (first-time to interactive examples contributor)
  [SphinxKnight](https://github.com/SphinxKnight).

Other significant PRs:

- Fix bug 1063560: Change search output with locale=*
  ([Kuma PR 4580](https://github.com/mozilla/kuma/pull/4580)),
  from
  [Deep Bhattacharyya](https://github.com/coderick14).
- Fix Bug 1420288, only load GA if DNT disabled
  ([Kuma PR 4571](https://github.com/mozilla/kuma/pull/4571)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).


Planned for January
===

We're contining on existing projects like BCD in January, and starting some
larger projects that will start to ship in February.

<a name="cdn-dec-17">Prepare for a CDN
---
We've exhausted the easy solutions for increasing availability on MDN. We
believe the next step is to put developer.mozilla.org behind a
Content Distribution Network, or CDN. Once we have everything setup, most
requests won't even hit the Kuma engine, but instead will be handled by
caching servers around the world. We expect it to take 1 - 2 months before
we can get the majority of requests served by the CDN.

A first step is to reduce the page variants sent to anonymous users, so that
the CDN edge servers can handle most requests.
[Schalk Neethling](https://github.com/schalkneethling) has been removing waffle
flags or migrating them to switches over many PRs, such as
[PR 4561](https://github.com/mozilla/kuma/pull/4561).

In January, [Ryan Johnson](https://github.com/escattone) will start adding the
caching headers needed for the CDN to store and serve the pages without
contacting Kuma.

We believe a CDN will reduce downtime and alerts from increased traffic.
More importantly, we expect it will speed up MDN Web Docs for visitors
outside the US.

<a name="more-interactive-dec-17">Ship More Interactive Examples
---
We launched the interactive example editor on a dozen pilot pages, and the analytics
look good. Just before the holiday break, we decided we can
[ship the interactive example editor](https://discourse.mozilla.org/t/interactive-examples-on-mdn-are-shipping/23673)
to any MDN page. You can see it on
[CSS background-size](https://developer.mozilla.org/en-us/docs/web/css/background-size),
[Javascript Array.slice()](https://developer.mozilla.org/en-us/docs/web/javascript/reference/global_objects/array/slice),
and [more](https://developer.mozilla.org/en-us/search?locale=en-us&kumascript_macros=embedinteractiveexample&topic=none).

![background-size](
 {{ site.baseurl }}/public/images/kuma/2017-12-background-size.png
 "CSS demo of background size")
![array-slice](
 {{ site.baseurl }}/public/images/kuma/2017-12-array-slice.png
 "Javascript demo of array.slice()")

We have many more interactive examples ready to publish, including
[many JavaScript examples](https://github.com/mdn/interactive-examples/tree/master/live-examples/js-examples)
by [Mark Boas](https://github.com/maboa). We'll roll these and more out to MDN.
We'll also start on HTML interactive examples, and we're planning to ship them
in February. Follow
[mdn/interactive-examples](https://github.com/mdn/interactive-examples) to see
the progress and learn how to help.

<a name="django-dec-17">Update Django to 1.11
---
MDN Web Docs is built on top of Django. We're currently using Django 1.8, first
released in 2015. It is a
[Long-Term Release](https://www.djangoproject.com/download/#supported-versions)
(LTS) that will be supported with security updates until at least April 2018.
Django 1.11, released in 2017, is the new LTS release, and will be supported
until at least April 2020. In January, we'll focus on updating our code and
third-party libraries so that we can quickly make the 
[transition to 1.11](https://docs.djangoproject.com/en/1.11/howto/upgrade-version/).

For now, our plan is to stay on Django 1.11 until April 2019, when Django 2.2,
the next LTS release, is shipped.  Django 2 requires Python 3, and it may
take a lot of effort to update Kuma and switch to
[third-party libraries that support Python 3](http://py3readiness.org/). We'll
make a lot of progress during the 1.11 transition, and we'll monitor our Django
2 and Python 3 compatibility in 2018.

<a name="2018-dec-17">Plan for 2018
---
We have a lot of things we *have* to do in Q1 2018, such as the CDN and Django
1.11 update.  We postponed a detailed plan for 2018, and instead will spend
some of Q1 discussing goals and priorities. During our discussions in December,
a few themes came up.

For the MDN Web Docs product, the 2018 theme is **Reach**. We want to reach
more web developers with MDN Web Docs data, and earn a key place in developers'
workflows. Sometimes this means making developer.mozilla.org the best place to
find the information, and sometimes it means delivering the data where the
developer works. We're using interviews and surveys to learn more and design
the best experience for web developers.

For the technology side, the 2018 theme is **Simplicity**. There are many
seldom-used Kuma features that require a history lesson to explain. These make
it more complicated to maintain and improve the web site. We'd like to retire
some of these features, simplify others, and make it easier to work on the
code and data.  We have ideas around zone redirects, asset pipelines, and
translations, and we hope to implement these in 2018.

One thing that has gotten more complex in 2017 is code contribution. We're
implementing new features like
[browser-compat-data](https://github.com/mdn/browser-compat-data) and
[interactive-examples](https://github.com/mdn/interactive-examples) as their
own projects. Kuma is usually not the best place to contribute, and it can be
challenging to discover where to contribute. We're thinking through ways to
improve this in 2018, and to steer contributor's effort and enthusiasm where it
will have the biggest impact.
