---
layout: post
title: MozMEAO SRE Status Report - November 14, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from November 7th - November 14th.

<!--more-->

## Current work

### Firefox Quantum release

The team actively monitored our [bedrock](https://github.com/mozilla/bedrock) Kubernetes deployments during the release of [Firefox Quantum]
(https://www.mozilla.org/en-US/firefox/). No changes or manual intervention was required during the release.

### SRE General

- To step up our efforts on the security front, we've updated all of our application Docker images [to use a few recommended images](https://github.com/mozmeao/infra/issues/641).

### SUMO

- an Elastic.co Elasticsearch development instance has been provisioned and is usable by the SUMO development team.
- [Redis and RDS provisioning automation has been merged](https://github.com/mozmeao/infra/pull/638), but resources have not been provisioned in AWS.
- The team worked on a SUMO infra estimate for AWS. 
    - Assumes existing K8s cluster, possible shared RDS/Elasticache.
  
### MDN 

- [Additional domains have been added to the MDN ELB certificate](https://github.com/mozmeao/infra/issues/644) to support the following legacy domains:
    - developer.mozilla.com
    - devmo.developer.mozilla.org
    - mdn.mozilla.org
    - developer-new.mozilla.org
    - developers.mozilla.org
- [Stalled asset loading leading to high load times](https://github.com/mozmeao/infra/issues/648)
- [Optimize prefetch_related usage in revisions dashboard](https://github.com/mozilla/kuma/pull/4520)

### Static site hostings

The team is in the process of evaluating the following static hosting solutions:

- [S3](https://aws.amazon.com/s3/) + [Cloudfront](https://aws.amazon.com/cloudfront/) (+ [Lambda@Edge](http://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html) for header tweaking)
    - some of our sites, including [IRL](https://irlpodcast.org/) and [Viewsourceconf](https://viewsourceconf.org/london-2017/) already use this set of services from AWS. 
    - we have [experienced some performance degredation issues](https://github.com/mdn/viewsourceconf/issues/198) when switching from nginx/K8s to S3/Cloudfront.

- [Google Firebase hosting](https://firebase.google.com/docs/hosting/)
- [Netlify](https://www.netlify.com/)
- [Nginx](https://www.nginx.com/) containers in Kubernetes

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
