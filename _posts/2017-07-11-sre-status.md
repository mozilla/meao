---
layout: post
title: MozMEAO SRE Status Report - July 11, 2017
author: Dave Parfitt
excerpt_separator: <!--more-->
---

Here's what happened on the MozMEAO SRE team from July 5th - July 11th.

<!--more-->

This weeks report is brief as the team is returning from the [Mozilla San Francisco All Hands](https://wiki.mozilla.org/All_Hands/SanFrancisco) and vacation.

## Current work

### Static site hosting

- assets.moz.works is [now hosted on S3 and CloudFront](https://github.com/mozmar/infra/pull/330). 
	- we've also used this pattern successfully with [irlpodcast.org](https://irlpodcast.org/) and are planning on doing the same with [viewsourceconf.org](https://viewsourceconf.org/london-2017/) as well.

### Kubernetes

- Our main applications are [being moved](https://github.com/mozmar/infra/issues/301) to our new Frankfurt Kubernetes cluster.


## Links

- [Github project tracking SRE work](https://github.com/mozmar/infra/projects/2)
- [How MozMEAO SRE's work](https://github.com/mozmar/infra/blob/master/docs/how_we_work.md)
- [Weekly SRE meeting notes](https://goo.gl/WuhP0Y)
