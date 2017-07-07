---
layout: post
title: Kuma Report, June 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in June in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN Web Docs](https://developer.mozilla.org):

- Shipped the New Design to Beta Testers
- Added KumaScript macro tests
- Continued MDN data projects
- Shipped tweaks and fixes

Here's the plan for July:
- Continue the redesign
- Experiment with on-site interactive examples
- Update localization of macros
- Ship the sample database

<!--more-->

Done in June
===

Shipped the new design to beta testers
---
This month, we revealed some long-planned changes.  First, MDN is
[focusing on web docs](https://blog.mozilla.org/opendesign/future-mdn-focus-web-docs/),
which includes changing our identity from "Mozilla Developer Network" to
"MDN Web Docs".  Second, we're shipping a
[new design to beta users](https://blog.mozilla.org/opendesign/mdns-new-design-beta/),
to reflect
[Mozilla's new brand identity](https://mozilla.ninja/)
as well as the MDN Web Docs brand.

[Stephanie Hobson](https://github.com/stephaniehobson) did a tremendous amount
of work over
[26 Kuma PRs](https://github.com/mozilla/kuma/pulls?utf8=%E2%9C%93&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-06-01..2017-07-01%22%20author%3Astephaniehobson%20)
and
[2 KumaScript PRs](https://github.com/mozilla/kumascript/pulls?utf8=%E2%9C%93&q=is%3Apr%20is%3Aclosed%20merged%3A%222017-06-01..2017-07-01%22%20author%3Astephaniehobson%20)
to launch a beta of the updated design on wiki pages. A lot of dead code has
been removed, and non-beta users continue to get the current design.
[Schalk Neethling](https://github.com/schalkneethling) reviewed the PRs as
fast as they were created, including checking the rendering in supported
browsers.  Our beta users have provided a lot of feedback and found some bugs,
which Stephanie has been triaging,
[tracking](https://bugzilla.mozilla.org/show_bug.cgi?id=1375892),
and fixing.

This work continues in July, with an update to the homepage and other pages.
When we've completed the redesign, we'll ship the update to all users. If you
want to see it early,
[opt-in as a beta tester](https://developer.mozilla.org/en-US/docs/MDN/Contribute/Howto/Be_a_beta_tester).

Added KumaScript Macro Tests
---
Macros used to be tested manually, in production. After moving the
macros to GitHub, they were still tested manually, but in the development
environment.  In June, [Ryan Johnson](https://github.com/escattone) added an
automated testing framework, and tests for five macros, in
[PR 204](https://github.com/mozilla/kumascript/pull/204). This allows us to
mock the Kuma APIs needed for rendering, and to test macros in
different locales and situations. This will help us refine and refactor
macros in the future.

Continued MDN Data Projects
---
The MDN data projects were very busy in June, with
[48 browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-06-01..2017-07-01%22&utf8=✓)
and
[10 data PRs](https://github.com/mdn/data/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-06-01..2017-07-01%22&utf8=✓)
merged.
MDN "writers"
[Florian Scholz](https://github.com/Elchi3),
[wbamberg](https://github.com/wbamberg), and
[Eric Shepherd](https://github.com/a2sheppy)
have been converting MDN browser compatibility tables to JSON data, refining
the schema and writing documentation. This is already becoming a community
project, with almost half of the PRs coming from contributors such as
[Andy McKay](https://github.com/andymckay) (1 PR).
[Dominik Moritz](https://github.com/domoritz) (2 PRs),
[Roman Dvornov](https://github.com/lahmatiy) (6 PRs),
[Ng Yik Phang](https://github.com/ngyikp) (2 PRs), and
[Sebastian Noack](https://github.com/snoack) (**16 PRs**!).

The tools and processes are updating as well, to keep up with the activity.
browser-compat-data gained a linter in
[PR 240](https://github.com/mdn/browser-compat-data/pull/240).
[mdn-browser-compat-data's npm package](https://www.npmjs.com/package/mdn-browser-compat-data)
was bumped to version 0.0.2, and then 0.0.3.
[mdn-data](https://www.npmjs.com/package/mdn-data) was released as 1.0.0.
We're loading the browser-compat-data from the NPM package in production,
and hope to start loading the data NPM package soon.

We're happy with the progress on the data projects. There's a lot of work
remaining to convert the data on MDN, and also a lot of work to automate the
process so that changes are reflected in production as quickly as possible.

Shipped Tweaks and Fixes
---
Here's some other highlights from the
[44 merged Kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-06-01..2017-07-01%22&utf8=✓)
in June:

- [PR 4262](https://github.com/mozilla/kuma/pull/4262):
  Fixed [bug 1370965](https://bugzilla.mozilla.org/show_bug.cgi?id=1370965).
  You can right-click to start editing again.
  ([a2sheppy](https://github.com/a2sheppy))
- [PR 4280](https://github.com/mozilla/kuma/pull/4280):
  KumaScript errors now link to the
  [GitHub repository](https://github.com/mozilla/kumascript/tree/master/macros)
  ([escattone](https://github.com/escattone)).
- [PR 4286](https://github.com/mozilla/kuma/pull/4286):
  Fixed [bug 1370514](https://bugzilla.mozilla.org/show_bug.cgi?id=1370514),
  updating links in editing mode
  ([karabellyj](https://github.com/karabellyj)'s first PR).
- [PR 4290](https://github.com/mozilla/kuma/pull/4290):
  Updated Github to GitHub
  (welcome back to Kuma [SphinxKnight](https://github.com/SphinxKnight)).


Here's some other highlights from the
[31 merged KumaScript PRs](https://github.com/mozilla/kumascript/pulls?page=1&q=is%3Apr+is%3Aclosed+merged%3A%222017-06-01..2017-07-01%22&utf8=✓)
in June:

- [PR 228](https://github.com/mozilla/kumascript/pull/228):
  Added Dutch translation
  ([stevenwdv](https://github.com/stevenwdv)'s first contribution).
- [PR 206](https://github.com/mozilla/kumascript/pull/206):
  Fix master Jenkins pipeline, publish Docker images again
  ([escattone](https://github.com/escattone)).
- [PR 214](https://github.com/mozilla/kumascript/pull/214):
  Add liveness/readiness endpoints
  ([escattone](https://github.com/escattone)).

Planned for July
===

Continue the Redesign
---
Some of the styling for the article pages is shared across other pages, but
there is more work to do to complete the redesign. Up next is the homepage,
which will change to reflect our new focus on documenting the open web.  Other
pages will need further work to make the site consistent. When we and the beta
testers are mostly happy, we'll ship the design to all MDN visitors, and then
remove the old design code.

Experiment with On-site Interactive Examples
---
We're preparing some interactive examples, so that MDN readers can learn by
adjusting the code without leaving the site. We're still working out the details
of serving these examples at production scale, so we're limiting the July
release to beta users. You can follow the work at
[mdn/interactive-examples](https://github.com/mdn/interactive-examples).

Update Localization of Macros
---
Currently, KumaScript macros use in-macro localization strings and
utility functions like
[getLocalString](https://github.com/mozilla/kumascript/blob/master/macros/MDN-Common.ejs#L52)
to localize output for three to five languages.  Meanwhile, user interface strings in
Kuma are translated in
[Pontoon](https://pontoon.mozilla.org/projects/mdn/) into 57 languages. We'd
like to use a similar workflow for strings in macros, and will get started on
this process in July.

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We almost had to break the tradition, but we can
say again it will ship next month.
[PR 4248](https://github.com/mozilla/kuma/pull/4248), adding the
``scrape_document`` command, shipped in June.  The final code,
[PR 4076](https://github.com/mozilla/kuma/pull/4076), is in review, and should
be merged in July.
