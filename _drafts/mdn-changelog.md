---
layout: post
title: MDN Changelog for January 2018
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in January to the
[code, data, and tools](https://github.com/mdn/)
that support
[MDN Web Docs](https://developer.mozilla.org):

- [Completed CSS compatibility data migration and more](#css-bcd-jan-18)
- [Shipped a new method for declaring language preference](#lang-cookie-jan-18)
- [Increased availability of MDN](#mdn-perf-jan-18)
- [Shipped tweaks and fixes](#tweaks-jan-18)
  by merging 326 pull requests,
  including 67 pull requests
  from 27 new contributors.

Here's the plan for February:

- [Continue development projects](#continue-jan-18)

<!--more-->

Done in January
===

<a name="css-bcd-jan-18">Completed CSS Compatibility Data Migration and More
---
Thanks to [Daniel D. Beck](https://github.com/ddbeck) and his
[83 Pull Requests](https://github.com/mdn/browser-compat-data/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+merged%3A%222018-01-01..2018-01-31%22+author%3Addbeck),
the CSS compatibility data is migrated to the
[browser-compat-data](https://github.com/mdn/browser-compat-data) repository.
This finishes Daniel's current contract, and we hope to get his help again
soon.

The newly announced
[MDN Product Advisory
Board](https://hacks.mozilla.org/2018/01/introducing-the-mdn-product-advisory-board/)
supports the Browser Compatibility Data project, and members are working to
migrate more data. In January, we saw an increase in contributions, many from
first-time contributors.  The migration work jumped from 39% to 43% complete in
January. See the [contribution
guide](https://github.com/mdn/browser-compat-data/blob/master/CONTRIBUTING.md)
to learn how to help.

On January 23, we turned on the
[new browser compatability tables](https://discourse.mozilla.org/t/new-mdn-browser-compatibility-tables/24747)
for all users. The new presentation provides a good overview of feature support
across desktop and mobile browsers, as well as JavaScript run-time environments
like Node.js, while still letting implementors dive into the details.

[Florian Scholz](http://florianscholz.com/) promoted the project with a
[blog post](https://hacks.mozilla.org/2018/02/mdn-browser-compatibility-data/),
and highlighted the
[compat-report addon](https://addons.mozilla.org/en-US/firefox/addon/compat-report/)
by [Eduardo Bouças](https://twitter.com/eduardoboucas)
that uses the data to highlight compatibility issues in a developer tools tab.
Florian also gave a talk about the project on February 3 at
[FOSDEM 18](https://fosdem.org/2018/schedule/event/mozilla_mdn_browser_compat_data_project/).
We're excited to tell people about this new resource, and see what people will
do with this data.

![compat-report](
 {{ site.baseurl }}/public/images/kuma/2018-01-compat-report.png
 "Compatibility report on MozMEAO")


<a name="lang-cookie-jan-18">Shipped a New Method for Declaring Language Preference
---
If you use the language switcher on MDN, you'll now be asked if you want to
always view the site in that language. This was added by
[Safwan Rahman](https://github.com/safwanrahman) in
[PR 4321](https://github.com/mozilla/kuma/pull/4321).

![language-switcher](
 {{ site.baseurl }}/public/images/kuma/2018-01-lang-cookie.png
 "Language preference switcher dialog")

This preference goes into effect for our "locale-less" URLs. If you access
<https://developer.mozilla.org/docs/Web/HTML>, MDN uses your browser's
preferred language, as set by the
[Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language)
header. If it is set to ``Accept-Language: en-US,en;q=0.5``, then you'll get
the English page at
<https://developer.mozilla.org/en-US/docs/Web/HTML>, while
``Accept-Language: de-CH`` will send you to the German page at
<https://developer.mozilla.org/de/docs/Web/HTML>.
If you've set a preference with this new dialog box, the
``Accept-Language`` header will be ignored and you'll get your preferred
language for MDN.

This is useful for MDN visitors who like to browse the web in their native
language, but read MDN in English, but it doesn't fix the issue entirely.
If a search engine thinks you prefer German, for instance, it will pick the
German translations of MDN pages, and send you to
<https://developer.mozilla.org/de/docs/Web/HTML>. MDN respects the link and
shows the German page, and the new language preference is not used.

We hope this makes MDN a little easier to use, but more will be needed to
satisfy those who get the "wrong" page. I'm not convinced there is a solution
that will work for everyone.  I've suggested a web extension in
[bug 1432826](https://bugzilla.mozilla.org/show_bug.cgi?id=1432826), to allow
configurable redirects, but it is unclear if this is the right solution.
We'll keep thinking about translations, and adjusting to visitors' preferences.

<a name="mdn-perf-jan-18">Increased Availability of MDN
---
MDN easily serves millions of visitors a month, but struggles under some
traffic patterns, such as a single visitor requesting every page on the site.
We continue to make MDN more reliable despite these traffic spikes, using
several different strategies.

The most direct method is to limit the number of requests. We've updated our
rate limiting to return the HTTP 429 "Too Many Requests" code
([PR 4614](https://github.com/mozilla/kuma/pull/4614)), to more clearly
communicate when a client hits these limits.
[Dave Parfitt](https://github.com/metadave) automated bans for users making
thousands of requests a minute, which is much more than legitimate scrapers.

Another strategy is to reduce the database load for each request, so that high
traffic doesn't slow down the database and all the page views. We're reducing
database usage by changing how async processes store state
([PR 4615](https://github.com/mozilla/kuma/pull/4615)) and using long-lasting
database connections to reduce time spent establishing per-request connections
([PR 4644](https://github.com/mozilla/kuma/pull/4644)).
[Safwan Rahman](https://github.com/safwanrahman) took a close look at the
database usage for wiki pages, and made several changes to reduce both the
number of queries and the size of the data transmitted from the database
([PR 4630](https://github.com/mozilla/kuma/pull/4630)). All of these add up
to a 10% to 15% improvement in server response time from December's
performance.

![response-time](
 {{ site.baseurl }}/public/images/kuma/2018-01-response-time.png
 "New Relic response time after shipping PR 4630")

[Ryan Johnson](https://github.com/escattone) continued work on the long-term
solution, to serve MDN content from a CDN. This requires getting our caching
headers just right
([PR 4638](https://github.com/mozilla/kuma/pull/4638)).
We hope to start shipping this in February. At that point, a high-traffic user
may still slow down the servers, but most people will quickly get their content
from the CDN instead.

<a name="tweaks-jan-18">Shipped Tweaks and Fixes
---
There were 326 PRs merged in January:

- [156 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)
- [75 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)
- [44 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)
- [27 mdn/kumascript PRs](https://github.com/mdn/kumascript/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)
- [19 mozmeao/infra PRs](https://github.com/mozmeao/infra/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)
- [5 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&q=is:pr+is:closed+merged:"2018-01-01..2018-01-31"&utf8=✓)

67 of these were from first-time contributors:

- Update JS grammar compat data for Chrome (trailing commas for functions)
  ([BCD PR 732](https://github.com/mdn/browser-compat-data/pull/732)),
  from
  [Olivier Dony](https://github.com/odony).
- Add classes compatibility with respect to Node.js
  ([BCD PR 746](https://github.com/mdn/browser-compat-data/pull/746)),
  from
  [Marc-Aurèle DARCHE](https://github.com/madarche).
- Add compat data for CanvasCaptureMediaStream
  ([PR 829](https://github.com/mdn/browser-compat-data/pull/829)),
  CanvasGradient
  ([PR 830](https://github.com/mdn/browser-compat-data/pull/830)),
  CanvasPattern
  ([PR 832](https://github.com/mdn/browser-compat-data/pull/832)),
  CanvasRenderingContext2D
  ([PR 851](https://github.com/mdn/browser-compat-data/pull/851)),
  HTMLCanvasElement
  ([PR 880](https://github.com/mdn/browser-compat-data/pull/880)),
  ImageBitmap
  ([PR 883](https://github.com/mdn/browser-compat-data/pull/883)),
  ImageBitmapRenderingContext
  ([PR 885](https://github.com/mdn/browser-compat-data/pull/885)),
  ImageData
  ([PR 891](https://github.com/mdn/browser-compat-data/pull/891)),
  Path2D
  ([PR 893](https://github.com/mdn/browser-compat-data/pull/893)),
  and
  TextMetrics
  ([PR 894](https://github.com/mdn/browser-compat-data/pull/894)),
  from
  [Mark Boas](https://github.com/maboa)
  (first contributions to BCD).
- Fix "RGB" typo to "RGBA" for the hex RGBA spec
  ([BCD PR 835](https://github.com/mdn/browser-compat-data/pull/835)),
  from
  [Yuval Greenfield](https://github.com/ubershmekel).
- Update text-decoration-skip.json
  ([BCD PR 836](https://github.com/mdn/browser-compat-data/pull/836)),
  from
  [Paul Irish](https://github.com/paulirish).
- Add data for Samsung Internet to font-face.json
  ([BCD PR 840](https://github.com/mdn/browser-compat-data/pull/840)),
  from
  [Ada Rose Cannon](https://github.com/AdaRoseCannon).
- Fix a typo in css.properties.justify-content
  ([BCD PR 844](https://github.com/mdn/browser-compat-data/pull/844)),
  from
  [Simon Chan](https://github.com/yume-chan).
- Edge doesn't currently support requestBody for webRequest
  ([BCD PR 860](https://github.com/mdn/browser-compat-data/pull/860)),
  from
  [Neil Durbin](https://github.com/durbin).
- IE11 doesn't support Map(iterable) constructor
  ([BCD PR 874](https://github.com/mdn/browser-compat-data/pull/874)),
  from
  [Jeff-Mott-OR](https://github.com/Jeff-Mott-OR).
- Update break-word
  ([BCD PR 882](https://github.com/mdn/browser-compat-data/pull/882),
  [Data PR 164](https://github.com/mdn/data/pull/164), and
  [Interactive Examples PR 440](https://github.com/mdn/interactive-examples/pull/440)),
  from
  [CShepartd](https://github.com/CShepartd).
- nodejs ES module support flag info
  ([BCD PR 903](https://github.com/mdn/browser-compat-data/pull/903)),
  from
  [slikts](https://github.com/slikts).
- Fix parameter ordering Math.atan2 example
  ([Interactive Examples PR 385](https://github.com/mdn/interactive-examples/pull/385)),
  from
  [Rhys Howell](https://github.com/Anemy).
- Fixed the demo titles
  ([Interactive Examples PR 401](https://github.com/mdn/interactive-examples/pull/401)),
  from
  [Ayush Gupta](https://github.com/7ayushgupta).
- Allow an empty commit for travis deploy
  ([PR 410](https://github.com/mdn/interactive-examples/pull/410)),
  from
  [me](https://github.com/jwhitlock)
  (first contribution to Interactive Examples).
- Add demo for text-decoration-skip-ink
  ([Interactive Examples PR 411](https://github.com/mdn/interactive-examples/pull/411)),
  from
  [Paul Irish](https://github.com/paulirish).
- Typo fix
  ([PR 424](https://github.com/mdn/interactive-examples/pull/424)),
  Fix URL and missing comma
  ([PR 446](https://github.com/mdn/interactive-examples/pull/446)),
  Fix clipboard target ids
  ([PR 447](https://github.com/mdn/interactive-examples/pull/447)),
  Add `border-width` example
  ([PR 448](https://github.com/mdn/interactive-examples/pull/448)),
  Add `border-color` example
  ([PR 465](https://github.com/mdn/interactive-examples/pull/465)),
  Add `overflow-wrap` example
  ([PR 472](https://github.com/mdn/interactive-examples/pull/472)),
  Add `<angle>` example
  ([PR 473](https://github.com/mdn/interactive-examples/pull/473)),
  Update `border-style` example
  ([PR 474](https://github.com/mdn/interactive-examples/pull/474)),
  Add `text-transform` example
  ([PR 475](https://github.com/mdn/interactive-examples/pull/475)),
  Add `border-*-width` examples
  ([PR 499](https://github.com/mdn/interactive-examples/pull/499)),
  Add `border-*-color` examples
  ([PR 501](https://github.com/mdn/interactive-examples/pull/501)),
  Add `border-*-style` examples
  ([PR 504](https://github.com/mdn/interactive-examples/pull/504)),
  Add `border` examples
  ([PR 511](https://github.com/mdn/interactive-examples/pull/511)),
  Add `overflow-*` examples
  ([PR 513](https://github.com/mdn/interactive-examples/pull/513)),
  Add/update `background-position-*` examples
  ([PR 514](https://github.com/mdn/interactive-examples/pull/514)),
  and
  Add `text-decoration-color` example
  ([PR 516](https://github.com/mdn/interactive-examples/pull/516)),
  from
  [mfluehr](https://github.com/mfluehr)
  (first contributions to Interactive Examples).
- Add demo for Array.toString() and Array.unshift(), Fixes #421 and #422
  ([PR 427](https://github.com/mdn/interactive-examples/pull/427)),
  Add demo for Array.prototypes Fixes #420, #419
  ([PR 435](https://github.com/mdn/interactive-examples/pull/435)),
  and
  Add demo for Array.prototypes Fixes #417 and #416
  ([PR 439](https://github.com/mdn/interactive-examples/pull/439)),
  to Interactive Examples from
  [Dhruv Jain](https://github.com/maddhruv).
- console.log support for multiple arguments
  ([Interactive Examples PR 433](https://github.com/mdn/interactive-examples/pull/433)),
  from
  [Ivan Ng](https://github.com/qwIvan).
- Indents the break statements
  ([Interactive Examples PR 437](https://github.com/mdn/interactive-examples/pull/437)),
  from
  [Mike Lissner](https://github.com/mlissner).
- Enhance formatObject to support formatting actual object
  ([PR 451](https://github.com/mdn/interactive-examples/pull/451)),
  Add few examples
  ([PR 458](https://github.com/mdn/interactive-examples/pull/458)),
  Add .shorter css class for shorter JS examples
  ([PR 462](https://github.com/mdn/interactive-examples/pull/462)),
  and
  Reorganize live-examples folder
  ([PR 500](https://github.com/mdn/interactive-examples/pull/500)),
  to Interactive Examples from
  [Kenrick](https://github.com/kenrick95).
- Add interactive demo for Array.forEach(). Fixes #413
  ([PR 452](https://github.com/mdn/interactive-examples/pull/452)),
  and
  Add UTC set examples for Minutes,Milliseconds and Seconds
  ([PR 459](https://github.com/mdn/interactive-examples/pull/459)),
  to Interactive Examples from
  [Raymond Lochner](https://github.com/suknuk).
- Added examples for Array.prototype.reverse and  Array.prototype.keys
  ([Interactive Examples PR 460](https://github.com/mdn/interactive-examples/pull/460)),
  from
  [Anton Boyko](https://github.com/diablero13).
- Add line-height CSS example
  ([PR 485](https://github.com/mdn/interactive-examples/pull/485)),
  Add text-decoration-line CSS example
  ([PR 487](https://github.com/mdn/interactive-examples/pull/487)),
  Fixed some (all?) `data-clipboard-target` for CSS examples
  ([PR 488](https://github.com/mdn/interactive-examples/pull/488)),
  Add text-decoration-style CSS example
  ([PR 490](https://github.com/mdn/interactive-examples/pull/490)),
  Dynamically get clipboard button targets
  ([PR 491](https://github.com/mdn/interactive-examples/pull/491)),
  and
  Remove data-clipboard-target attribute
  ([PR 508](https://github.com/mdn/interactive-examples/pull/508)),
  to Interactive Examples from
  [Daniel Hickman](https://github.com/danielhickman).
- Fixed l10n-aware link to New_Compatibility_Tables_Beta
  ([PR 4609](https://github.com/mozilla/kuma/pull/4609)),
  and
  Fixed l10n-aware link to Troubleshooting article
  ([PR 4613](https://github.com/mozilla/kuma/pull/4613)),
  from
  [Віталій Крутько](https://github.com/asmforce)
  (first contributions to Kuma).
- Update LearnSidebar.ejs with French Translation
  ([KumaScript PR 550](https://github.com/mdn/kumascript/pull/550)),
  from
  [Kevin "Ilphrin" Pellet](https://github.com/Ilphrin).
- Fix typo in French translation for Spec2 macro
  ([KumaScript PR 556](https://github.com/mdn/kumascript/pull/556)),
  from
  [Victor Viale](https://github.com/Koroeskohr).
- Merge specification status, names and urls into a single source
  ([PR 557](https://github.com/mdn/kumascript/pull/557)),
  and
  Update statuses and URLs of a number of W3C specs
  ([PR 565](https://github.com/mdn/kumascript/pull/565)),
  to KumaScript from
  [Dominique Hazael-Massieux](https://github.com/dontcallmedom).
- Remove legacy `autocomplete` and `autocompleteerror` events
  ([PR 569](https://github.com/mdn/kumascript/pull/569)),
  from
  [Matt N.](https://github.com/mnoorenberghe)
  (first contribution to KumaScript).

Other significant PRs:

- Fix issue 546: Allow multiple flags (rename flag to flags)
  ([BCD PR 701](https://github.com/mdn/browser-compat-data/pull/701) and
  [KumaScript PR 438](https://github.com/mdn/kumascript/pull/438)),
  from
  [Florian Scholz](https://github.com/Elchi3).
- SharedArrayBuffer now unsupported to mitigate Spectre attack
  ([BCD PR 789](https://github.com/mdn/browser-compat-data/pull/789)),
  from
  [Florian Scholz](https://github.com/Elchi3).
- Add safari_ios validation
  ([BCD PR 831](https://github.com/mdn/browser-compat-data/pull/831)),
  from
  [Florian Scholz](https://github.com/Elchi3).
- Refactor browser data
  ([BCD PR 834](https://github.com/mdn/browser-compat-data/pull/834)),
  from
  [Florian Scholz](https://github.com/Elchi3).
- Further restrict identifiers
  ([BCD PR 915](https://github.com/mdn/browser-compat-data/pull/915)),
  from
  [Florian Scholz](https://github.com/Elchi3).
- Adds config for welcome bot
  ([Interactive Examples PR 407](https://github.com/mdn/interactive-examples/pull/407)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).
- Disables interactive examples for the currently disabled SharedArrayBuffer
  ([Interactive Examples PR 430](https://github.com/mdn/interactive-examples/pull/430)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).
- [Bug 1308322](https://bugzilla.mozilla.org/show_bug.cgi?id=1308322): 
  Upgrade to selenium 3.x
  ([Kuma PR 4195](https://github.com/mozilla/kuma/pull/4195)),
  from
  [me](https://github.com/jwhitlock).
- Add icons in case of support ranges
  ([KumaScript PR 548](https://github.com/mdn/kumascript/pull/548)),
  from
  [Florian Scholz](https://github.com/Elchi3).

Planned for February
===

<a name="plan1-jan-18">Continue Development Projects
---
In February, we'll continue working on our January projects. Our plans include:

* Converting more compatibility data
* Serving developer.mozilla.org from a CDN
* Updating third-party libraries for compatibility with Django 1.11
* Designing interactive examples for more complex scenarios
* Preparing for a team meeting and "Hack on MDN" event in March

See the
[December report](https://mozilla.github.io/meao/2018/01/08/kuma-report/#planned-for-january)
for more information on these projects.
