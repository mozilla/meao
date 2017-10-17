---
layout: post
title: MozMEAO SRE Status Report - October 17, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from October 3rd - October 17th.

<!--more-->

## Current work

### MDN Migration to AWS

MDN is now running in AWS on Kubernetes. 

Our [migration project](https://github.com/mozmeao/infra/projects/4) has been closed, and a new [post-migration project](https://github.com/mozmeao/infra/projects/5) has been opened.

##### Migration work

- [Implement monitoring for MDN](https://github.com/mozmeao/infra/issues/398)
    - included in this issue are New Relic setup, Datadog Redis queue monitoring, and Deadmanssnitch backup cronjob monitoring.
- [Celery: use long options, send log to stdout](https://github.com/mozmeao/infra/pull/555)
- [Update prod and stage configuration files](https://github.com/mozmeao/infra/pull/557)
- [Create new MDN prod traffic policy version](https://github.com/mozmeao/infra/issues/563)

##### Migration testing
- [Manual test of MM in AWS https://prod.mdn.moz.works (for second MM traffic test)](https://github.com/mozmeao/infra/issues/552)
- [Manually test staging in Portland K8s](https://github.com/mozmeao/infra/issues/527)


##### Post migration

- [Jenkins deployments to stage/prod](https://github.com/mozmeao/infra/issues/394)
- [Frankfurt K8s maintenance mode cluster using RDS read-replica](https://github.com/mozmeao/infra/issues/607)
- [Cache header improvements](https://github.com/mozmeao/infra/issues/578)
- [Bug 1361729: Switch to alabaster theme](https://github.com/mozilla/kuma/pull/4457)
- [Deploy hash-tagged Kumascript Docker images](https://github.com/mozmeao/infra/issues/574)
- [Investigate issues with sending emails](https://github.com/mozmeao/infra/issues/576)
- [Decide on a public name for staging development](https://github.com/mozmeao/infra/issues/584)
- [Setup mdn-restore-prod cronjob in our Frankfurt cluster](https://github.com/mozmeao/infra/issues/588)

### Upcoming Portland Deis 1 cluster decommissioning

Applications are being moved off Deis 1 to support [decommissioning the Deis 1 cluster in Portland](https://github.com/mozmeao/infra/issues/404).


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
