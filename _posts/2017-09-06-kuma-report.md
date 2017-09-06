---
layout: post
title: Kuma Report, August 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in August in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- Launched beta of interactive examples
- Continued work on the AWS migration
- Prepared for KumaScript translations
- Refined the Browser Compat Data schema
- Shipped tweaks and fixes

Here's the plan for September:
- Establish maintenance mode in AWS

<!--more-->

Done in August
===

Launched beta of interactive examples
---
On August 29, we launched the interactive examples. We're starting with showing
them to 50% of anonymous users, to measure the difference in site speed.
You can also visit the new pages directly. See the
[interactive editors in beta](https://discourse.mozilla.org/t/interactive-editors-in-beta/18548)
post on Discourse for more details. We're collecting feedback with a short
survey. See the "take our survey" link below the new interactive example.

We've already gotten several rounds of feedback, by showing early iterations
to Mozilla staff and to the [Brigade](https://wearebrigade.com/),
who helped with the MDN redesign. Schalk, Stephanie, Kadir, and Will Bamberg
added user interviews to our process. They recruited web developers to try out the
new feature, watched how they used it, and adjusted the design based on the
feedback.

One of the challenging issues was avoiding a scrollbar, when the ``<iframe>``
for the interactive example was smaller than the content. The scrollbar
broke the layout, and made interaction clumsy.  We tried several rounds of
manual iframe sizing before implementing dynamic sizing using
[postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
to send the desired size from the client ``<iframe>`` to the MDN page.
([PR 4361](https://github.com/mozilla/kuma/pull/4361)).

Another change from user testing is that we began with deployment to S3 behind
a CDN, rather than waiting until after beta testing. Thanks to
[Dave Parfitt](https://github.com/metadave) for quickly implementing this
([PR 149](https://github.com/mdn/interactive-examples/pull/149)).

It will take a while to complete the beta testing and launch these six pages
to all users. Until then, we still have the
[live samples](https://developer.mozilla.org/en-US/docs/MDN/Contribute/Structures/Live_samples).
[Stephanie Hobson](https://github.com/stephaniehobson) recently improved these
by opening them in a new tab, rather than replacing the MDN reference page.
([PR 4391](https://github.com/mozilla/kuma/pull/4391)).

Continued work on the AWS migration
---
We're continuing the work to rehost MDN in AWS, using
[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes). We track the AWS
migration work in
[a GitHub project](https://github.com/mozmeao/infra/projects/4), and we're
getting close to production data tests.

In our current datacenter, we use Apache to serve the website
(using [mod_wsgi](https://en.wikipedia.org/wiki/Mod_wsgi)). We're not using
Apache in AWS, and in August we updated Kuma to take on more of Apache's
duties, such as serving files from MDN's distant past
([PR 4365](https://github.com/mozilla/kuma/pull/4365) from
[Ryan Johnson](https://github.com/escattone))
and handling old redirects
([PR 4231](https://github.com/mozilla/kuma/pull/4231) from
[Dave Parfitt](https://github.com/metadave)).

We are currently using MySQL with a
[custom collation `utf8_distinct_ci`](https://mariadb.com/resources/blog/adding-case-insensitive-distinct-unicode-collation).
The collation determines how text is sorted, and if two strings are considered
to be equal.  MySQL includes several collations, but they
didn't allow the behavior we wanted for tags. We wanted to allow both
"Reference" and the French "Référence", but not allow the lower-case variants
"reference" and "référence". The custom collation allowed us to do this
while still using our tagging library
[django-taggit](https://github.com/alex/django-taggit). However, we can't
use a custom collation in AWS's RDS database service. The compromise was to
programmatically rename tags (they are now "Reference" and "Référence (2)"),
and switch to the standard ``utf8_general_ci`` collation, which still prevents
the lowercase variants
([PR 4376](https://github.com/mozilla/kuma/pull/4376) by
[John Whitlock](https://github.com/jwhitlock)). After the AWS migration, we
will revisit tags, and see how to best support the desired features.

Prepared for KumaScript translations
---
There was some preparatory work toward translating KumaScript strings in
[Pontoon](https://pontoon.mozilla.org/projects/mdn/), but nothing shipped yet.
The locale files have been moved from the Kuma repository to a new repository,
[mozilla-l10n/mdn-l10n](https://github.com/mozilla-l10n/mdn-l10n/). The Docker
image for KumaScript now includes the locale files.  Finally, KumaScript now
lives at
[mdn/kumascript](https://github.com/mdn/kumascript), in the
[mdn Github organization](https://github.com/mdn/).

There are
[additional tasks planned](https://bugzilla.mozilla.org/show_bug.cgi?id=1340342#c4),
to use 3rd-party libraries to load translation files, apply translations, and to
extract localizable strings. However, AWS will be the priority for the rest of
September, so we are not planning on taking the next steps until October.

Refined the Browser Compat Data schema
---
[Florian Scholz](https://github.com/Elchi3) and
[wbamberg](https://github.com/wbamberg) have finished a long project to update
the Browser Compatibility Data schema. This included a script to migrate
the data ([BCD PR 304](https://github.com/mdn/browser-compat-data/pull/304)),
and a unified `{{'{{'}}compat}}` macro suitable for compatibility tables
across the site
([KumaScript PR 272](https://github.com/mdn/kumascript/pull/272)).
The new schema is used in release 0.0.4 of
[mdn-browser-compat-data](https://www.npmjs.com/package/mdn-browser-compat-data).

The goal is to convert all the compatibility data on MDN to the BCD format. Florian
is on track to convert the JavaScript data in September.
[Jean-Yves Perrier](https://github.com/teoli2003) has made good progress on
migrating HTML compatibility data with 7 merged PRs, starting with
[PR 279](https://github.com/mdn/browser-compat-data/pull/279).

Shipped Tweaks and Fixes
---
There were many PRs merged in August:

- [59 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)
- [52 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)
- [30 mdn/kumascript PRs](https://github.com/mozilla/kumascript/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)
- [27 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)
- [6 mdn/doc-linter-webextension PRs](https://github.com/mdn/doc-linter-webextension/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)

<!---
- [0 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-08-01..2017-09-01%22&utf8=✓)
-->

Many of these were from external contributors, including several first-time contributions. Here are some of the highlights:

- [Kuma PR 4337](https://github.com/mozilla/kuma/pull/4337):
  Add the wordcount to the article editor, from
  [Eric Shepherd](https://github.com/a2sheppy).
- [Kuma PR 4345](https://github.com/mozilla/kuma/pull/4345):
  Use 302 not 301 for locale based redirects, from
  [Safwan Rahman](https://github.com/safwanrahman).
- [Kuma PR 4364](https://github.com/mozilla/kuma/pull/4364):
  Change default page title to "MDN Web Docs", first contribution from
  [Dylan Pyle](https://github.com/dylanpyle).
- [Kuma PR 4374](https://github.com/mozilla/kuma/pull/4374):
  Get development environment working on SELinux, from
  [SphinxKnight](https://github.com/SphinxKnight).
- [Kuma PR 4375](https://github.com/mozilla/kuma/pull/4375):
  Show "hidden" content in the English panel when translating, from
  [SphinxKnight](https://github.com/SphinxKnight).
- [Kuma PR 4387](https://github.com/mozilla/kuma/pull/4387):
  Redirect some legacy locales like `en` and `cn` to their new locations,
  fixing 4-year-old
  [bug 962148](https://bugzilla.mozilla.org/show_bug.cgi?id=962148), from
  [Safwan Rahman](https://github.com/safwanrahman).
- [Interactive Examples PR 237](https://github.com/mdn/interactive-examples/pull/237):
  Add dataview examples for ArrayBuffer from
  [Mark Boas](https://github.com/maboa).
- [KumaScript PR 265](https://github.com/mdn/kumascript/pull/265):
  LearnSidebar German Translation, first contribution from
  [Shi](https://github.com/shidigital).
- [KumaScript PR 281](https://github.com/mdn/kumascript/pull/281):
  Background tasks is a candidate recommendation, first contribution from
  [Christophe Coevoet](https://github.com/stof).
- [KumaScript PR 289](https://github.com/mdn/kumascript/pull/289):
  add 'shape' and 'basic-shape' data output cases, first contribution from
  [mfluehr](https://github.com/mfluehr).
- [Browser Compat Data PR 288](https://github.com/mdn/browser-compat-data/pull/288):
  Updated background-clip:text compatibility on Edge, first contribution from
  [Gary Lee](https://github.com/lvnam96).
- [Browser Compat Data PR 301](https://github.com/mdn/browser-compat-data/pull/301):
  MS Edge supports options and locales in Date.prototype.toLocaleDateString,
  first contribution from
  [Yordan Darakchiev](https://github.com/iordan93).
- [Browser Compat Data PR 321](https://github.com/mdn/browser-compat-data/pull/321):
  Add Edge support for `extension.getViews()`, first contribution from
  [Thierry Régagnon](https://github.com/tregagnon).
- [Browser Compat Data PR 335](https://github.com/mdn/browser-compat-data/pull/335):
  Add information about is_default in Firefox 57, first contribution from
  [Michael Kaply](https://github.com/mkaply).
- [Browser Compat Data PR 341](https://github.com/mdn/browser-compat-data/pull/341):
  Add border-width CSS property compat data, one of two first contributions from
  [Daniel D. Beck](https://github.com/ddbeck).
- [Doc Linter Webextension PR 52](https://github.com/mdn/doc-linter-webextension/pull/52):
  Release 1.0.1, from
  [Maton Anthony](https://github.com/MatonAnthony).


Planned for September
===
Work will continue to migrate to Browser Compat Data, and to fix issues with the
redesign and the new interactive examples.

Establish Maintenance Mode in AWS
---
In September, we plan to prepare a maintenance mode deployment in AWS, and send
it some production traffic.  This will allow us to model the resources needed
when the production environment is hosted in AWS. It will also keep MDN data
available while the production database is transferred, when we finalize the
transition.
