---
layout: post
title: MozMEAO SRE Status Report - February 28, 2018
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from February 16 - February 28th.

<!--more-->

## Current work

### support.mozilla.org (SUMO)

Most of our recent efforts have been related to the SUMO migration to AWS. We'll be running the stage and production environments in our Oregon-A and Oregon-B clusters, with read-only failover in Frankfurt.  

- [@pmac](https://github.com/pmac/) and [@glogiotatidis](https://github.com/glogiotatidis/) [cleaned up our `ALLOWED_HOSTS` settings](https://github.com/mozilla/kitsune/pull/3062) to make them more secure using a new [django-allow-cidr](https://pypi.python.org/pypi/django-allow-cidr/) package. There's an excellent blog post on their work [here](https://mozilla.github.io/meao/2018/02/27/django-k8s-elb-health-checks/).

- We've provisioned [a MySQL instance in Oregon](https://github.com/mozmeao/infra/pull/738), and production data is currently being replicated to this instance from SUMO's current home in the SCL3 datacenter. 

- Our us-west-2 Redis cluster does not have the capacity for SUMO, so [a new cluster has been provisioned](https://github.com/mozmeao/infra/pull/744).

- Stage and production load balancers [have been created](https://github.com/mozmeao/infra/pull/741) for our Oregon-A, Oregon-B and Frankfurt clusters.

- Certificates have [been requested and approved](https://github.com/mozmeao/infra/issues/742) for SUMO stage and production services. As part of the same issue, we worked out [how DNS will work](https://github.com/mozmeao/infra/issues/742#issue-300354040).


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
