---
layout: post
title: MozMEAO SRE Status Report - 5/2/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from April 25th - May 2nd.

<!--more-->

## Current work

### Bedrock (mozilla.org)

##### Bedrock CDN

The SRE team is currently evaluating different [CDN options](https://github.com/mozmar/infra/issues/32) for Bedrock. The CDN that we choose needs to have support for the `Accept-Language` header, which CloudFront and Fastly both appear to provide. Next up is testing CloudFront with a bedrock demo deployment.

##### Bedrock moving to Kubernetes

Our Fleet and Deis 1 infrastructure will eventually be replaced with Kubernetes and Deis Workflow. [pmac](https://github.com/pmac) and [jgmize](https://github.com/jgmize/) have bedrock deployed in our Virginia Kubernetes cluster. Minor issues with https redirects were uncovered, but have been resolved. Next steps are getting integration tests working and trying Cloudfront with this deployment.

##### Bedrock log analysis

The bedrock durable team is looking to gather some traffic metrics for `/firefox`, and using [AWS Athena](https://aws.amazon.com/athena/) to query the data in the [S3 bucket populated by Papertrail](https://medium.com/@dnorth98/analyzing-papertrail-logs-with-aws-athena-2427d3dd14f2) looks like a viable solution. 

##### old resources in SCL3

[pmac](https://github.com/pmac/) is going to followup on moving old SCL3 Bedrock resources to an S3 bucket for backup.

### MDN

The SRE team has been working on the analysis of the existing SCL3 MDN deployment and it's migration to AWS.

Below are some issues and PR's related to this work:

- [Multi-region provisioning PR](https://github.com/mozmar/infra/pull/190)
	- Refactor existing S3 automation into a shared directory
	- region-specific resources (EFS) are easily created in any region w/ ~5 lines of env var + bash. Currently provisioned for our Virginia K8s cluster (`us-east-1`).
- [We won’t be migrating or running the existing Apache httpd in AWS](https://github.com/mozmar/infra/issues/180). As much as possible will be moved to Kuma.
- [We’ll be using EFS instead of S3](https://github.com/mozmar/infra/issues/183) where appropriate to minimize code changes
	- EFS is only available in the following regions: EU (Ireland), Asia Pacific (Sydney), US East (N. Virginia), US East (Ohio), US West (Oregon)
- MDN legacy samples [analysis](https://github.com/mozmar/infra/issues/197)
- Thoughts on [a simple EFS backup strategy](https://github.com/mozmar/infra/issues/194).
- Thoughts on [an EFS replication strategy](https://github.com/mozmar/infra/issues/189).
- WIP using [EFS in persistent development environment](https://github.com/mozmar/infra/issues/134)
	
### New Relic Synthetics CLI tools

[Giorgos](https://github.com/glogiotatidis) is working on an unofficial New Relic Synthetics CLI tool:

"NeReS is a cli tool to manage NewRelic Synthetics monitors with a Synthetics Lite account (Pro should work too). The tool emulates the actions of a user in the browser and doesn't use the Synthetics API since that's only available to the Pro accounts."

The project lives [on Github](https://github.com/glogiotatidis/neres/).

## Future work

### Decommission webwewant.mozilla.org

[We'll be decommissioning](https://github.com/mozmar/infra/issues/202) webwewant.mozilla.org. A webops bug has been filed to redirect webwewant requests to mozilla.org.

### Decommission openwebdevice.org?

Looking into possibility of shutting down this site. Waiting for some internal communications before moving forward.

### Nucleus

We're planning to move nucleus to Kubernetes, and then proceed to decommissioning current nucleus infra.

### Basket

We're planning to move basket to Kubernetes shortly after the nucleus migration, and then proceed to decommissioning existing infra.

### Snippets

Status unchanged since last week. [Giorgos](https://github.com/glogiotatidis/) is looking at snippets-stats to see if it's behaving correctly. The snippets-stats Route53 routing policy currently points at the Deis 1 deployment due to low stats alerts in new K8s environment.

### New Kubernetes cluster

We'll be creating a new Kubernetes cluster in Portland so we can take advantage of EFS to support MDN in that region. We currently run many of our services from Portland, Virginia, and Ireland. The new cluster will be created in an entirely new VPC, and existing resources will not be shared.

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
