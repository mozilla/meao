---
layout: post
title: MozMEAO SRE Status Report - June 13, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from June 6th - June 13th.

<!--more-->

## Current work

### irlpodcast.org provisioning

[We've provisioned](https://github.com/mozmar/infra/issues/283) infrastructure for [https://irlpodcast.org](https://irlpodcast.org), including S3 and CloudFront resources.
More about this site coming soon!

### Frankfurt Kubernetes cluster provisioning

[We're provisioning](https://github.com/mozmar/infra/issues/293) a new Kubernetes 1.6.4 cluster in Frankfurt (`eu-central-1`). This cluster takes advantage of features in new versions of [kops](https://github.com/kubernetes/kops), [helm](https://helm.sh/), and [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

We've modified our [New Relic](https://newrelic.com/), [Datadog](https://www.datadoghq.com/), and [mig](https://github.com/mozilla/mig) [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) with [tolerations](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#taints-and-tolerations-beta-feature) so we can gather system metrics from both K8s master and worker nodes.

The first apps to be installed in this cluster will be [bedrock](https://github.com/mozilla/bedrock) and [basket](https://github.com/mozmar/basket/).

### Basket move to Kubernetes

Basket [has been moved](https://github.com/mozmar/infra/issues/179) to Kubernetes! We experienced some networking issues in our Virginia Kubernetes cluster, so traffic has been routed away from this cluster for the time being.

### Snippets

The Firefox 56 activity stream will ship to some users, with some form of snippets integration.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)