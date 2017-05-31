---
layout: post
title: MozMEAO SRE Status Report - 5/30/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from May 23rd - May 30th.

<!--more-->

## Current work

### Bedrock (mozilla.org)

Bedrock has been stable in production on Kubernetes for 7 days. The current traffic policy includes Virginia (K8s), Tokyo (K8s), Portland (Deis 1) and Ireland (Deis 1).

- application limits/requests [were increased](https://github.com/mozmar/infra/issues/258#issuecomment-303467009) to deal with initial performance issues.

- we're [discussing](https://github.com/mozmar/infra/issues/271) replacing the usage of assets.mozilla.org on www.mozilla.org.

### nucleus.mozilla.org

Nucleus [has been moved](https://github.com/mozmar/infra/issues/184) from our Deis 1 infrastructure to Kubernetes in Virginia.

### surveillance.mozilla.org

The surveillance site [has been moved](https://github.com/mozmar/infra/issues/184) from our Deis 1 infrastructure to Kubernetes in Virginia.

### snippets.mozilla.org

Web QA tests [have been added](https://github.com/mozmar/snippets-service/pull/235) by [Stephen Donner](https://github.com/stephendonner) to the snippets service.

## Future work

### Move basket.mozilla.org to K8s

We're planning to move basket to Kubernetes shortly after the nucleus migration, and then proceed to decommission existing infrastructure.

### Scale down Deis 1 clusters

Now that were serving a large portion of production traffic via Kubernetes, we can safely scale down the Portland and Ireland Deis 1/Fleet clusters to reduce AWS costs. We'll also be provisioning a Portland Kubernetes cluster in the near future.

### Decommission openwebdevice.org

We are waiting on some [internal communications](https://github.com/mozmar/infra/issues/205) before moving forward.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)