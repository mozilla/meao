---
layout: post
title: MozMEAO SRE Status Report - September 19, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from September 5th - September 19th.

<!--more-->

## Current work

### MDN Migration to AWS

- We've established a few [target release dates](https://github.com/mozmeao/infra/issues/493) for [our milestones](https://github.com/mozmeao/infra/milestones).
- All attachment files are [being synced from SCL3 to S3](https://github.com/mozmeao/infra/issues/412#issuecomment-329491916)
    - Previously, attachments from 2012 contained unicode characters in their filenames that prevents several *nix/AWS tools from working.
- [All HTTPD aliases have been addressed](https://github.com/mozmeao/infra/issues/241)
- [Tested urllib3 v 1.22 against Elasticsearch](https://github.com/mozmeao/infra/issues/481)
- [Implement database backup/restore process](https://github.com/mozmeao/infra/issues/401)
- [Production AWS resources have been provisioned](https://github.com/mozmeao/infra/issues/460)
    - [RDS changed to multi-AZ (part 2)](https://github.com/mozmeao/infra/issues/470)
- [Production Elasticsearch instance has been setup](https://github.com/mozmeao/infra/issues/462)
- [MIME type analysis complete](https://github.com/mozmeao/infra/issues/244)
- [Environment overrides for SCL3 settings in K8s](https://github.com/mozmeao/infra/issues/477)
- [SSL certs have been re-requested with additional names](https://github.com/mozmeao/infra/issues/416)
- [Split out credentials into Kubernetes secrets resources](https://github.com/mozmeao/infra/pull/467)
- [Create Elasticsearch stage cluster](https://github.com/mozmeao/infra/issues/470)
- [Using multi-AZ RDS for hosted MySQL (part 1)](https://github.com/mozmeao/infra/issues/470)
- Some architecture diagrams have been [added to the repo](https://github.com/mozmeao/infra/pull/472)
- [Establish a faster MySQL backup process from SCL3](https://github.com/mozmeao/infra/issues/401)

### Snippets

- Snippets has been deployed to the Portland cluster, in addition to the Frankfurt and Tokyo clusters.

- Some autoscaling inconsistencies between clusters were uncovered by [Giorgos](https://github.com/glogiotatidis/), which have been corrected via [this PR](https://github.com/mozmeao/infra/pull/504).

- The Snippets production traffic policy has been changed from latency-based to weighted between Frankfurt/Portland/Tokyo.

- [Giorgos](https://github.com/glogiotatidis/) also uncovered some Route 53 health check inconsistencies, and is working to make them more useful.

### Upcoming Portland Deis 1 cluster decommissioning

The Deis 1 cluster in Portland [decommissioning](https://github.com/mozmeao/infra/issues/404) has been pushed out until next week due to support issues related to other applications.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
