---
layout: post
title: MozMEAO SRE Status Report - October 24, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from October 17th - October 24th.

<!--more-->

## Current work

### SUMO

[@glogiotatidis](https://github.com/glogiotatidis/), [@jgmize](https://github.com/jgmize/), [@metadave](https://github.com/metadave/) and [@pmac](https://github.com/pmac/) are starting to plan on a [SUMO](https://github.com/mozilla/kitsune) migration from the SCL3 datacenter to AWS. Work will be tracked in a forthcoming project in the [https://github.com/mozilla/kitsune](https://github.com/mozilla/kitsune) repo. 

### MDN 

- [Caching headers are being improved for file serving](https://github.com/mozmeao/infra/issues/578). This will allow us to use Cloudfront effectively to help reduce load on MDN `web` pods.

### SRE misc

- [careers.mozilla.org](https://careers.mozilla.org/) certs have been renewed via [Amazon Certificate Manager](https://aws.amazon.com/certificate-manager/). 
- Snippets buckets in `eu-central-1`, `ap-northeast-1`, and `us-east-1` have been [merged into a single bucket](https://github.com/mozmeao/infra/issues/559) in `us-west-2`, so unused buckets [have been deleted](https://github.com/mozmeao/infra/issues/567). 
- Deis RDS instances [have been resized](https://github.com/mozmeao/infra/pull/618) to use a `t2.small` instance type in `eu-central-1` and `ap-northeast-1` to reduce costs.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
