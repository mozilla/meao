---
layout: post
title: MozMEAO SRE Status Report - August 8, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from August 1st - August 8th.

<!--more-->

## Current work

### MDN Migration to AWS

- Our goal is to pilot a read-only maintenance mode with Kubernetes-hosted MySQL. For production, there's some work related to MySQL custom collation that needs to be resolved before we move to [AWS RDS](https://aws.amazon.com/rds/). More on this in coming weeks.
- We've implemented [Terraform automation for redis, memcached and EFS](https://github.com/mozmeao/infra/issues/378) for use in our Portland Kubernetes cluster.
- The remaining [httpd rewrites have been implemented in Django](https://github.com/mozmeao/infra/issues/217). This allows us to move from Apache httpd in SCL3 to an all-Django deployment in Kubernetes.
- We're going to be storing static samples, diagrams, and presentations in a shared EFS persistent volume, and there's [work in progress](https://github.com/mozmeao/infra/issues/237) on an automated backup solution to [Amazon S3](https://aws.amazon.com/s3/).
- Additionally, we're working on a [solution to synchronize content from SCL3 to S3](https://github.com/mozmeao/infra/issues/197) to prep for stage/production environments.
- This week we'll be [evaluating hosted Elasticsearch from elastic.co ](https://github.com/mozmeao/infra/issues/383).

### Virginia and EUW cluster decommissioning

- Both [Virginia (Kubernetes 1.5/Deis Workflow)](https://github.com/mozmeao/infra/issues/335) and [Ireland (Fleet/Deis 1)](https://github.com/mozmeao/infra/issues/336) have both been decommissioned. Some cleanup work remains, including removing references from documentation, and cleaning up credentials.

### Upcoming Portland Deis 1 cluster decommissioning

The Deis 1 cluster in Portland is tentatively [scheduled to be decommissioned next week](https://github.com/mozmeao/infra/issues/404). 


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
