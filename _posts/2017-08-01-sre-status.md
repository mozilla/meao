---
layout: post
title: MozMEAO SRE Status Report - August 1, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from July 25th - August 1st.

<!--more-->

## Current work

### MDN Migration

[@metadave](https://github.com/metadave) and [@escattone](https://github.com/escattone) are working on migrating MDN from the SCL3 datacenter to AWS.

- A [new Kubernetes cluster in Portland](https://github.com/mozmeao/infra/issues/366) has been provisioned to support this work.
- [@escattone](https://github.com/escattone) has been [evaluating](https://github.com/mozmeao/infra/issues/359) the MySQL helm chart and [working on automation](https://github.com/mozmeao/infra/pull/377) to install MDN in Kubernetes.

### MDN misc

- MDN interactive examples [can now be hosted in S3/Cloudfront](https://github.com/mozmeao/infra/issues/362). This allows us to deploy interactive examples to an S3 bucket [via Jenkins](https://github.com/mdn/interactive-examples/pull/149), viewable at `interactive-examples.mdn.mozilla.net`.

### Decommissioning the Virginia cluster

The last remaining services running on the Virginia cluster have been moved to other regions or hosting options:

- [Nucleus has been moved to the Frankfurt cluster](https://github.com/mozmeao/infra/issues/363)
- [surveillance.mozilla.org](https://surveillance.mozilla.org) is now [hosted with S3 and Cloudfront](https://github.com/mozmeao/infra/issues/332).
- [viewsourceconf.org](https://viewsourceconf.org) is now [hosted with S3 and Cloudfront](https://github.com/mozmeao/infra/issues/312).

## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
