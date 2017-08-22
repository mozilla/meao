---
layout: post
title: MozMEAO SRE Status Report - August 22, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from August 15th - August 22nd.

<!--more-->

## Current work

### MDN Migration to AWS


- MDN ELB automation has been implemented using Kubernetes `LoadBalancer` resources. [SSL](https://github.com/mozmeao/infra/pull/430) and [AWS security groups](https://github.com/mozmeao/infra/pull/439) have been configured, and port 80 is open to [forward all http requests to https](https://github.com/mozmeao/infra/pull/439) (although our Cloudfront distribution will most likely handle this for us).
- [RDS automation has been implemented](https://github.com/mozmeao/infra/pull/434) to provision staging and production MySQL instances. Stage will be configured to use a `db.t2.medium`, and production will use a `db.m4.xlarge`. At some point, we may experiment with [AWS memory optimized database instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/memory-optimized-instances.html).
- [Cloudfront automation](https://github.com/mozmeao/infra/issues/427) has been implemented to serve stage and production:
    - for prod, we'll use: `cdn.mdn.mozilla.net` / `cdn.mdn.moz.works`
    - for stage, we'll use: `stage-cdn.mdn.mozilla.net` / `stage-cdn.mdn.moz.works`
 
- The [ability to serve legacy files](https://github.com/mozmeao/infra/pull/431) from Kuma/Django [has been implemented](https://github.com/mozilla/kuma/pull/4365). There were some file system permissions issue related to Docker, but these were solved using [a Kubernetes Job](https://github.com/mozmeao/infra/issues/422) to set the correct values upon install.
- [Certificates for stage and prod have been requested](https://github.com/mozmeao/infra/issues/416).

### Upcoming Portland Deis 1 cluster decommissioning

The Deis 1 cluster in Portland [decommissioning](https://github.com/mozmeao/infra/issues/404) has been pushed out until next week due to support issues related to other applications.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
