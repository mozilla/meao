---
layout: post
title: MozMEAO SRE Status Report - October 31, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from October 24th - October 31st.

<!--more-->

## Current work

### SUMO

An initial infra project structure for SUMO, along with S3 + Cloudfront distributions for dev, stage and production environments has been created in [this PR](https://github.com/mozmeao/infra/pull/626).

Future SUMO migration tasks will be tracked [here](https://github.com/mozilla/kitsune/projects/2), while infrastructure code will be stored [here](https://github.com/mozmeao/infra/tree/master/apps/sumo). 

### MDN 

MDN attachments are now behind a [Cloudfront CDN](https://aws.amazon.com/cloudfront/) to help reduce load on the MDN web [pods](https://kubernetes.io/docs/concepts/workloads/pods/pod/).

- [High level issue](https://github.com/mozmeao/infra/issues/590)
- [Include untrusted-domain origin in allowed hosts](https://github.com/mozmeao/infra/pull/627)
- [Add kuma ATTACHMENT_ORIGIN setting](https://github.com/mozmeao/infra/pull/623)
- [Provision MDN attachments CDN](https://github.com/mozmeao/infra/pull/622)

### SRE misc


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
