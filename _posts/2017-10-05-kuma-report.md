---
layout: post
title: Kuma Report, September 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in September in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- Ran Maintenance Mode Tests in AWS
- Updated Article Styling
- Continued Conversion to Browser Compat Data
- Shipped Tweaks and Fixes

Here's the plan for October:
- Move MDN to AWS
- Improve Performance of the Interactive Editor

<!--more-->

Done in September
===

Ran Maintenance Mode Tests in AWS
---
Back in March 2017, we added Maintenance Mode to Kuma, which allows the site
content to be available when we can't write to the database. This mode got
its first workout this month, as we put MDN into Maintenance Mode in SCL3,
and then sent an increasing percentage of public traffic to an MDN
deployment in AWS.

We ran 3 tests in September. In the first, we just tried Maintenance Mode with
production traffic in SCL3. In [the second
test](https://github.com/mozmeao/infra/issues/516) we sent 5% of traffic to
AWS, and in [the third test](https://github.com/mozmeao/infra/issues/518) we
ramped it up to 15%, then 50%, and finally 100%. The most recent test,
on October 3, included New Relic monitoring, which gave us useful data
and pretty charts.

Web Transactions Time shows how the average request is
handled by the different services.  For the SCL3 side, you can see a steady
improvement in transaction time from 125 to 75 ms, as more traffic is handled
by AWS.

![SCL3 transaction time]({{ site.baseurl }}/public/images/kuma/2017-09-scl3-transaction-time.png "SCL3 transaction time")

On the AWS side, the response time grows from 40 to 90 ms, as the DNS
configuration sends 100% of traffic to the new cluster.

![AWS transaction time]({{ site.baseurl }}/public/images/kuma/2017-09-aws-transaction-time.png "AWS transaction time")

The Web Transaction Percentiles chart shows useful statistics beyond the
average.  For example, 99% of users see at least 375 ms response time, and the
median is at 50 ms.

![SCL3 transaction percent]({{ site.baseurl }}/public/images/kuma/2017-09-scl3-transaction-percent.png "SCL3 transaction percent")

On the AWS side, 99% of users see at least 350 ms response time (slightly better), and the
median is at 100 ms (slightly worse).

![AWS transaction percent]({{ site.baseurl }}/public/images/kuma/2017-09-aws-transaction-percent.png "AWS transaction percent")

Finally, Throughput measures the requests handled per minute. SCL3
continued handling over 500 requests per minute during the test. This may be
due to clients using old DNS records, or because KumaScript continues making
requests to render out-of-date pages.

![SCL3 throughput]({{ site.baseurl }}/public/images/kuma/2017-09-scl3-throughput.png "SCL3 throughput")

AWS ramped up to over 2000 requests per minute during the test, easily handing
the load of a US afternoon.

![AWS throughput]({{ site.baseurl }}/public/images/kuma/2017-09-aws-throughput.png "AWS throughput")

We consider this a successful test. Our AWS environment can easily handle
regular, read-only MDN traffic, with capacity to spare. We don't expect
MDN users to notice much of a difference when we make the change.

Updated Article Styling
---
We're working on the next phase of redesigning MDN. We're looking at ways to
present MDN articles, to make them easier to read, to scan quickly, and to
emphasize the most useful information. We're testing some ideas with users, and
some of the adjustments showed up on the site this month.

For example, MDN documents a lot of code in prose, such as HTML element and
attribute names. In [PR 4400](https://github.com/mozilla/kuma/pull/4400),
[Stephanie Hobson](https://github.com/stephaniehobson) added a highlight
background to make these stand out.

Before PR 4400, a fixed-width font was used to display literals:

![Before 4400 no highlight]({{ site.baseurl }}/public/images/kuma/2017-09-before-4400.png "Before 4400")

After PR 4000, the literals stand out with a light grey background:

![After 4400 highlight]({{ site.baseurl }}/public/images/kuma/2017-09-after-4400.png "After 4400")

There's a lot that goes into making text on the web readable (see
[Stephanie's slides](https://www.slideshare.net/stephaniehobson/writing-for-every-reader)
from her talk at [#a11yTOConf](http://conf.a11yto.com) for some suggestions).
One of the things we can do with the default style is to try to make lines
about 50-75 characters wide. On the other hand, code examples don't wrap well,
and we want to make them stand out. We're experimenting with style changes
for line length with beta testers, using some of the ideas from
[blog.mozilla.org](https://blog.mozilla.org). For example,
[PR 4402](https://github.com/mozilla/kuma/pull/4402) expands the sample output,
making the examples stand out from the rest of the page.

Before PR 4402, the examples shared the text's narrow width:

![Before 4402 narrow]({{ site.baseurl }}/public/images/kuma/2017-09-before-4402.png "Before 4402")

After PR 4402, the example is as wide as the code samples, and the buttons restyled:

![After 4402 narrow]({{ site.baseurl }}/public/images/kuma/2017-09-after-4402.png "After 4402")

We'll test more adjustments with beta testers and in individual user tests.
Some of these we'll ship immediately, and others will inform the article
redesign.

Continued Conversion to Browser Compat Data
---
The Browser Compat Data (BCD) project now includes all the HTML and JavaScript
compatibility data from MDN. 1,500 MDN pages now generate their compatibility
tables from this data. Only 4,500 more to go!

The BCD project was the most active MDN project in September.  There were 159
commits over 90 pull requests. These PRs came from from 18 different
contributors, bringing the total to 50 contributors. There's over 58,000
additional lines in the project.  13 of these PRs are from [Daniel D.
Beck](https://github.com/ddbeck), who is joining the MDN team as a contractor.

This progress was made possible by
[Florian Scholz](https://github.com/Elchi3),
[Jean-Yves Perrier](https://github.com/teoli2003), and
[wbamberg](https://github.com/wbamberg), who quickly and accurately reviewed
the PRs, working out issues and getting them merged. Florian has also started
a weekly release of the npm package, and we're up to
[mdn-browser-compat-data 0.0.8](https://www.npmjs.com/package/mdn-browser-compat-data).

Shipped Tweaks and Fixes
---
There were many PRs merged in September:

- [90 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)
- [36 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)
- [24 mdn/kumascript PRs](https://github.com/mozilla/kumascript/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)
- [17 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)
- [2 mdn/doc-linter-webextension PRs](https://github.com/mdn/doc-linter-webextension/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)
- [1 mdn/data PR](https://github.com/mdn/data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-09-01..2017-10-01%22&utf8=✓)

Here are some of the highlights:

- [BCD PR 300](https://github.com/mdn/browser-compat-data/pull/300):
  Add notes for JavaScript API ``runtime.OnInstalledReason``, from first-time contributor
  [Kestrel](https://github.com/nkestrel).
- [BCD PR 332](https://github.com/mdn/browser-compat-data/pull/332):
  Add note about Firefox support for Origin header, from first-time contributor
  [Linus Lewandowski](https://github.com/LEW21).
- [BCD PR 356](https://github.com/mdn/browser-compat-data/pull/356):
  Update JavaScript API ``browsingData`` support, from first-time contributor
  [Tushar Saini](https://github.com/shatur).
- [BCD PR 366](https://github.com/mdn/browser-compat-data/pull/366):
  Update Referrer-Policy same-origin / strict-origin support, from
  first-time contributor
  [Tim Düsterhus](https://github.com/TimWolla).
- [BCD PR 370](https://github.com/mdn/browser-compat-data/pull/370):
  Add support info for ``windowID``, from first-time contributor
  [Baptiste Thémin](https://github.com/Baptistou).
- [BCD PR 416](https://github.com/mdn/browser-compat-data/pull/416):
  Add Safari 11's added support for the ``Intl`` JavaScript API, from
  first-time contributor
  [Andy VanWagoner](https://github.com/thetalecrafter).
- [BCD PR 377](https://github.com/mdn/browser-compat-data/pull/377)
  Firefox 57 will support ``Tab.discarded`` state, from first-time contributor
  [Joachim](https://github.com/jmozmoz).
- [BCD PR 420](https://github.com/mdn/browser-compat-data/pull/420):
  Add 'font-weight' CSS properties, the first of 5 PRs from
  first-time BCD contributor [mfluehr](https://github.com/mfluehr).
  mfluehr also contributed 4 PRs to KumaScript, and kept the mdn/data project
  active with [PR 107](https://github.com/mdn/data/pull/107), documenting the
  ``::placeholder`` pseudo-element.
- [KumaScript PR 327](https://github.com/mozilla/kumascript/pull/327) and
  [KumaScriptPR 328](https://github.com/mozilla/kumascript/pull/328):
  Add Web Share API, from first-time contributor
  [Jeffrey Yasskin](https://github.com/jyasskin).
- [Kuma PR 4428](https://github.com/mozilla/kuma/pull/4428):
  Rename WebExtensions to Browser Extensions in the main navgation, following
  the new [naming standard](https://browserext.github.io/browserext/), from
  [wbamberg](https://github.com/wbamberg).
- [Kuma PR 4434](https://github.com/mozilla/kuma/pull/4343):
  Wrap task completion call-to-action in ``gettext``, so that we can start
  getting better feedback from MDN users who see non-English pages, from
  [Stephanie Hobson](https://github.com/stephaniehobson).

Planned for October
===
Work will continue to migrate to Browser Compat Data, and to fix issues with the
redesign and the new interactive examples.

Move MDN to AWS
---
In October, we'll complete our functional testing of MDN, making sure that
page editing and other read/write tests are working, and that the rarely used
features continue to work. We'll then put SCL3 in Maintenance Mode again,
move the database, and come back with MDN in AWS.

We've done a lot of preparation, but we expect *something* to break, so we're
planning on fixing AWS-related bugs in October. The AWS move will also allow
us to improve our deployment processes, helping us ship features faster.
If things go smoothly, we have plenty of other work lined up, such as style
improvements, SEO-related tweaks, updating to Django 1.11, and getting
KumaScript UI strings into Pontoon.

Improve Performance of the Interactive Editor
---
We're continuing the
[beta test for the interactive editor](https://discourse.mozilla.org/t/interactive-editors-in-beta/18548).
The feedback has been overwhelming positive, but we're not happy with the page
speed impact. We'll continue work in October to improve performance.
In the meantime, contractor [Mark Boas](https://github.com/maboa) is preparing
examples for the launch, such as 26 examples for JavaScript expressions and
operators ([PR 286](https://github.com/mdn/interactive-examples/pull/286)).
