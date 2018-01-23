---
layout: post
title: MozMEAO SRE Status Report - January 23, 2018
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from December 2017 - January 23.

<!--more-->

## Current work

### SRE general

We're busy setting up multiple Kubernetes 1.8 clusters in us-west-2 to serve SUMO, Bedrock and other MozMEAO applications. These new clusters will [replace our Deis 1 cluster](https://github.com/mozmeao/infra/issues/705) in the same region.

### www.mozilla.org

The Bedrock team will be [moving from an RDS database to updates distributed via S3](https://github.com/mozilla/bedrock/pull/5334). This will make Bedrock hosting cheaper and easier to manage.

Additionally, Bedrock needs to be tweaked to run on Kubernetes natively as [Deis Workflow is being discontinued](https://deis.com/blog/2017/deis-workflow-final-release/).

### MDN

MDN is switching it's [Celery](http://www.celeryproject.org/) results backend [from MySQL to Redis](https://github.com/mozilla/kuma/pull/4615), to avoid database reads/writes. No significant difference in throughput noticed.


### support.mozilla.org (SUMO)

Work is progressing quickly on the SUMO move from SCL3 to AWS.

User media is [now hosted by S3 and Cloudfront in SCL3](https://github.com/mozilla/kitsune/issues/3003) as of 2017-01-17 14:14 UTC. This makes our migration easier as it's one less component we have to plan for on go-live day. 

We've been [discussing SUMO database architecture](https://github.com/mozilla/kitsune/issues/3012) with a focus on high uptime. We're also [discussing our Elasticsearch architecture](https://github.com/mozilla/kitsune/issues/3013).

Work on a new CDN is [in-progress for hosting static media in AWS](https://github.com/mozilla/kitsune/issues/2949). We'll need to request a few DNS changes and certificates in order to proceed.

The team is also working on establishing MySQL replication between SCL3 and RDS, in order to significantly decrease the deployment window on migration day.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
