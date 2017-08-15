---
layout: post
title: MozMEAO SRE Status Report - August 15, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from August 8th - August 15th.

<!--more-->

## Current work

### MDN Migration to AWS

- We've [setup a few cronjobs](https://github.com/mozmeao/infra/issues/408) to periodically sync static files from the current SCL3 datacenter to an S3 bucket. Our Kubernetes development environment runs a cronjobs that pulls these files from S3 to a local EFS mount.
  - There was [some additional work](https://github.com/mozmeao/infra/issues/197#issuecomment-321078100
) needed to deal with files in SCL3 that contained unicode characters in their names.

- A [cronjob in Kubernetes](https://github.com/mozmeao/infra/issues/237) has been implemented to backup new files uploaded to our shared EFS volume.

- We’ve [finished our evaluation](https://github.com/mozmeao/infra/issues/383) of hosted Elasticsearch from elastic.co, which we'll be using for our initial migration in production.


### Upcoming Portland Deis 1 cluster decommissioning

The Deis 1 cluster in Portland is tentatively [scheduled to be decommissioned later this week](https://github.com/mozmeao/infra/issues/404). 


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
