---
layout: post
title: MozMEAO SRE Status Report - June 20, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from June 13th - June 20th.

<!--more-->

## Current work

### Static site hosting

- The irlpodcast site now has a [staging environment](https://github.com/mozmar/infra/pull/305) also hosted in S3 with CloudFront. Additionally, [Jenkins](https://github.com/mozmar/infra/issues/295) has been updated to deploy to staging and production via git push.

- We're going to move viewsourceconf.org from Kubernetes to S3 and CloudFront hosting. [Production](https://github.com/mozmar/infra/pull/306) and [staging](https://github.com/mozmar/infra/pull/316) environments have been provisioned, but we'll need to update Jenkins to push changes to these new environments.

### Basket move to Kubernetes

- Basket will switch to [HTTPS only](https://github.com/mozmar/basket/issues/24).

### Kubernetes (general)

Our [DataDog](https://www.datadoghq.com/), [New Relic](https://newrelic.com/) and [MIG](http://mig.mozilla.org/) DaemonSets have been [configured](https://github.com/mozmar/infra/issues/227#issuecomment-308245470) to use Kubernetes [tolerations](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#taints-and-tolerations-beta-feature) to schedule pods on master nodes. This allows us to capture metrics from K8s master nodes in additional to worker nodes.

#### Frankfurt Kubernetes cluster provisioning

Work continues to enable our apps in the new Frankfurt Kubernetes cluster. In addition, we're working on [automating our app](https://github.com/mozmar/infra/pull/311) installs as must as possible.

### MDN

- ElasticSearch will be upgraded to 2.4 in SCL3 production, June 21 11 AM PST

- We may [reconsider](https://github.com/mozmar/infra/issues/193) [self-hosting](https://github.com/mozmar/infra/issues/193#issuecomment-301583226) ElasticSearch.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
