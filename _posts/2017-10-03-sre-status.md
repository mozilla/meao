---
layout: post
title: MozMEAO SRE Status Report - October 3, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from September 26th - October 3rd.

<!--more-->

## Current work

### MDN Migration to AWS

We've successfully completed a series of tests against MDN hosted in AWS, but we have a few more to complete before moving to AWS.

#### Testing

- A successful MDN maintenance mode test was performed on Tuesday October 3rd 2017, at 2pm eastern / 11 pacific.

#### Migration work

- Restrict URLs for untrusted (files / samples) and CDN domains. PR [529](https://github.com/mozmeao/infra/issues/529)

- New Relic support has been added to the MDN Kubernetes deployments in these PRs: [549](https://github.com/mozmeao/infra/pull/549), [548](https://github.com/mozmeao/infra/pull/548), [547](https://github.com/mozmeao/infra/pull/547), [542](https://github.com/mozmeao/infra/pull/542)

- MDN K8s crontasks have been updated to change the process user:group to `kuma`, add [Deadmanssnitch](https://deadmanssnitch.com) support, and some optimizations to prevent `aws s3 sync` from timing out. PR [533](https://github.com/mozmeao/infra/pull/533)

- Unused MDN S3 buckets have been deleted, with some manual cleanup due to versioning enabled on the buckets. PR [531](https://github.com/mozmeao/infra/pull/531)


### Upcoming Portland Deis 1 cluster decommissioning

Applications are being moved off Deis 1 to support [decommissioning the Deis 1 cluster in Portland](https://github.com/mozmeao/infra/issues/404).


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
