---
layout: post
title: MozMEAO SRE Status Report - July 25, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from July 18th - July 25th.

<!--more-->

## Current work

### MDN

We started discussing hosting for the MDN Live Sample Code Editor using a strategy [similar to what was used](https://github.com/mozmeao/infra/pull/287) for [IRLPodcast](https://irlpodcast.org/).

- MDN discussion [here](https://github.com/mdn/interactive-examples/issues/54).
- Infrastructure discussion [here](https://github.com/mozmeao/infra/issues/362).


### Ireland Deis 1/Fleet cluster decommissioning

Now that our Frankfurt Kubernetes cluster is [up and running](https://github.com/mozmeao/infra/issues/301), we're getting ready to [decommission our Ireland Deis 1/Fleet cluster](https://github.com/mozmeao/infra/issues/336).

Once the Ireland cluster has been shut down, we'll continue on to our Portland cluster.

### Virginia cluster decom

In order to decommission our Virginia Kubernetes cluster, we [need to finish moving a few smaller apps](https://github.com/mozmeao/infra/issues/335#issuecomment-317538890 ) to a different region or hosting:

- [Nucleus to K8s Frankfurt](https://github.com/mozmeao/infra/issues/363)
- [Surveillance to S3 + Cloudfront](https://github.com/mozmeao/infra/issues/332)
- [Mdn-dev to K8s Frankfurt](https://github.com/mozmeao/infra/issues/364)

### Kubernetes

- `snippets` and `snippets-stats` are now running in our Frankfurt cluster and have been added to each respective Route 53 traffic policy.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
