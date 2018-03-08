---
layout: post
title: MDN Changelog for February 2018
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in February to the
[code, data, and tools](https://github.com/mdn/)
that support
[MDN Web Docs](https://developer.mozilla.org):

- [Migrated 14% of compatibility data](#bcd-feb-18), leaping to 57% completion
  for the conversion effort.
- [Improved and extended interactive examples](#ie-feb-18)
- [Prepared for a CDN and Django 1.11](#kuma-feb-18)
- [Shipped tweaks and fixes](#tweaks-feb-18)
  by merging 413 pull requests,
  including 147 pull requests
  from 47 new contributors.

Here's the plan for March:

- [Move developers to Emerging Technologies](#et-feb-18)
- [Meet in Paris for Hack on MDN](#paris-feb-18)
- [Evaluate proposals for a performance audit](#rfp-performace-feb-18)

<!--more-->

Done in February
===

<a name="bcd-feb-18">Migrated 14% of compatibility data</a>
---
In February, we asked the MDN community to help convert compatibility data
to the [browser-compat-data](https://github.com/mdn/browser-compat-data/)
repository. [Florian Scholz](https://github.com/Elchi3) led this effort,
starting with a conference talk and blog post
[last month](https://mozilla.github.io/meao/#css-bcd-jan-18). He created
[GitHub issues](https://github.com/mdn/browser-compat-data/labels/help%20wanted)
to suggest migration tasks, and
[added](https://github.com/mdn/kumascript/pull/585) a
[call to action](https://developer.mozilla.org/en-US/docs/MDN/Contribute/Structures/Compatibility_tables)
on the old pages:

![call-to-action](
 {{ site.baseurl }}/public/images/kuma/2018-02-call-to-action.png
 "Call to action to help convert tables")

The response from the community has been overwhelming. There were 203 PRs
merged in February, and 96 were from 23 first-time contributors. Existing
contributors such as [Mark Boas](https://github.com/maboa),
[Chris Mills](https://github.com/chrisdavidmills), and
[wbamberg](https://github.com/wbamberg) kept up their January pace.
The PRs were reviewed for the correctness of the conversion as well as
ensuring the data was up to date, and Florian,
[Jean-Yves Perrier](https://github.com/teoli2003), and
[Joe Medley](https://github.com/jpmedley) have done the most reviews.
In February, the project jumped from 43% to 57% of the data converted,
and the data is better than ever.

There are two new tools using the data.
[SphinxKnight](https://github.com/SphinxKnight) is working on
[compat-tester](https://github.com/SphinxKnight/compat-tester), which scans
an HTML, CSS, or Javascript file for compatibility issues with a user-defined
set of browsers. [K3N](https://github.com/epistemex) is working on
[mdncomp](https://github.com/epistemex/mdncomp), which displays compatibility
data on the command line:

![mdncomp](
 {{ site.baseurl }}/public/images/kuma/2018-02-mdncomp.png
 "mdncomp on the command line")

If you have a project using the data, let us know about it!

<a name="ie-feb-18">Improved and Extended Interactive Examples</a>
---
We continue to improve and expand the interactive examples, such as a
[clip-path](https://developer.mozilla.org/en-US/docs/Web/CSS/clip-path)
demo from [Rachel Andrew](https://github.com/rachelandrew):

![clip-path](
 {{ site.baseurl }}/public/images/kuma/2018-02-clip-path.png
 "Demo of the clip-path attribute with an ellipse setting")

We're expanding the framework to allow for HTML examples, which often
need a mix of HTML and CSS to be interesting. Like previous efforts,
we're using
[user testing](https://discourse.mozilla.org/t/html-interactive-editor-user-testing/26368)
to develop this feature. We show the work-in-progress, like the
[&lt;table&gt; demo](https://developer.mozilla.org/en-US/docs/User:wbamberg/HTML_editor_user_test_pages/table),
to an individual developer, watch how the demo is used and ask for feedback,
and then iterate on the design and implementation.

![html-table](
 {{ site.baseurl }}/public/images/kuma/2018-02-html-table.png
 "Demo of the HTML table element with styling")

The demos have gone well, and the team will firm up the implementation and
write more examples to prepare for production. The team will also work on
expanding test coverage and formalizing the build tools in a new package.

<a name="kuma-feb-18">Prepared for a CDN and Django 1.11</a>
---
We made
[many changes last month](https://mozilla.github.io/meao/2018/02/07/mdn-changelog/#mdn-perf-jan-18)
to improve the performance and reliability of MDN. They worked, and we've
entered a new period of calm. We've had a month without 3 AM downtime or
performance alerts, for the first time since the move to AWS. The site is
responding more smoothly, and easily handling MDN's traffic.

![new-relic-calm](
 {{ site.baseurl }}/public/images/kuma/2018-02-new-relic-calm.png
 "The right side shows how things have calmed down.")

This has freed us to focus on longer term fixes and on the goals for the
quarter.  One of those is to serve MDN from behind a CDN, which will further
reduce server load and may have a huge impact on response time.
[Ryan Johnson](https://github.com/escattone) is getting the code ready.
He switched to Django's middleware for handling ``ETag`` creation
([PR 4647](https://github.com/mozilla/kuma/pull/4647)), which allowed him to
remove some buggy caching code
([PR 4648](https://github.com/mozilla/kuma/pull/4648)). Ryan is now working
through the many endpoints, adding caching headers and cleaning up tests
([PR 4676](https://github.com/mozilla/kuma/pull/4676),
[PR 4677](https://github.com/mozilla/kuma/pull/4677), and others). Once this
work is done, we'll add the CDN that will cache content based on the directives
in the headers.

My focus has been on the
[Django 1.11 upgrade](https://docs.djangoproject.com/en/1.11/releases/1.11/),
since
[Django 1.8 is scheduled to lose support in April](https://www.djangoproject.com/download/#supported-versions).
This requires updating third-party libraries like ``django-tidings``
([PR 4660](https://github.com/mozilla/kuma/pull/4660)) and
``djangorestframework``
([PR 4664](https://github.com/mozilla/kuma/pull/4664)
from [Safwan Rahman](https://github.com/safwanrahman)). We're moving away
from other requirements, such as dropping ``dbgettext``
([PR 4669](https://github.com/mozilla/kuma/pull/4669)). We've taken care of
the most obvious upgrades, but there are 142,000 lines of Python in our
libraries, so we expect more surprises as we get closer to the switch.

Once the libraries are compatible with Django 1.11, the remaining issues
will be with the Kuma codebase. Some changes are small and easy,
such as a one-liner in [PR 4684](https://github.com/mozilla/kuma/pull/4684).
Some will be quite large. Our code that serves up locale-specific content,
such as
[reverse](https://github.com/mozilla/kuma/blob/da9245976da5a404dcb96976942ff701600cf5ee/kuma/core/urlresolvers.py#L36-L72)
and
[LocaleURLMiddleware](https://github.com/mozilla/kuma/blob/da9245976da5a404dcb96976942ff701600cf5ee/kuma/core/middleware.py#L20-L82),
are incompatible, and we'll have to swap some of our
[oldest code](https://github.com/mozilla/kuma/commit/d03b6f87c91f140576a371e8d3ff41a1dd21cd15)
for
[Django's version](https://docs.djangoproject.com/en/1.11/ref/middleware/#module-django.middleware.locale).

<a name="tweaks-feb-18">Shipped Tweaks and Fixes</a>
---
There were 413 PRs merged in February:

- [203 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")
- [89 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")
- [63 mdn/kumascript PRs](https://github.com/mdn/kumascript/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")
- [36 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")
- [11 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")
- [11 mozmeao/infra PRs](https://github.com/mozmeao/infra/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28")

147 of these were from first-time contributors:

- Update String method support in Node.js
  ([BCD PR 938](https://github.com/mdn/browser-compat-data/pull/938)),
  from
  [Keith Cirkel](https://github.com/keithamus).
- Add Edge support of ``grid-template-columns:repeat()``
  ([BCD PR 939](https://github.com/mdn/browser-compat-data/pull/939)),
  from
  [Timmy Kokke](https://github.com/sorskoot).
- `animation-name` is supported since Edge 12
  ([BCD PR 951](https://github.com/mdn/browser-compat-data/pull/951)),
  from
  [Borek Bernard](https://github.com/borekb).
- Add RTCCertificate compat data
  ([PR 952](https://github.com/mdn/browser-compat-data/pull/952)),
 Adding compat data for RTCConfiguration
  ([PR 958](https://github.com/mdn/browser-compat-data/pull/958)),
  and
  [48 more PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:bunnybooboo)
  to BCD from
  [David Ross](https://github.com/bunnybooboo).
- Change ordering for String.prototype.includes
  ([BCD PR 953](https://github.com/mdn/browser-compat-data/pull/953)),
  from
  [Todor Gaidarov](https://github.com/toshotosho).
- Added chrome and opera support of min-height:fill-available
  ([BCD PR 962](https://github.com/mdn/browser-compat-data/pull/962)),
  from
  [Abel Serrano Juste](https://github.com/Akronix).
- String.prototype.includes is incorrectly marked as deprecated
  ([BCD PR 974](https://github.com/mdn/browser-compat-data/pull/974)),
  from
  [Patrick Westerhoff](https://github.com/poke).
- Add compat data for Animation
  ([PR 975](https://github.com/mdn/browser-compat-data/pull/975)),
 Adding compat data for Blob
  ([PR 988](https://github.com/mdn/browser-compat-data/pull/988)),
  and
  [6 more PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:CalmBit)
  to BCD from
  [Ethan Brooks](https://github.com/CalmBit).
- Adds compat data for AnimationEffectTiming
  ([PR 1000](https://github.com/mdn/browser-compat-data/pull/1000)),
 Adds compat data for AnimationEffectTimingReadOnly
  ([PR 1001](https://github.com/mdn/browser-compat-data/pull/1001)),
  and
  [6 more PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:bennypowers)
  to BCD from
  [Benny Powers](https://github.com/bennypowers).
- ``Array.prototype.values()`` shipped in FF and Chrome
  ([BCD PR 1014](https://github.com/mdn/browser-compat-data/pull/1014)),
  from
  [Serg Hospodarets](https://github.com/malyw).
- Add comp data for BroadcastChannel
  ([PR 1026](https://github.com/mdn/browser-compat-data/pull/1026)),
 add compat data for BudgetService and BudgetState
  ([PR 1028](https://github.com/mdn/browser-compat-data/pull/1028)),
  and
  [6 more PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:gsouquet)
  to BCD from
  [Germain](https://github.com/gsouquet).
- Update referrer policy compat data to note some values as standard
  ([PR 1032](https://github.com/mdn/browser-compat-data/pull/1032)),
  from
  [David Bruant](https://github.com/DavidBruant)
  (first contribution to BCD).
- Adding compat data for HTML global attributes
  ([BCD PR 1089](https://github.com/mdn/browser-compat-data/pull/1089)),
  from
  [Sebastian Martin](https://github.com/frittate).
- Add Animation.updatePlaybackRate
  ([BCD PR 1106](https://github.com/mdn/browser-compat-data/pull/1106)),
  from
  [Brian Birtles](https://github.com/birtles).
- Add PerformanceNavigationTiming
  ([PR 1117](https://github.com/mdn/browser-compat-data/pull/1117)),
  Add PerformanceResourceTiming
  ([PR 1118](https://github.com/mdn/browser-compat-data/pull/1118)),
  and
  Add NavigationPreloadManager
  ([PR 1194](https://github.com/mdn/browser-compat-data/pull/1194)),
  to BCD from
  [ExE Boss](https://github.com/ExE-Boss).
- Add nodejs compat for Object.entries()
  ([PR 1129](https://github.com/mdn/browser-compat-data/pull/1129)),
  and
  Add nodejs compat for Object.getOwnPropertyDescriptors()
  ([PR 1131](https://github.com/mdn/browser-compat-data/pull/1131)),
  to BCD from
  [Antoine Neff](https://github.com/antoineneff).
- Correct support for css `break-` properties
  ([BCD PR 1133](https://github.com/mdn/browser-compat-data/pull/1133)),
  from
  [shrpne](https://github.com/shrpne).
- Update npm dependencies install command
  ([BCD PR 1136](https://github.com/mdn/browser-compat-data/pull/1136)),
  from
  [Lubos](https://github.com/lmenus).
- Add compat data for Console
  ([BCD PR 1145](https://github.com/mdn/browser-compat-data/pull/1145)),
  from
  [Adrian Heng](https://github.com/Aetheus).
- Added Edge version that supports exponentiation
  ([BCD PR 1153](https://github.com/mdn/browser-compat-data/pull/1153)),
  from
  [Vijay Koushik, S.](https://github.com/svijaykoushik).
- Updated versions for node async/await
  ([BCD PR 1182](https://github.com/mdn/browser-compat-data/pull/1182)),
  from
  [Chris Weed](https://github.com/Kikketer).
- HTMLHtmlElement compat data
  ([BCD PR 1201](https://github.com/mdn/browser-compat-data/pull/1201)),
  from
  [Augusto Quadros](https://github.com/awquadros).
- adding compat data for HTMLHRElement
  ([BCD PR 1202](https://github.com/mdn/browser-compat-data/pull/1202)),
  from
  [Raju Dasa](https://github.com/RajuDasa).
- Adding flex-wrap example
  ([PR 524](https://github.com/mdn/interactive-examples/pull/524)),
 Flex examples
  ([PR 558](https://github.com/mdn/interactive-examples/pull/558)),
  and
  [8 more PRs](https://github.com/mdn/interactive-examples/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:rachelandrew)
  to Interactive Examples from
  [Rachel Andrew](https://github.com/rachelandrew).
- Update class expression example
  ([Interactive Examples PR 539](https://github.com/mdn/interactive-examples/pull/539)),
  from
  [Xi Zhang](https://github.com/aefhm).
- Fix typo
  ([Interactive Examples PR 540](https://github.com/mdn/interactive-examples/pull/540)),
  from
  [Hidde de Vries](https://github.com/hidde).
- Adding border radius example with recommended changes.
  ([PR 546](https://github.com/mdn/interactive-examples/pull/546)),
  Adding list-style css example.
  ([PR 547](https://github.com/mdn/interactive-examples/pull/547)),
  and
  Adding supporting samples for border corners to support request #502
  ([PR 553](https://github.com/mdn/interactive-examples/pull/553)),
  to Interactive Examples from
  [Helmut Granda](https://github.com/helmutgranda).
- Add `list-style-position` css example
  ([Interactive Examples PR 559](https://github.com/mdn/interactive-examples/pull/559)),
  from
  [Darek Antkowicz](https://github.com/d7ark).
- add css font-size examples
  ([Interactive Examples PR 567](https://github.com/mdn/interactive-examples/pull/567)),
  from
  [Ben Stokes](https://github.com/benji1304).
- CSS examples: example for z-index
  ([Interactive Examples PR 570](https://github.com/mdn/interactive-examples/pull/570)),
  from
  [Veekas Shrivastava](https://github.com/veekas).
- CSS interactive examples: Add example for width.
  ([Interactive Examples PR 571](https://github.com/mdn/interactive-examples/pull/571)),
  from
  [Dominic Duffin](https://github.com/dominicduffin1).
- Add resize example
  ([Interactive Examples PR 582](https://github.com/mdn/interactive-examples/pull/582)),
  from
  [Ben](https://github.com/bromy).
- Add example for list-style-type CSS property
  ([PR 594](https://github.com/mdn/interactive-examples/pull/594)),
 Add example for list-style-image CSS property
  ([PR 600](https://github.com/mdn/interactive-examples/pull/600)),
  and
  [9 more PRs](https://github.com/mdn/interactive-examples/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:ddbeck)
  from
  [Daniel D. Beck](https://github.com/ddbeck)
  (first contributions to Interactive Examples).
- feat: adds cursor interactive examples
  ([Interactive Examples PR 597](https://github.com/mdn/interactive-examples/pull/597)),
  from
  [Brian Macdonald](https://github.com/brianlmacdonald).
- Issue 561 Added example for vertical-align in text context
  ([Interactive Examples PR 606](https://github.com/mdn/interactive-examples/pull/606)),
  from
  [Laurent Lyaudet](https://github.com/LLyaudet).
- Browser Kompatibilität -&gt; Browserkompatibilität
  ([PR 570](https://github.com/mdn/kumascript/pull/570)),
  add german translation
  ([PR 617](https://github.com/mdn/kumascript/pull/617)),
  and
  add german translation
  ([PR 618](https://github.com/mdn/kumascript/pull/618)),
  to KumaScript from
  [schlagi123](https://github.com/schlagi123).
- Add WebAuthn spec
  ([PR 574](https://github.com/mdn/kumascript/pull/574)),
  and
  Add Web Authentication API
  ([PR 615](https://github.com/mdn/kumascript/pull/615)),
  to KumaScript from
  [Adam Powers](https://github.com/apowers313).
- Update Russian translations
  ([KumaScript PR 578](https://github.com/mdn/kumascript/pull/578)),
  from
  [Dmitry Murzin](https://github.com/dima74).
- Add Arabic language to ``LocalizationStatusl10nPriority`` macro
  ([KumaScript PR 586](https://github.com/mdn/kumascript/pull/586)),
  from
  [Ahmad Nourallah](https://github.com/ahmadnourallah).
- Update Japanese translation
  ([PR 590](https://github.com/mdn/kumascript/pull/590)),
  Added Japanese translation
  ([PR 591](https://github.com/mdn/kumascript/pull/591)),
  and
  Added Japanese translations for ``CompatTable``.
  ([PR 593](https://github.com/mdn/kumascript/pull/593)),
  to KumaScript from
  [Masahiro Fujimoto](https://github.com/mfuji09).
- Modify Japanese translation of spec status
  ([KumaScript PR 596](https://github.com/mdn/kumascript/pull/596)),
  from
  [Momdo Nakamura](https://github.com/momdo).
- Adding missing fr strings
  ([KumaScript PR 604](https://github.com/mdn/kumascript/pull/604)),
  from
  [Alphal10n](https://github.com/Alphal10n).
- added Chinese simplified translation for ``learnsidebar``
  ([KumaScript PR 637](https://github.com/mdn/kumascript/pull/637)),
  from
  [Allan Simon](https://github.com/allan-simon).
- fix bug 1419466 - added Jinja2 extension of translating the 404 page
  ([Kuma PR 4655](https://github.com/mozilla/kuma/pull/4655)),
  from
  [Hritvi Bhandari](https://github.com/hritvi).
- bug 951180: Position labels after checkboxes
  ([Kuma PR 4682](https://github.com/mozilla/kuma/pull/4682)),
  from
  [Donovan Glover](https://github.com/GloverDonovan).
- Microsoft CSS changes
  ([Data PR 156](https://github.com/mdn/data/pull/156)),
  from
  [jameshkramer](https://github.com/jameshkramer).
- Update align-items to match current spec
  ([PR 170](https://github.com/mdn/data/pull/170)),
  from
  [Michael[tm] Smith](https://github.com/sideshowbarker)
  (first contribution to Data).
- Correct and add some Japanese translations
  ([Data PR 175](https://github.com/mdn/data/pull/175)),
  from
  [Masahiro Fujimoto](https://github.com/mfuji09).

Other significant PRs:

- Delete ``suivant`` macro,
  ([PR 582](https://github.com/mdn/kumascript/pull/582)),
  ``AnteriorSiguiente.ejs``
  ([PR 587](https://github.com/mdn/kumascript/pull/587)),
  and 
  [27 more macro deletion PRs](https://github.com/mdn/kumascript/pulls?page=1&utf8=✓&q=is:pr+is:closed+merged:"2018-02-01..2018-02-28"+author:SphinxKnight)
  from
  [SphinxKnight](https://github.com/SphinxKnight).
- &#91;Bug 1434690&#93; Use different favicon on staging and development
  ([Kuma PR 4650](https://github.com/mozilla/kuma/pull/4650)),
  from
  [Safwan Rahman](https://github.com/safwanrahman).
- bug 957802: Add Code of Conduct, Update Contributing doc
  ([Kuma PR 4674](https://github.com/mozilla/kuma/pull/4674)),
  from
  [me](https://github.com/jwhitlock).
- Fix bug 1434558, swap search and toolbox components
  ([Kuma PR 4656](https://github.com/mozilla/kuma/pull/4656)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).
  Check that your profile image still works with round photos!
  ![user-search](
   {{ site.baseurl }}/public/images/kuma/2018-02-user-search.png
   "User swapped with search, using round photos.")
- update mdn backup cron image version + docs
  ([Infra PR 719](https://github.com/mozmeao/infra/pull/719)),
  from
  [Dave Parfitt](https://github.com/metadave).

Planned for March
===
We'll continue with the compatibility migration, interactive examples, the CDN,
and the Django 1.11 migration in March.

<a name="et-feb-18">Move developers to Emerging Technologies</a>
---
Starting March 2, the MDN developers move from Marketing to Emerging
Technologies.  We'll be working on the details of this transition in March and
the coming months. That will include planning a infrastructure transition, and
finding a new home for the MDN Changelog.

[Stephanie Hobson](https://github.com/stephaniehobson) and I joined Marketing
Engineering and Operations in March 2016, back when it was still Engagement
Engineering. EE was already responsible for
[50% of Mozilla's web traffic](https://www.alexa.com/siteinfo/mozilla.org#subdomain-panel)
with [www.mozilla.org](https://www.mozilla.org/en-US/), and adding
[support.mozilla.org](https://support.mozilla.org/en-US/) (34%) and
[developer.mozilla.org](https://developer.mozilla.org/en-US) (16%) put
99% of Mozilla's web presence under one engineering group. MDN
benefited from this amazing team in many ways:

* [Josh Mize](https://github.com/jgmize) led the effort to integrate MDN into
  the marketing technology and processes. He helped with our move to
  Docker-based development and deployment, implemented
  [demo deploys](https://github.com/mozilla/kuma/pull/4121), advocated for
  a read-only and statically-generated deployment, and worked out details of
  the go-to-AWS strategy, such as file serving and the master database
  transfer. Josh keeps up to date on the infrastructure community, and knows
  what tech is reliable, what the community is excited about, and what the
  next best practices will be.
* [Dave Parfitt](https://github.com/metadave) did a lot of the heavy lifting on
  the AWS transition, from
  [demo instances](https://github.com/mozilla/kuma/pull/4127), through
  maintenance mode and staging deployments, and all the way to a smooth
  production deployment. He
  [figured out database initialization](https://github.com/mozilla/kuma/pull/4153),
  [implemented the redirects](https://github.com/mozilla/kuma/pull/4220), and
  tackled the
  [dark corners of unicode filenames](https://github.com/mozilla/kuma/pull/4153).
  He consistently does what need to be done, then goes above and beyond by
  refining the process, writing excellent documentation, and automating
  whenever possible.
* [Jon Petto](https://github.com/jpetto) introduced and integrated
  [Traffic Cop](https://mozilla.github.io/meao/2017/01/16/traffic-cop/),
  allowing us to experiment with in-content changes in a lightweight, secure
  way.
* [Giorgos Logiotatidis](https://github.com/glogiotatidis)'s
  [Jenkins scripts](https://github.com/mozmeao/jenkins-pipeline) and workflows
  are the foundation of
  [MDN's Jenkins integration](https://github.com/mozilla/kuma/tree/master/Jenkinsfiles),
  used to automate our tests and AWS deployments.
* [Paul McLanahan](https://github.com/pmac) helped review PRs when we had a
  single backend developer. His experience migrating
  [bedrock](https://github.com/mozilla/bedrock) to AWS was invaluable, and
  his battle-tested
  [django-redirect-urls](https://github.com/pmac/django-redirect-urls) made it
  possible to migrate away from Apache and get 10 years of redirects under
  control.
* [Schalk Neethling](https://github.com/schalkneethling) reviewed front-end
  code when we were down to one front-end developer. He implemented the
  [interactive examples](https://github.com/mdn/interactive-examples) from
  prototype to production, and joined the MDN team when
  [Stephanie Hobson](https://github.com/stephaniehobson)
  [transitioned to bedrock](https://mozilla.github.io/meao/2018/01/08/kuma-report/#stephanie-dec-17).
* [Ben Sternthal](https://github.com/bensternthal) made the transition
  into Marketing possible. He made us feel welcome from day one, hired
  [some amazing contractors](https://groups.google.com/d/msg/mozilla.dev.mdn/phVYeWfRlWc/A8PWb1IxEAAJ)
  to help with the dark days of the
  [2016 spam attack](https://wiki.mozilla.org/MDN/Projects/SPAM_Fight), hired
  [Ryan Johnson](https://github.com/escattone), and
  worked for the resources and support to move to AWS. He created a space where
  developers could talk about what is important to us, where we spent time
  and effort on technical improvements and career advancement, and where
  technical excellence was balanced with features and experiments.

MDN is on a firmer foundation after the time spent in MozMEAO, and is ready
for the next chapter in its 13 year history.

Ryan Johnson, Schalk Neethling, and I will join the Advanced Development team
in Emerging Technologies, reporting to
[Faramarz Rashed](https://twitter.com/frashed). The Advanced Development team
has been working on various ET projects, most recently
[Project Things](https://blog.mozilla.org/blog/2018/02/06/announcing-project-things-open-framework-connecting-devices-web/),
an Internet of Things (IoT) project that is focused on decentralization,
security, privacy, and interoperability. It's a team that is focused on
getting fresh technology into users' hands. This is a great environment for
the next phase of MDN, as we build on the more stable foundation and expand our
reach.

<a name="paris-feb-18">Meet in Paris for Hack on MDN</a>
---
We're traveling to the [Mozilla Paris Office](https://wiki.mozilla.org/Paris)
in March. We'll have team meetings on Tuesday, March 13 through Thursday,
March 15, to plan for the next three months and beyond.

From Friday, March 16 through Sunday, March 18, we'll have the third
[Hack on MDN](https://wiki.mozilla.org/MDN/Hack_on_MDN) event. The last one
was in
[2015 in Berlin](https://blog.mozilla.org/community/2015/04/17/a-highly-productive-hack-on-mdn-weekend-in-berlin/),
and the team is excited to return to this format. The focus of the Paris
event will be the
[Browser Compat Data project](https://github.com/mdn/browser-compat-data).
We expect to build some tools using the data, alternative displays of
compat information, and improve the migration and review processes.

<a name="rfp-performance-feb-18">Evaluate Proposals for a Performance Audit</a>
---
One of our goals for the year is to improve page load times on MDN. We're
building on a similar SEO project last year, and looking for an external
expert to measure MDN's performance and recommend next steps. Take a look at
our
[Request for Proposal](https://docs.google.com/document/d/1Q-6PfrqjPRQnA4oq6Wc4MQNibEAxiG4xUUUjpE0NDdQ/edit?usp=sharing).
We plan to select the top bidders by March 30, 2018.
