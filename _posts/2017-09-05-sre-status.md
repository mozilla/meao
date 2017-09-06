---
layout: post
title: MozMEAO SRE Status Report - September 5, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from August 29th - September 5th.

<!--more-->

## Current work

## Deis Workflow: Final Release

The final release of Deis Workflow is [scheduled for September 9th, 2017](https://deis.com/blog/2017/deis-workflow-final-release/). We use Deis Workflow to help run [Basket](https://github.com/mozmeao/basket), [Bedrock](https://github.com/mozilla/bedrock), [Snippets](https://github.com/mozmeao/snippets), and [Careers](https://github.com/mozmeao/lumbergh), so each project will need to be modified to use Kubernetes directly (instead of interfacing with Kubernetes via Deis).

More info [here](https://github.com/mozmeao/infra/issues/448#issuecomment-326035173).

### MDN Migration to AWS

- [Django views have been implemented](https://github.com/mozilla/kuma/pull/4401) for serving sitemaps as well as kuma and kumascript revision hashes.
    - an endpoint [has been added](https://github.com/mdn/kumascript/pull/303) for serving revision hashes.
    - revision hashes [are now persisted](https://github.com/mozilla/kuma/pull/4399) in Docker images.
- [Cloudfront automation](https://github.com/mozmeao/infra/issues/427) has been provisioned for serve stage and production:
    - for prod, we'll use: `cdn.mdn.mozilla.net` / `cdn.mdn.moz.works`
    - for stage, we'll use: `stage-cdn.mdn.mozilla.net` / `stage-cdn.mdn.moz.works`
    - Certificates for each domain [have been requested](https://github.com/mozmeao/infra/pull/440#issuecomment-327220954).
    - DNS changes [have been requested](https://bugzilla.mozilla.org/show_bug.cgi?id=1397006).
 
### Analytics eval

We're [evaluating](https://github.com/mozmeao/infra/issues/453) [Snowplow](https://github.com/snowplow/snowplow) to see if it will meet our analytics needs.

### Upcoming Portland Deis 1 cluster decommissioning

The Deis 1 cluster in Portland [decommissioning](https://github.com/mozmeao/infra/issues/404) has been pushed out until next week due to support issues related to other applications.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
