---
layout: post
title: MozMEAO SRE Status Report - 5/16/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from May 9th - May 16th.

<!--more-->

## Current work

### Bedrock (mozilla.org)

Work continues on moving Bedrock to our Kubernetes infrastructure. 

##### Postgres/RDS provisioning

A Postgres RDS instance has already been provisioned in `us-east-1` for our Virginia cluster, and another was [created](https://github.com/mozmar/infra/issues/222) in `ap-northeast-1` to support the Tokyo cluster. Additionally, development, staging, and production databases were [created in each region](https://github.com/mozmar/infra/issues/240). This process was documented [here](https://github.com/mozmar/infra/pull/239).

##### Elastic Load Balancer (ELB) provisioning

We've automated the [creation of ELB's](https://github.com/mozmar/infra/pull/247) for Bedrock in Virginia and Tokyo. There are still a few more wrinkles to sort out, but the infra is mostly in place to begin The Big Move to Kubernetes.

### MDN

Work continues to analyze the Apache httpd configuration from the current SCL3 datacenter config. 

- The last remaining rewrites [have been implemented](https://github.com/mozilla/kuma/pull/4231).
- [John Whitlock](https://github.com/jwhitlock) reviewed [httpd icon configuration](https://github.com/mozmar/infra/issues/243) and [accepted locales](https://github.com/mozmar/infra/issues/242) and determined that no migration is needed.
- More work is needed to ensure that [mime types](https://github.com/mozmar/infra/issues/244) are correct and consistent in Django. 
- [httpd `Alias` directives](https://github.com/mozmar/infra/issues/241) need to be implemented in Django.
- [Ryan Johnson](https://github.com/escattone) has [submitted a PR](https://github.com/mozilla/kuma/pull/4240) for liveness/readiness endpoints.

##### Downtime incident 2017-05-13

On May 13th, 2017 22:49 -22:55, New Relic reported that MDN was unavailable.  The site was slow to respond to page views, and was running long database queries.  Log analysis show a security scan of our database-intensive endpoints. 

On May 14th, 2017, there were high I/O alerts on 3 of the 6 production web servers. This was not reflected in high traffic or a decrease in responsiveness.

The incident report is available [here](https://docs.google.com/document/d/1DtV8DBXZqat0YvnFasOxeOyJZUaOZL40CuuVxTA-bgA/edit#)


### Basket

The FxA team would like to [send events](https://bugzilla.mozilla.org/show_bug.cgi?id=1358123) (FXA_IDs) to Basket and Salesforce, and needed SQS queues in order to move forward. We automated the [provisioning of dev/stage/prod SQS queues](https://github.com/mozmar/infra/issues/208), and passed off credentials to the appropriate engineers.

The [FxA team requested cross AWS account access](https://bugzilla.mozilla.org/show_bug.cgi?id=1358123) to the [new SQS queues](https://github.com/mozmar/infra/issues/208). Access has been automated and granted via [this PR](https://github.com/mozmar/infra/pull/248).


### Snippets

##### Snippets Stats Collection Issues 2017-04-10

A planned configuration change to add a Route 53 Traffic Policy for the snippets stats collection service caused a day’s worth of data to not be collected due to a SSL certificate error.

The incident report is available [here](https://docs.google.com/document/d/1qc0a19Fk1gS6iHAsErkjx4OQ1NHnTkjvuvxCK1vRKtU/edit)

### Careers

##### Autoscaling

In order to take advantage of Kubernetes cluster and pod autoscaling (which we've documented [here](https://github.com/mozmar/infra/blob/master/docs/k8s_autoscaling.md)), app [memory and CPU limits were set](https://github.com/mozmar/infra/issues/165) for careers.mozilla.org in our Virginia and Tokyo clusters. This allows the careers site to scale up and down based on load.

##### Acceptance tests

[Giorgos Logiotatidis](https://github.com/glogiotatidis/) added [acceptance tests](https://github.com/mozmar/lumbergh/pull/195), which contains a simple bash script and additional Jenkinsfile stages to check if careers.mozilla.org pages return valid responses after deployment. 

##### Downtime incident 2017-04-11

A typo was merged and pushed to production and caused a couple of minutes of downtime before we rolled-back to the previous version.

The incident report is available [here](https://goo.gl/Re3vdP)


### Decommission openwebdevice.org status

openwebdevice.org will remain operational in http-only mode until the [board approves decommissioning](https://github.com/mozmar/infra/issues/205#issuecomment-300524422). A timeline is unavailable.

## Future work

### Nucleus

We're planning to move nucleus to Kubernetes, and then proceed to decommissioning current nucleus infra.

### Basket

We're planning to move basket to Kubernetes shortly after the nucleus migration, and then proceed to decommissioning existing infra.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)