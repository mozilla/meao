---
layout: post
title: MozMEAO SRE Status Report - 5/9/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from May 3rd - May 9th.

<!--more-->

## Current work

### Bedrock (mozilla.org)

##### Bedrock multi-region RDS provisioning

Work continues to move Bedrock from Deis 1/Fleet to Kubernetes. The team has [implemented Terraform automation](https://github.com/mozmar/infra/pull/209) to provision RDS instances in multiple regions.

##### Demo deployments

Jenkins deployments have been [restructured](https://github.com/mozilla/bedrock/pull/4808), and demos now build in main pipeline. This was a meaty PR from [pmac](https://github.com/pmac), and a [motivation to upgrade](https://github.com/mozilla/bedrock/pull/4808#issuecomment-299883086) Deis Workflow to the latest version (more info below).

Next actions: 

- create persistent development, staging, and production applications using RDS (Postgres)
- enable deployments to new apps in Jenkins
- Cloudfront distribution and integration testing

### MDN

We're working on migrating custom Apache config for MDN directly in Kuma/Django for the eventual move to AWS. Most of the Apache rewrites/redirects have [been implemented in Kuma](https://github.com/mozilla/kuma/pull/4220), with only a [few remaining](https://github.com/mozilla/kuma/blob/master/configs/htaccess).

### Basket

The FxA team would like to [send events](https://bugzilla.mozilla.org/show_bug.cgi?id=1358123) (FXA_IDs) to Basket and Salesforce, and need SQS queues in order to move forward. We automated the [provisioning of dev/stage/prod SQS queues](https://github.com/mozmar/infra/issues/208), and passed off credentials to the appropriate engineers.

### Kubernetes / Deis Workflow

Deis Workflow has been [upgraded to latest version (2.14.20) in Virginia and Tokyo](https://github.com/mozmar/infra/issues/213). We hit a few snags during the first upgrade, as our Workflow install has some [customization](https://github.com/mozmar/infra/blob/master/k8s/install/stage2_functions.sh#L124-L215) that wasn't applied. Subsequent upgrades should be easier, as we’ve [automated the process via a script](https://github.com/mozmar/infra/pull/219) (with minor tweaks in [this PR](https://github.com/mozmar/infra/pull/220)).

### Snippets

##### Snippets-stats is running in Tokyo and Virginia.

`snippet-stats` was already running on our Deis 1 clusters in Oregon and Ireland, however [Giorgos](https://github.com/glogiotatidis/) enabled it on our Virginia and Tokyo Kubernetes clusters.

- Metrics have been [validated](https://github.com/mozmar/infra/issues/174) for snippets-stats in Virginia and Tokyo.
- Application memory/CPU limits and autoscaling have been [configured in Tokyo and Virginia](https://github.com/mozmar/infra/issues/164).

#### Issues with `HTTP_X_FORWARDED_PROTO` header not set for for snippets-*.virginia.moz.works

We created a generic [http to https redirector](https://github.com/mozmar/infra/pull/163) [service](https://github.com/mozmar/infra/blob/master/k8s/install/stage2_functions.sh#L303-L305) that runs in Kubernetes. This allows Kubernetes to handle forwarding `http` to `https` for us without having custom implementations in each application. However, there remained an [issue](https://github.com/mozmar/infra/issues/101) in our current ELB setup where `HTTP_X_FORWARDED_PROTO` was not set, and thus Django cannot be aware whether a connection is secure or not.

[pmac](https://github.com/pmac) has implemented an alternative to `X-Forwarded-Proto` using [an HTTPS env var and a SWGIRequest subclass](https://github.com/mozilla/bedrock/commit/8124b66cb3f4f6faa337dde999df104145ebb29c).

Thanks to [Giorgos](https://github.com/glogiotatidis/) and [pmac](https://github.com/pmac) for their hard work on this!

### Decommission webwewant.mozilla.org

`webwewant.mozilla.org` has been [decommissioned](https://github.com/mozmar/infra/issues/203). All requests to `webwewant.mozilla.org` are [now being forwarded](https://bugzilla.mozilla.org/show_bug.cgi?id=1361114) to [https://www.mozilla.org](https://www.mozilla.org).

## Future work

### Decommission openwebdevice.org

Waiting for some [internal communications](https://github.com/mozmar/infra/issues/205) before moving forward.

### Nucleus

We're planning to move nucleus to Kubernetes, and then proceed to decommissioning current nucleus infra.

### Basket

We're planning to move basket to Kubernetes shortly after the nucleus migration, and then proceed to decommissioning existing infra.


### New Kubernetes cluster

We'll be creating a new Kubernetes cluster in Portland so we can take advantage of EFS to support MDN in that region. We currently run many of our services from Portland, Virginia, and Ireland. The new cluster will be created in an entirely new VPC, and existing resources will not be shared.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)