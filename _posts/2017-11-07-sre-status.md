---
layout: post
title: MozMEAO SRE Status Report - November 7, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from October 31st - November 7th.

<!--more-->

## Current work

### SUMO

Work progresses on a SUMO development environment for use with Kubernetes in AWS.

- [S3](https://github.com/mozilla/kitsune/issues/2933) and [Cloudfront](https://github.com/mozilla/kitsune/issues/2934) distributions have been provisioned, and [DNS](https://github.com/mozilla/kitsune/issues/2899#issuecomment-342610541) has been setup for the following domains:
    - [https://dev-cdn.sumo.mozilla.net/](https://dev-cdn.sumo.mozilla.net/)
    - [https://stage-cdn.sumo.mozilla.net/](https://stage-cdn.sumo.mozilla.net/)
    - [https://prod-cdn.sumo.mozilla.net/](https://prod-cdn.sumo.mozilla.net/)

- We decided to use a small [elastic.co](https://cloud.elastic.co)-hosted Elasticsearch instance instead of using [the Helm chart](https://github.com/kubernetes/charts/tree/master/incubator/elasticsearch) due to [difficulties getting the chart to run](https://github.com/mozilla/kitsune/issues/2936#issuecomment-341722552).
- The team has decided use MySQL or MariaDB instead of pursuing a migration to Postgres before moving to AWS.

### MDN 

- The [October 2017 Kuma Report](https://mozilla.github.io/meao/2017/11/07/kuma-report/) describes the MDN move to AWS.
- The [mdn-samples.mozilla.org]() domain is in the [process of being moved to Kubernetes](https://github.com/mdn/samples-server/pull/47).
    - See also [https://bugzilla.mozilla.org/show_bug.cgi?id=1414294](https://bugzilla.mozilla.org/show_bug.cgi?id=1414294)
- We're now varying the CloudFront cache on the querystring parameter revision, which is used to refresh embeded live samples when the document is updated. 
    - [bug 1414419: Vary MDN attachment CDN on ?revision=X](https://github.com/mozmeao/infra/pull/639)
- Work to get Jenkins to push to Kubernetes is in progress in the following PRs:
    - [bug 1406546: refactor groovy code to handle kumascript as well as kuma](https://github.com/mozilla/kuma/pull/4503)
    - [bug 1406546: add code for deploying kumascript to stage](https://github.com/mdn/kumascript/pull/395)

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
