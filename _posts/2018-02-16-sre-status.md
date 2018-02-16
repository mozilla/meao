---
layout: post
title: MozMEAO SRE Status Report - February 16, 2018
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from January 23 - February 16.

<!--more-->

## Current work

### SRE general

#### Load Balancers

- We've tried several methods of automating our AWS Elastic Load Balancers, including [Terraform](https://www.terraform.io/), the [AWS CLI](https://aws.amazon.com/cli/) and [Kubernetes-managed services](https://kubernetes.io/docs/concepts/services-networking/service/). Each method has proven to be quirky and error-prone, so we're trying a [Python-based automation system](https://github.com/mozmeao/infra/pull/714). Additionally, the automation has the ability to [generate code from existing ELBs in a given region](https://github.com/mozmeao/infra/pull/727).

#### Cloudflare to Datadog service

- The Cloudflare to Datadog service [has been converted](https://github.com/mozmeao/cloudflare-datadog/pull/12) to use a non-[helm](https://helm.sh/) based install, and is running in our new Oregon-B cluster.

#### Oregon-A cluster

- We have a new Kubernetes cluster running in the us-west-2 AWS region that will run support.mozilla.org (SUMO) services as well as many of our other services.

### Bedrock

- Bedrock is moving to a ["sqlitened" version](https://github.com/mozilla/bedrock/pull/5334) in our Oregon-B Kubernetes cluster that removes the dependency on an external database.


### MDN

- The cronjob that performs backups on attachments and other static media broke due to a misconfigured `LANG` environment variable. The base image for the cronjob [was updated](https://github.com/mozmeao/infra/pull/711) and [deployed](https://github.com/mozmeao/infra/pull/719). We've also added some cron troubleshooting documentation as part of the same pull request.

- [Safwan Rahman](https://github.com/safwanrahman) submitted [an excellent PR](https://github.com/mozilla/kuma/pull/4630) to optimize Kuma document views 🎉🎉🎉. 

### support.mozilla.org (SUMO)

- SUMO [now uses](https://github.com/mozilla/kitsune/issues/2900) AWS [Simple Email Service (SES)](https://aws.amazon.com/ses/) to send email.
- We're working on establishing a secure link between SCL3 and AWS for MySQL replication, which will help us signficantly reduce the amount of time needed in our migration window.
- SUMO is now using a [CDN](https://github.com/mozmeao/infra/pull/694) to [host static media](https://github.com/mozilla/kitsune/issues/2949#issuecomment-363429101)
- We're working on [Python-based Kubernetes automation](https://github.com/mozilla/kitsune/pull/3034) for SUMO based on the [Invoke library](http://www.pyinvoke.org/). Automation includes web, cron and celery deployments, as well as rollout and rollback functionality.
- Using the Python automation above, SUMO now runs in "vanilla Kubernetes" without [Deis Workflow](https://deis.com/workflow/).
        

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
