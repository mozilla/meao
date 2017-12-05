---
layout: post
title: MozMEAO SRE Status Report - December 5, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from November 14th - December 5th.

<!--more-->

## Current work

### SUMO

Work continues on the SUMO move to AWS. We've [provisioned a small RDS MySQL instance](https://github.com/mozmeao/infra/pull/657) in AWS for development and tried importing a production snapshot. The import took 30 hours on a `db.t2.small` instance, so we experimented with temporarily scaling the RDS instance to a an `db.m4.xlarge`. The import is now expected to complete in 5 hours. 

We will investigate if incremental backup/restore is an option for the production transition.


### MDN 

MDN had several short downtime events in November, caused by heavy load due to scraping. Our [K8s liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/) often forced pods to restart when MySQL was slow to respond. 

Several readiness and liveness probe changes were issued by 
[@escattone](https://github.com/escattone) and [@jwhitlock](https://github.com/jwhitlock) to help alleviate the issue:

- [eliminate DB dependency from liveness & readiness endpoints in Kuma](https://github.com/mozmeao/infra/issues/660)
- [adjust liveness tests, avoid DB query in middleware](https://github.com/mozilla/kuma/pull/4579)
- [increase threshold of failure for liveness/readiness probes](https://github.com/mozmeao/infra/pull/665)


The [November 2017 Kuma report](https://mozilla.github.io/meao/2017/12/05/kuma-report/)  has additional details.


We now have a few load balancer infrastructure tests for MDN, implemented in [this](https://github.com/mozmeao/infra/pull/664) pull request.

#### MDN Interactive-examples

Caching is now more granular due to [setting different cache times for different assets](https://github.com/mdn/interactive-examples/issues/334).

### Bedrock

Bedrock is transitioning to [a local Sqlite DB and clock process in every container](https://github.com/mozilla/bedrock/pull/5236). This removes the dependency on RDS and makes running Bedrock cheaper. In preparation for this change, [S3 buckets have been created for dev, stage and prod](https://github.com/mozmeao/infra/pull/669).


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
