---
layout: post
title: MDN in AWS
author: John Whitlock
---
This week, we moved MDN from the SCL3 datacenter to a
[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) cluster in
the AWS ``us-west2`` (Oregon) region. This has been a huge, 3 year project, and
we're thrilled we've reached this milestone.

This project was started in
[November 2014](https://public.etherpad-mozilla.org/p/r.c171c5789092370bcb021ccd7e320375).
The original plan was to switch by Summer 2015, but the technical and
organizational hurdles proved harder than expected. For me, a highlight of the
effort was the Mozilla All Hands in December 2015, where the team merged
[several branches of work-in-progress code](https://github.com/mozilla/kuma/compare/mozlando)
to get Kuma running in
[Heroku](https://en.wikipedia.org/wiki/Heroku).

I've tried to reconstruct the early days of the project, following the thread
of [bug 1110799](https://bugzilla.mozilla.org/show_bug.cgi?id=1110799), but
there's a lot, and it's complicated. Thanks to
[Jannis Leidel](https://github.com/jezdez),
[Rob Hudson](https://github.com/robhudson),
[Luke Crouch](https://github.com/groovecoder),
[Lonnen](https://github.com/lonnen),
[Will Kahn-Greene](https://github.com/willkg),
[David Walsh](https://github.com/darkwing),
[James Bennet](https://github.com/ubernostrum),
cyliang,
Jake,
Sean Rich,
Travis Blow,
Sheeri Cabral,
and everyone else who worked on or influenced this phase of the project.

# Changes in AWS
MDN users shouldn't notice a difference with the move to AWS. Requests are just
about as fast as they were in SCL3. There was hope that it would be faster, but
SCL3 is fast and Kuma is efficient, so we don't expect a change in performance,
as seen by the MDN user. We'll monitor page speed over the next few months, and
report any interesting data.

The big changes are in the way MDN is implemented. The base unit of
implementation in SCL3 are multi-purpose virtual machines (VMs). In AWS, we
are switching to application-specific
[Docker](https://en.wikipedia.org/wiki/Docker_(software)) containers:

![SCL3 versus AWS MDN units]({{ site.baseurl }}/public/images/kuma/2017-10-scl3-vs-aws-units.svg)

AWS doesn't serve Kuma with Apache, but instead serves requests directly with
[gunicorn](https://en.wikipedia.org/wiki/Gunicorn) and with the
[meinheld](http://meinheld.org/) worker. I did some analysis in January, and
[Dave Parfitt](https://github.com/metadave) and
[Ryan Johnson](https://github.com/escattone) led the effort to port Apache
features to Kuma:

* Redirects, implemented with
  [Paul McLanahan](https://github.com/pmac)'s
  [django-redirect-urls](https://github.com/pmac/django-redirect-urls)
* Serve static assets like CSS and JavaScript with
  [WhiteNoise](http://whitenoise.evans.io/en/stable/)
* Handle the domain-based differences between the main website
  and the untrusted domain for user-uploaded attachments and wiki-editable
  example code.
* Serve mostly-static files like robots.txt and sitemaps
* Serve legacy files from the early days of MDN
* Add security headers

The move to Docker containers has an impact on the server configuration:

![SCL3 versus AWS Servers]({{ site.baseurl }}/public/images/kuma/2017-10-scl3-vs-aws-servers.svg)

In SCL3, the VMs are split into 6 user-facing web servers and 4 backend
[Celery](https://en.wikipedia.org/wiki/Celery_(software)) servers,
maintained as long running servers.
[Puppet](https://en.wikipedia.org/wiki/Puppet_(software)) is used to install
security updates and new software. MDN deployments require re-installing
third-party packages and building the static assets and translation files.
The Apache, KumaScript, and
[Celery](https://en.wikipedia.org/wiki/Celery_(software))
services are shut down, the new software installed, and the services restarted,
in about 1/2 of a second, so that there's no interuption to MDN users.

In AWS, the EC2 servers that act as Docker hosts. Docker uses
[operating system virtualization](https://en.wikipedia.org/wiki/Operating-system-level_virtualization),
which has several advantages over machine virtualization when running many
Linux applications. These two image types implement the four services
of MDN:

* **web** - User-facing Kuma service
* **celery** - Backend Kuma processes outside of the request loop
* **kumascript** - The [node.js](https://en.wikipedia.org/wiki/Node.js)
  service that renders wiki pages
* **api** - A backend Kuma service, used by KumaScript to render pages. This
  avoids an issue in SCL3 where KumaScript API calls were competing with MDN
  user requests.

The allocation of these Docker containers is controlled by
[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes),
a system for automating the deployment, scaling, and management of
containerized applications. The containers, or "pods" in Kubernetes
terminology, get unique names like ``web-61720-ckg``.

Kubernetes's view of MDN looks more like this:

![AWS MDN from Kubernetes' Perspective]({{ site.baseurl }}/public/images/kuma/2017-10-aws-k8s.svg)

Kubernetes takes some study to understand.
[Kubernetes Concepts](https://kubernetes.io/docs/concepts/) is a good place
to start. Here's how some of these concepts are implemented for MDN:

* Nine EC2 instances in AWS are configured as
  **[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)**, and
  joined into a Kubernetes **cluster**. Our cluster is in the Oregon AWS
  region, and we call it the Portland cluster. Eight nodes are available for
  application usage, and the master node runs the cluster.
* The ``mdn-prod``
  **[Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)**
  collects the resources that need to collaborate to make MDN work. The
  ``mdn-stage`` namespace is also in the cluster, as well as other Mozilla
  projects.
* A **[Service](https://kubernetes.io/docs/concepts/services-networking/service/)**
  defines a service provided by an application at a port. For
  a webserver usually provides HTTP on port 80.  The ``web`` service for
  ``mdn-prod`` is connected to the outside world via an AWS
  Elastic Load Balancer (ELB), which can reach it at https://developer.mozilla.org.
  The ``api`` and ``kumascript`` services are available in the cluster, but not
  routed to the outside world. ``celery`` doesn't use HTTP requests to work,
  and doesn't get a Service.
* The application that provides a service is defined by a
  **[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#writing-a-deployment-spec)**,
  which declares what Docker image and tag will be used, how many replicas are
  desired, the CPU and memory budget, what disk volumes should be mounted, and
  what the environment configuration should be.  Kubernetes translates this
  into a
  **[ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)**,
  which then starts up several
  **[Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/)**
  to meet the demands.

It takes some time to translate an application into Kubernetes, but once you
do, it takes on a lot of the burden of deploying and maintaining the
application. It decides which node a pod will be deployed on, based on the CPU
and memory budget, and the load on existing nodes. If a pod terminates, due to
an error or other cause, it will be restarted or recreated. If a node fails,
replacement pods will be created on surviving nodes.

With Kubernetes, we can independently deploy our ``web``, ``api``,
``kumascript``, and ``celery`` deployments.  Kubernetes Deployments handles the
details of deploying new software. It creates a new ReplicaSet to describe the
desired state, and creates new Pods to implement it, while it destroys the Pods
in the old ReplicaSet.

![Kubernetes Rolling Deployment]({{ site.baseurl }}/public/images/kuma/2017-10-k8s-deployment.svg)

(Scaling Opportunities)
