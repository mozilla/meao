---
layout: post
title: MozMEAO SRE Status Report - 5/23/2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from May 17th - May 23rd.

<!--more-->

## Current work

### Bedrock (mozilla.org)

Bedrock has been deployed to our Virginia Kubernetes cluster, with our Tokyo cluster closely following shortly later today or Wednesday.

##### Production deployment

- Gunicorn was upgraded and [the Meinheld worker](	https://github.com/mozilla/bedrock/pull/4845) is now used to help prevent timeouts.
	- Meinheld helped to resolve timeout issues in the [snippets](https://github.com/mozmar/snippets-service/) app as well.
	- Thanks to [pmac](https://github.com/pmac) for the assistance!
- We've [cleaned up](https://github.com/mozmar/infra/issues/254) some Bedrock DNS entries
- Some [decom work on unused Bedrock prod/stage ELBs](https://github.com/mozmar/infra/issues/255) was performed.
- [ELB certificates and DNS entries were created](https://github.com/mozmar/infra/issues/178) as part of the move to K8s.
- App limits and requests set: Dev, stage and production environment [limits and requests](https://kubernetes.io/docs/tasks/administer-cluster/cpu-memory-limit/) [have been set](https://github.com/mozmar/infra/issues/258) in Kubernetes in preparation for the production push. This allows Bedrock to take advantage of cluster and pod autoscaling, which is documented [here](https://github.com/mozmar/infra/blob/master/docs/k8s_autoscaling.md).
	- Since we've added K8s to the www.mozilla.org Route 53 Traffic Policy, we've had to [fine tune the memory and cpu limits](https://github.com/mozmar/infra/issues/258#issuecomment-303467009) for better performance.


### MDN

- [Multi-region EFS replication](https://github.com/mozmar/infra/issues/237) progress is in this WIP [branch](https://github.com/mozmar/infra/compare/dp_efs_backup_and_sync).
	- the work in this branch will also be used in [MySQL backup solution for AWS hosted MDN](https://github.com/mozmar/infra/issues/198).
- The last remaining Apache rewrites [have been implemented](https://github.com/mozilla/kuma/pull/4231) in Django.
- More work is needed to ensure the [mime types](https://github.com/mozmar/infra/issues/244) are correct and consistent in Django. 
- [httpd Alias directives](https://github.com/mozmar/infra/issues/241) need to be implemented in Django.

##### MDN migration analysis summary

- [File storage](https://github.com/mozmar/infra/issues/183)
	- store all additional media ([including samples](https://github.com/mozmar/infra/issues/197)) on EFS.
- [Serving HTTP](https://github.com/mozmar/infra/issues/180)
	- Django hosts everything, completely removing httpd.
- [Database](https://github.com/mozmar/infra/issues/121)
	- We're sticking with self-hosted MySQL running per-region in Kubernetes.
	- We'll need [a custom backup solution](https://github.com/mozmar/infra/issues/198)
- [Elasticsearch](https://github.com/mozmar/infra/issues/193).
	- (waiting for [confirmation](https://github.com/mozmar/infra/issues/193#issuecomment-301583226)) for the initial migration, use AWS hosted ES, keeping in mind that we can always self-host.


## Future work

### Decommission openwebdevice.org

Waiting for some [internal communications](https://github.com/mozmar/infra/issues/205) before moving forward.

### Nucleus

We're planning to move nucleus to Kubernetes, and then proceed to decommissioning current nucleus infra.

### Basket

We're planning to move basket to Kubernetes shortly after the nucleus migration, and then proceed to decommissioning existing infra.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)