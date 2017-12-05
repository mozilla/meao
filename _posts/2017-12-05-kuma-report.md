---
layout: post
title: Kuma Report, November 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in November in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- [Shipped the first 21 interactive examples](#interactive-nov-2017)
- [Added browser versions, <code>list-style-type</code>, and even more Browser Compatibility Data](#bcd-nov-2017)
- [Shipped a sticky table of contents and other article improvements](#article-nov-2017)
- [Improved MDN in AWS and Kubernetes](#aws-nov-2017)
- [Shipped tweaks and fixes](#tweaks-nov-2017) by merging 260 pull requests,
  including 33 pull requests from 27 new contributors.

We're planning on [more of the same](#next-nov-2017) for December.

<!--more-->

Done in November
===

<a name="interactive-nov-2017">Shipped the First Interactive Examples
---
We've launched the new interactive examples on
[20+ pages](https://developer.mozilla.org/en-US/search?locale=en-US&kumascript_macros=EmbedInteractiveExample&topic=none).
Try them out on the pages for the
[CSS property box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow)
and the
[JavaScript method Array.slice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice).

![box-shadow example]({{ site.baseurl }}/public/images/kuma/2017-11-box-shadow.png
                      "CSS Demo of Box Shadow")

We're monitoring the page load impact of this limited rollout,
and if the results are good, we have another
[400 examples](https://github.com/mdn/interactive-examples) ready to go,
thanks to [Mark Boas](https://github.com/maboa) and others. Mark also
added a
[JavaScript Interactive Examples Contributing Guide](https://github.com/mdn/interactive-examples/blob/master/JS-Example-Guide.md),
so that contributors can create even more.

We want the examples to be as fast as possible.
[Schalk Neethling](https://github.com/schalkneethling) improved
the page load speed of the <code>&lt;iframe&gt;</code> by using preload
URLs
([PR 4537](https://github.com/mozilla/kuma/pull/4537)).
[Stephanie Hobson](https://github.com/stephaniehobson) and Schalk dived into
HTTP/2, and identified <code>require.js</code> as a potential issue for this
protocol ([Kuma PR 4521](https://github.com/mozilla/kuma/pull/4521) and
[Interactive Examples PR 329](https://github.com/mdn/interactive-examples/pull/329)).
[Josh Mize](https://github.com/jgmize) added appropriate
caching headers for the examples and static assets
([PR 326](https://github.com/mdn/interactive-examples/pull/326)).

For the next level of speed gains, we'll need to speed up the MDN pages
themselves. One possibility is to serve developer.mozilla.org from a CDN,
which will require big changes to make pages more cacheable. One issue is
[waffle flags](https://kuma.readthedocs.io/en/latest/feature-toggles.html),
which allow us to experiment with per-user changes, at the cost of making pages
uncacheable.  Schalk has made steady progress in eliminating inactive waffle
flag experiments, and this work will continue into December.

<a name="bcd-nov-2017">Continued Migration of Browser Compatibility Data
---
The [Browser Compatibility Data](https://github.com/mdn/browser-compat-data/)
project was the most active MDN project in November. 36.6% of the MDN pages
(2284 total) have been converted. Here are some highlights:

<ol style="list-style-type: georgian">
  <li>Imported more CSS data, such as the huge list of allowed values for the
      <code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type">list-style-type</a></code>
      property (this list uses <code>georgian</code>).
      This property alone required 7 PRs, starting with
      <a href="https://github.com/mdn/browser-compat-data/pull/576">PR 576</a>.
      <a href="https://github.com/ddbeck">Daniel D. Beck</a> submitted 32 CSS
      PRs that were merged in November, and is making good progress on
      converting CSS data.
  </li>
  <li>Added browser and version validation, a month-long effort in
      <a href="https://github.com/mdn/browser-compat-data/pull/439">PR 439</a>
      from
      <a href="https://github.com/Elchi3">Florian Scholz</a> and
      <a href="https://github.com/teoli2003">Jean-Yves Perrier</a>.
  </li>
  <li>Added a <code>runtime_flag</code> for features that can be enabled at
      browser startup
      (<a href="https://github.com/mdn/browser-compat-data/pull/615">PR 615</a>
      from
      <a href="https://github.com/Elchi3">Florian Scholz</a>).
  </li>
  <li>Add the first compatibility data for Samsung Internet for Android
      (<a href="https://github.com/mdn/browser-compat-data/pull/657">PR 657</a>
      from first-time contributor
      <a href="https://github.com/poshaughnessy">Peter O'Shaughnessy</a>).
  </li>
  <li>Shipped the new compatibility table to beta users.
      <a href="https://github.com/stephaniehobson">Stephanie Hobson</a>
      resurrected a design that had been through a few rounds of user testing
      (<a href="https://github.com/mozilla/kuma/pull/4436">PR 4436</a>),
      and has made further improvements such as augmenting colors with
      gradients
      (<a href="https://github.com/mozilla/kuma/pull/4511">PR 4511</a>).
      For more details and to give us feedback, see
      <a href="https://discourse.mozilla.org/t/beta-testing-new-compatability-tables/21269">Beta Testing New Compatability Tables</a>
      on Discourse.
  </li>
</ol>

![New Browser Compatibiility Table](
 {{ site.baseurl }}/public/images/kuma/2017-11-new-bc-table.png
 "New Browser Compatibility Table, showing gradients with colors.")

<a name="article-nov-2017">Sticky Table of Contents and Other Article Improvements
---
We shipped some additional article improvements in November.

The new table of contents is limited to the top-level headings, and "sticks" to
the top of the window at desktop sizes, showing where you are in a document and
allowing fast navigation ([PR 4510](https://github.com/mozilla/kuma/pull/4510)
from [Stephanie Hobson](https://github.com/stephaniehobson)).

![Sticky Table of Contents](
 {{ site.baseurl }}/public/images/kuma/2017-11-sticky-toc.png
 "Table of Contents with Specifications highlighted")

The breadcrumbs (showing where you are in the page hierarchy) have moved to the
sidebar, and now has [schema.org](https://schema.org/) metadata tags.
Stephanie also refreshed the style of the sidebar links.

![Breadcrumbs and Quick Links](
 {{ site.baseurl }}/public/images/kuma/2017-11-quick-links.png)

Stephanie also updated the visual hierarchy of article headings. This is most
noticeable on <code>&lt;h3&gt;</code> elements, which are now indented with
black space.

![New &lt;h3&gt; style](
 {{ site.baseurl }}/public/images/kuma/2017-11-h3.png
 "&lt;h3&gt; elements are inverse with some leading black space.")

<a name="aws-nov-2017">Improved MDN in AWS and Kubernetes
---
We continued to have performance and uptime issues in AWS in November. We're
prioritizing fixing these issues, and we're delaying some 2017 plans, such as
improving KumaScript translations and upgrading Django, to next year.

We lost GZip compression in the move to AWS.
[Ryan Johnson](https://github.com/escattone) added it back in
[PR 4522](https://github.com/mozilla/kuma/pull/4522). This reduced the
average page download time by 71% (0.57s to 0.16s), and contributed to a
6% decrease in page load time (4.2 to 4.0s).

![Page Download drop due to GZip](
 {{ site.baseurl }}/public/images/kuma/2017-11-gzip.png
 "71% drop from 0.57s to 0.16s due to GZip")

Heavy load due to scraping caused 6 downtimes totaling 35 minutes.
We worked to improve the performance of unpopular pages that get high traffic
from scrapers, such as document list views
([PR 4463](https://github.com/mozilla/kuma/pull/4463) from
[John Whitlock](https://github.com/jwhitlock)) and the revisions dashboard
([PR 4520](https://github.com/mozilla/kuma/pull/4520) from
[Josh Mize](https://github.com/jgmize)). This made the system more resilient.

Kubernetes was contributing to the downtimes, by restarting web servers when
they started to undergo heavy load and were slow to respond.  We've adjusted
our "readiness" and "liveness" probes so that Kubernetes will be more patient
and more gentle
([Infra PR 665](https://github.com/mozmeao/infra/pull/665) from
[Ryan Johnson](https://github.com/escattone)).

These changes have made MDN more resilient and reliable, but more work will be
needed in December.

[Stephanie Hobson](https://github.com/stephaniehobson) fixed the development
favicon appearing in production
([PR 4530](https://github.com/mozilla/kuma/pull/4530)), as well as an issue
with lazy-loading web fonts
([PR 4533](https://github.com/mozilla/kuma/pull/4533)).

[Ryan Johnson](https://github.com/escattone) continues work on our deployment
process. Pushing certain branches will cause Jenkins to take specific
deployment steps. Pushing ``master`` will run tests and publish a Docker image.
Pushing ``stage-push`` will deploy that image to
[stage.mdn.moz.works](https://stage.mdn.moz.works/).  Pushing
``stage-integration-tests`` will run browser and HTTP tests against that
deployment. We'll make these steps more reliable, add production variants, and
then link them together into automated deployment pipelines.

<a name="tweaks-nov-2017">Shipped Tweaks and Fixes
---
There were 260 PRs merged in November:

- [89 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)
- [76 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)
- [38 mdn/kumascript PRs](https://github.com/mdn/kumascript/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)
- [32 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)
- [16 mozmeao/infra PRs](https://github.com/mozmeao/infra/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)
- [9 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&q=is:pr+is:closed+merged:"2017-11-01..2017-11-30"&utf8=✓)

Many of these were from external contributors, including several first-time
contributions. Here are some of the highlights:

- Update `chrome_url_overrides` for Opera
  ([BCD PR 559](https://github.com/mdn/browser-compat-data/pull/559)),
  from first-time contributor
  [Zbyněk Eiselt](https://github.com/eiselzby).
- Mark `add` and `set` methods of `Set`, `Map` and `WeakMap` objects as
  partially implemented on IE 11
  ([BCD PR 586](https://github.com/mdn/browser-compat-data/pull/586)),
  from first-time contributor
  [Ivan Buryak](https://github.com/11bit).
- Add link to Edge bug report for `<a>`
  ([BCD PR 592](https://github.com/mdn/browser-compat-data/pull/592)),
  from first-time contributor
  [Michael Hogg](https://github.com/michaelhogg).
- Update status for CSS Scroll Snapping properties
  ([BCD PR 609](https://github.com/mdn/browser-compat-data/pull/609)),
  from first-time contributor
  [Masataka Yakura](https://github.com/myakura).
- Update IANA timezone name support in Chrome/Opera
  ([BCD PR 611](https://github.com/mdn/browser-compat-data/pull/611)),
  from first-time contributor
  [jungshik](https://github.com/jungshik).
- Update browser identifier declaration instructions
  ([BCD PR 625](https://github.com/mdn/browser-compat-data/pull/625)),
  Fix schema documentation for `flag`
  ([BCD PR 627](https://github.com/mdn/browser-compat-data/pull/627)), and
  Add example for Status information
  ([BCD PR 628](https://github.com/mdn/browser-compat-data/pull/628)),
  from first-time contributor
  [Ra'Shaun Stovall](https://github.com/snuggs).
- Update support data for `parseInt` treatment of leading zeros
  ([BCD PR 633](https://github.com/mdn/browser-compat-data/pull/633)),
  from first-time contributor
  [Claude Pache](https://github.com/claudepache).
- Update ``textarea`` ``@autocomplete`` compat data
  ([BCD PR 637](https://github.com/mdn/browser-compat-data/pull/637) and
  [PR 673](https://github.com/mdn/browser-compat-data/pull/673)),
  from first-time contributor
  [Matt N.](https://github.com/mnoorenberghe)
- Add ``sampleRate`` option to ``new AudioContext()``
  ([BCD PR 651](https://github.com/mdn/browser-compat-data/pull/651)),
  from first-time contributor
  [Jedipedia](https://github.com/Jedipedia).
- Add support for ``page_action`` for FF for Android
  ([BCD PR 667](https://github.com/mdn/browser-compat-data/pull/667)),
  from first-time contributor
  [Elad](https://github.com/katzelad).
- Safari has implemented ``upgrade-insecure-requests``
  ([BCD PR 670](https://github.com/mdn/browser-compat-data/pull/670)),
  from first-time contributor
  [Justyn Temme](https://github.com/justyntemme).
- `TypedArray.toString`
  ([BCD PR 677](https://github.com/mdn/browser-compat-data/pull/677)),
  from first-time contributor
  [Lambdac0re](https://github.com/Lambdac0re).
- Update support for `content-security-policy`
  ([BCD PR 683](https://github.com/mdn/browser-compat-data/pull/683)),
  from first-time contributor
  [Jakob Jarosch](https://github.com/foxylion).
- Add note about `Origin` header when using `POST` requests in Edge
  ([BCD PR 684](https://github.com/mdn/browser-compat-data/pull/684)),
  from first-time contributor
  [Viktor](https://github.com/Yaffle).
- Add the ability for users to hide GitHub link from their public profile
  ([bug 1360294](https://bugzilla.mozilla.org/show_bug.cgi?id=1360294),
   [Kuma PR 4346](https://github.com/mozilla/kuma/pull/4346)),
  from
  [Maton Anthony](https://github.com/MatonAnthony).
- Add details about the changes in the `.env`
  ([Kuma PR 4494](https://github.com/mozilla/kuma/pull/4494)),
  from first-time contributor
  [Pavan Gudiwada](https://github.com/pavangudiwada).
- Docker setup guidance
  ([Kuma PR 4501](https://github.com/mozilla/kuma/pull/4501)),
  from first-time contributor
  [Pavan Gudiwada](https://github.com/pavangudiwada).
- Enable Telugu (te) as candidate locale
  ([bug 984149](https://bugzilla.mozilla.org/show_bug.cgi?id=984149),
  [Kuma PR 4547](https://github.com/mozilla/kuma/pull/4547)),
  from
  [John Whitlock](https://github.com/jwhitlock).
- Add `curl` as an alternative to `wget`
  ([bug 1387505](https://bugzilla.mozilla.org/show_bug.cgi?id=1387505),
  [Kuma PR 4570](https://github.com/mozilla/kuma/pull/4570)),
  from first-time contributor
  [Deep Bhattacharyya](https://github.com/coderick14).
- Add Mozilla Foundation End-of-Year callout
  ([bug 1420535](https://bugzilla.mozilla.org/show_bug.cgi?id=1420535),
   [Kuma PR 4572](https://github.com/mozilla/kuma/pull/4572)),
  from
  [Stephanie Hobson](https://github.com/stephaniehobson).
- Add support for Bulgarian.
  ([KumaScript PR 374](https://github.com/mdn/kumascript/pull/374)),
  from first-time contributor
  [Красимир Беров](https://github.com/kberov).
- Mark Background Tasks as Proposed Recommendation
  ([KumaScript PR 390](https://github.com/mdn/kumascript/pull/390)),
  from first-time contributor
  [Masataka Yakura](https://github.com/myakura).
- Close `<li>` tag properly
  ([KumaScript PR 398](https://github.com/mdn/kumascript/pull/398)),
  from first-time contributor
  [antonio-piha](https://github.com/antonio-piha).
- Add French for event properties
  ([KumaScript PR 408](https://github.com/mdn/kumascript/pull/408)),
  from first-time contributor
  [Matilin Torre](https://github.com/Watilin).
- Add Dutch translation
  ([KumaScript PR 412](https://github.com/mdn/kumascript/pull/412)),
  from first-time contributor
  [evelijn](https://github.com/evelijn).
- Fix a mistake in ``array-reduce`` comment
  ([Interactive Examples PR 358](https://github.com/mdn/interactive-examples/pull/358)),
  from first-time contributor
  [Gal Pasternak](https://github.com/galman33).
- Fix AudioContext &amp; OfflineAudioContext inheritance
  ([Data PR 152](https://github.com/mdn/data/pull/152)),
  from first-time contributor
  [Jedipedia](https://github.com/Jedipedia).

<a name="next-nov-2017">Planned for December
===
Mozilla gathers for the
[All-Hands event in Austin, TX](https://wiki.mozilla.org/All_Hands/Austin) in
December, which gives us a chance to get together, celebrate the year's
accomplishments, and plan for 2018. Mozilla offices will shut down for the
last full week of December. This doesn't leave a lot of time for coding.

We'll continue working on the projects we worked on in November. We'll convert
more Browser Compatibility data. We'll tweak the AWS infrastructure.  We'll
eliminate and convert more waffle flags. We'll watch the interactive examples
and improved compatibility tables, and ship them when ready.

We'll also take a step back, and ask if we're spending time and attention on
the most important things. We'll think about our processes, and how they could
better support our priorities.

But mostly, we'll try not to mess things up, so that we can enjoy the holidays
with friends and family, and come back refreshed for 2018.
