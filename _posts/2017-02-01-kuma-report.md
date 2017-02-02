---
layout: post
title: Kuma Report, January 2017
author: jwhitlock
excerpt_separator: <!--more-->
---

Here's what happened in January in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- Upgraded to node.js v6
- Reached next milestone on functional tests
- Switched from Stylus to Sass for CSS
- Published AWS Migration Plan
- Shipped Tweaks and Fixes

Here's the plan for February:

- Ship the Sample Database
- Demo deployments in AWS
- Read-Only Maintenance Mode

<!--more-->

Done in January
===

Upgraded to node.js v6
---
[KumaScript](https://github.com/mozilla/kumascript), MDN's rendering engine,
runs on node.js, and we also use node.js-based tools in our static asset
pipeline.  We upgraded from v0.10 to v6, which will be supported under the
[Long-term Support policy](https://github.com/nodejs/LTS)
until April 2019.

Ryan Johnson (rjohnson)
[updated the Kumascript engine](https://github.com/mozilla/kumascript/pull/69),
including switching from checked-in modules to package.json.
I updated the [Kuma side](https://github.com/mozilla/kuma/pull/4094).
We worked with Ryan Watson (rw0ts0n), and Eric Ziegenhorn (ericz) to update the
13 production servers, and to update the deployment process. It was a
time-consuming update, but went smoothly for users, with a handful of rendering
issues discovered after deployment.

We're excited about Docker-based deployment, which will make similar updates
easier in the future, and a KumaScript macros test suite, to detect rendering
issues before they get to production.

Reached next milestone on functional tests
---
Stephanie Hobson (shobson) completed the conversion of the functional tests
from Intern to py.test with the
[translation tests](https://github.com/mozilla/kuma/pull/4102), and has
submitted the pull request to remove the
[Intern tests](https://github.com/mozilla/kuma/pull/4099). We now have
a library of browser-based functional tests to verify that an integrated
environment is serving MDN correctly. Giorgos Logiotatidis (giorgos) has
[re-written the Jenkins integration pipeline](https://github.com/mozilla/kuma/pull/4102),
providing a framework for automated acceptance testing.  There's more work to
do, but we have a good foundation for automatically detecting more issues
before they appear in production.

Switched from Stylus to Sass for CSS
---
Kuma first started using [Stylus](http://stylus-lang.com) way back in
[2013](https://github.com/mozilla/kuma/pull/1243),
when we started MDN redesign from the
"[black](https://web.archive.org/web/20121003233220/https://developer.mozilla.org/en-US/)"
design to the current "blue" design. At the time, use of CSS preprocessors
was growing, and there wasn't a clear winner. In a
[2012 poll](https://css-tricks.com/poll-results-popularity-of-css-preprocessors/),
54% of developers had tried a preprocessor, and
[LESS](http://lesscss.org) was the most popular at 51%, probably due to its
use in Twitter Bootstrap.

In 2017, it looks like [Sass](http://sass-lang.com) is the CSS preprocessor
of choice. There are more tools and tutorials available. Twitter Bootstrap
is now just [Bootstrap](http://getbootstrap.com), and has an official
[Sass port](https://github.com/twbs/bootstrap-sass). We're planning on a lot
of front-end changes in 2017, so it is a good time to switch to a new toolset.

Stephanie Hobson (shobson)
[changed the Stylus files to Sass](https://github.com/mozilla/kuma/pull/4097),
and Jon Petto (jpetto) and Ryan Johnson (rjohnson) worked to validate the
changes, and integrate Sass into the static asset pipeline. This included
improving the build process for Docker, which can now be used
more efficiently for front-end development.

Published AWS Migration Plan
---
The Kuma team has been working toward rehosting MDN for years, updating
systems and modifying the software architecture to fit cloud computing
standards. Soon, we'll start moving services to AWS, with a goal of
rehosting production in AWS later this year.

There are a lot of moving pieces, which we've cataloged in the
[AWS Migration Plan](http://bit.ly/MDN-AWS-Plan).  Take a look to see what is
coming, or if you are having trouble sleeping.

Shipped Tweaks and Fixes
---
Other highlights from January:
* [PR 4070](https://github.com/mozilla/kuma/pull/4070):
  Improve error message when tag list is too long
  ([gautamramk](https://github.com/gautamramk)'s first PR!).
* [PR 4089](https://github.com/mozilla/kuma/pull/4089):
  Add Bulgarian to the candidate languages, and enable on the
  [staging server](https://developer.allizom.org/bg/).
* [PR 4095](https://github.com/mozilla/kuma/pull/4095):
  Add rel="nofollow" to non-indexable links
  (the first of several PRs from Jon Petto
  ([jpetto](https://github.com/jpetto)).

Planned for February
===

Ship the Sample Database
---
The Sample Database has been promised every month since October 2016, and
has slipped every month. We don't want to break the tradition: the
sample database will ship in February. See
[PR 4076](https://github.com/mozilla/kuma/pull/4076) for the remaining
tasks and to download the beta sample database.

Demo deployments in AWS
---
We are working with Josh Mize (jgmize) and Dave Parfitt (metadave) to
automate deployment of temporary instances of Kuma to AWS.  This will be
useful for demonstrating new code, as well as for load and integration
testing. This is a first step toward deploying staging and production
instances to AWS.

Read-Only Maintenance Mode
---
We are working on Read-Only Maintenance Mode, a Kuma configuration that works
against a recent database backup, displaying MDN data but not allowing login or
page editing.  This will be useful for keeping content available during
database maintenance and for load-testing. We also want to determine the effort
needed to split Kuma between read-only and read-write instances, as a
possible AWS deployment strategy.
