---
layout: post
title: MozMEAO SRE Status Report - September 26, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from September 19th - September 26th.

<!--more-->

## Current work

### MDN Migration to AWS

We've successfully completed a series of tests against MDN hosted in AWS. 

#### Testing

- [Manually test maintenance mode in stage AWS](https://github.com/mozmeao/infra/issues/498) (success 🎉)
- [Manually test maintenance mode in prod AWS](https://github.com/mozmeao/infra/issues/515) (success 🎉)
- [Manually test maintenance mode in SCL3 stage](https://github.com/mozmeao/infra/issues/510) (success 🎉)
- [Maintenance mode traffic test: 5% to K8s](https://github.com/mozmeao/infra/issues/516) (success 🎉)
- [Maintenance mode traffic test: 15% / 50% / 100%](https://github.com/mozmeao/infra/issues/518) (success 🎉)

#### Migration work

- [Use clean-css in Kuma Docker image](https://github.com/mozmeao/infra/issues/457)
- [Add general security headers](https://github.com/mozmeao/infra/issues/482)
- [Deploy backup service in prod](https://github.com/mozmeao/infra/issues/506)
- [Deploy a maintenance mode config for manual testing in AWS](https://github.com/mozmeao/infra/issues/497)
- [MDN weighted DNS setup for testing](https://github.com/mozmeao/infra/issues/487)
- [Plan memcached/redis queue migration for go-live](https://github.com/mozmeao/infra/issues/402#issuecomment-330940636)
- [Create MDN prod services](https://github.com/mozmeao/infra/issues/507)
- [K8s rolling update testing](https://github.com/mozmeao/infra/issues/382)
- [Add checklist for read/write staging test](https://github.com/mozmeao/infra/pull/500)
- [Maintenance mode release plan](https://github.com/mozmeao/infra/issues/409)
- [Configure AWS staging for read/write testing](https://github.com/mozmeao/infra/issues/517)
- [Set stage/prod cronjob history limits](https://github.com/mozmeao/infra/issues/523)
- [MDN initialization checklist](https://github.com/mozmeao/infra/pull/509)
- [Disallow robots everywhere but developer.mozilla.org](https://github.com/mozmeao/infra/pull/528)



### Upcoming Portland Deis 1 cluster decommissioning

Applications are being moved off Deis 1 to support [decommissioning the Deis 1 cluster in Portland](https://github.com/mozmeao/infra/issues/404).


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
