---
layout: post
title: MozMEAO SRE Status Report - July 18, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from July 11th - July 18th.

<!--more-->

## Current work

### Kubernetes

- `basket`, `snippets`, `snippets-stats`, and `careers` [have been deployed to our Frankfurt cluster](https://github.com/mozmar/infra/issues/301). Once some last minute tests pass, we'll enable these applications via updates to our Route 53 traffic policies. 

### Decommissioning old infrastructure

We're planning on [decommissioning our Deis 1 infrastructure](https://github.com/mozmar/infra/issues/336) starting with Ireland, as our apps are all running on Kubernetes in multiple regions. Once the Ireland cluster has been shut down, we'll continue on to our Portland cluster.

Additionally, we'll be [scaling down our Virginia cluster](https://github.com/mozmar/infra/issues/335), as our apps are being moved to regions with lower latencies for the majority of our users. 

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
