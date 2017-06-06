---
layout: post
title: MozMEAO SRE Status Report - 6/6/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from May 30th - June 6th.

<!--more-->

## Current work

### Scale down Deis 1 clusters

Now that [bedrock](https://github.com/mozmar/infra/issues/178), [nucleus](https://github.com/mozmar/infra/issues/184), [surveillance](https://github.com/mozmar/infra/issues/269), and [viewsourceconf](https://github.com/mozmar/infra/issues/20) have been deployed to Kubernetes, [we scaled down our Portland Deis 1 cluster](https://github.com/mozmar/infra/issues/268) from 10 nodes to 6 to save on AWS costs. Additionally, Deis 1 [ELB's](https://aws.amazon.com/elasticloadbalancing/) for surveillance, viewsourceconf, and nucleus have been decommissioned.

### Cloudflare to Datadog service running in Kubernetes

The Cloudflare to Datadog service that was previously running in Deis 1 [is now running in Kubernetes](https://github.com/mozmar/infra/issues/122). Additionally, an external contributor has submitted a [pull request](https://github.com/kubernetes/charts/pull/780) to add this service to the Kubernetes charts repo. The PR looks to be abandoned, so it may be closed without being merged within a few days. If this happens, we'll open a new PR with any requested changed from the current PR.

### Cloudfront Provisioning

We've started work on provisioning [Cloudfront](https://aws.amazon.com/cloudfront/), a global content delivery network service, for our [bedrock staging](https://github.com/mozilla/bedrock) environment. 
Once we iron out the wrinkles with bedrock stage, we'll continue on to bedrock prod.

### Preparing to move basket.mozilla.org to Kubernetes

Work has started to [move Basket to Kubernetes](https://github.com/mozmar/infra/issues/179).

[pmac](https://github.com/pmac) has completed work to [build and deploy Basket with Jenkins](https://github.com/mozmar/basket/pull/22) similar to how our Bedrock deployment work.

### Evaluation of Kubewatch

We [tried](https://github.com/mozmar/infra/issues/278) [Kubewatch](https://github.com/skippbox/kubewatch), a service to watch Kubernetes events and report them to Slack. However, this doesn't seem like the right tool for us, as it currently doesn't allow us to filter the many notifications that we get.

## Future work

### Decommission openwebdevice.org

We are waiting on some [internal communications](https://github.com/mozmar/infra/issues/205) before moving forward.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)