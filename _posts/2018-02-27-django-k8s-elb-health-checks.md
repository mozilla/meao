---
layout: post
title: Django, K8s, and ELB Health checks
author: Paul McLanahan
excerpt_separator: <!--more-->
---

As you may have seen in several of our
[SRE](https://mozilla.github.io/meao/2018/02/16/sre-status/)
[status](https://mozilla.github.io/meao/2018/01/23/sre-status/)
[reports](https://mozilla.github.io/meao/2017/12/05/sre-status/),
we're moving all of our webapp hosting from [Deis][] to [Kubernetes][] (k8s). As part of that
we've also been doing some additional thinking about the security of our deployments.
One thing we've not done as good a job as we should is with [Django's `ALLOWED_HOSTS` setting][].
We should have been adding all possible hosts to that list, but it seems we used to occasionally
leave it set to `['*']`. This isn't great, but also isn't the end-of-the-world since
we don't knowingly construct URLs using the info sent via the `Host` header. In an effort
to cover all bases we've decided to improve this. Unfortunately our particular combination
of technologies doesn't make this as
[easy as we thought it would](https://github.com/mozmeao/infra/issues/735) (story of our lives).

<!--more-->

## AWS ELB Health Checks

Here's the thing: Amazon Web Services' (AWS) Elastic Load Balancers (ELB) do not have many configuration options for
their health checks. These checks ensure that your app on a particular node in your cluster
is working as expected. If the check fails the ELB will remove the node from the list of nodes
to which it will route requests for your app. However, because it's hitting the nodes directly
it doesn't rely on DNS and directly requests the IP address and port, and it doesn't allow you
to specify custom headers (e.g. the `Host` header). It also can't do HTTPS because we terminate
TLS connections at the ELB, so the app nodes speak only plain HTTP back to the ELB. All of that
means that our health check endpoint needs to do two unique things: allow HTTP connections and
allow the IP address that the ELB requests as a valid `Host` header. The first bit is easy enough
when using Django's in-built `SecurityMiddleware` since it supports the `SECURE_REDIRECT_EXEMPT`
setting. It's this second requirement that gets more interesting when combined with k8s.

## K8s Routing

The way I understand it (and I'm admittedly no expert) is that k8s (at least the way we use it)
sets up a [NodePort][] per app (or namespace). To hit that app you can hit any node in the cluster
at that port and that node will route you to one of the nodes that is running a [pod][]
for that app. The important bit for us is that the node that serves this request is not
necessarily the one that the ELB sent it to. So the `Host` header may contain an IP address for the
node that was initially hit, but not necessarily for the node that serves the request. This means that we can't
simply add the IP of the host to the `ALLOWED_HOSTS` list when the app starts. We could get more info
from [AWS' metadata service][] endpoint, but for security reasons we block that service from all of our
nodes.

So, the approach could then be to simply add all of the IPs for all of the nodes in the cluster to the
`ALLOWED_HOSTS` setting and call it done. The problem with this happens when there is a scaling event.
When a node is killed and a new one started, or the cluster is scaled to include more nodes, you'd need
to have a way to inform every running [pod][] of this change so they could get the new list of IPs. If they
didn't update the list the new node(s) could be immediately excluded from the cluster because health checks would
return 400s since their IP (host) would not be allowed by Django.

## Enter django-allow-cidr

The way we decided to solve this was by implementing a Django middleware that would allow a range of IP
addresses defined by a [CIDR][] (Classless Inter-Domain Routing). We've released this middleware in a
Django package called [django-allow-cidr][]. The way it works is to store the normal hosts you've set
in your `ALLOWED_HOSTS` setting, change that setting to `['*']` in order to bypass Django's default
host header checking in the `HttpRequest.get_host()` method, and do the checking itself.
It does this checking via the [same methods as Django][] would have, but if those methods fail it does
a secondary check using the IP ranges you've defined in an `ALLOWED_CIDR_NETS` setting. It creates
[netaddr.IPNetwork][] instances from the CIDRs in that list and will check any host that isn't valid
based on your original `ALLOWED_HOSTS` setting. Failing both of those checks will result in an
immediate return of a 400 response.

## Conclusion

That was a long way to go to get to some simple health checking, but we believe it was the right move for the
reliability and security of our Django apps hosted in our k8s infrastructure on AWS. Please check out the
[repo for django-allow-cidr][] on Github if you're interested in the code. Our hope is that releasing this as
a general use package will help others that find themselves in our situation, as well as helping ourselves
to do less copypasta coding around our [various](https://www.mozilla.org/) [web](https://developer.mozilla.org)
[projects](https://support.mozilla.org).

[Deis]: https://deis.com/
[Kubernetes]: https://kubernetes.io/
[CIDR]: https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
[django-allow-cidr]: https://pypi.python.org/pypi/django-allow-cidr/
[netaddr.IPNetwork]: https://netaddr.readthedocs.io/en/latest/api.html#ip-networks-and-subnets
[repo for django-allow-cidr]: https://github.com/mozmeao/django-allow-cidr
[Django's `ALLOWED_HOSTS` setting]: https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
[NodePort]: https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport
[AWS' metadata service]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
[pod]: https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/
[same methods as Django]: https://github.com/mozmeao/django-allow-cidr/blob/d36d3e2b772c7bebdb69db98acc323168ea28ded/allow_cidr/middleware.py#L34-L37
