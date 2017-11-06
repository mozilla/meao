---
layout: post
title: Kuma Report, October 2017
author: John Whitlock
excerpt_separator: <!--more-->
---

Here's what happened in October in
[Kuma](https://github.com/mozilla/kuma),
the engine of
[MDN](https://developer.mozilla.org):

- MDN Migrated to AWS
- Continued Migration of Browser Compatibility Data
- Shipped tweaks and fixes

Here's the plan for November:

- Ship New Compat Table to Beta Users
- Improve Performance of MDN and the Interactive Editor
- Update Localization of KumaScript Macros

I've also included an 
[overview of the AWS migration project](#aws-intro), and an
[introduction to our new AWS infrastructure in Kubernetes](#k8s-intro),
which helps make this the longest Kuma Report yet.

<!--more-->

Done in October
===

MDN Migrated to AWS
---
On October 10, we moved MDN from Mozilla's SCL3 datacenter to a
[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) cluster in
the AWS ``us-west2`` (Oregon) region. The database move went well, but we
needed five times the web resources as the maintenance mode tests. We were
able to smoothly scale up in the four hours we budgeted for the
migration.
[Dave Parfitt](https://github.com/metadave) and
[Ryan Johnson](https://github.com/escattone) did a great job implementing
a flexible set of deployment tools and monitors, that allowed us to quickly
react to and handle the unexpected load.

The extra load was caused by mdn.mozillademos.org, which serves
[user uploads](https://mdn.mozillademos.org/files/12984/web-font-example.png) and
[wiki-based code samples](https://mdn.mozillademos.org/en-US/docs/Learn/CSS/Styling_text/Fundamentals$samples/Color).
These untrusted resources are served from a different domain so that browsers
will protect MDN users from the worst security issues. I excluded these
resources from the production traffic tests, which turned out to be a mistake,
since they represent 75% of the web traffic load after the move.

Ryan and I worked to get this domain behind a CDN. This included avoiding a
``Vary: Cookie`` header that was being added to all responses
([PR 4469](https://github.com/mozilla/kuma/pull/4469)), and adding
caching headers to each endpoint
([PR 4462](https://github.com/mozilla/kuma/pull/4462) and
 [PR 4476](https://github.com/mozilla/kuma/pull/4476)).

We added [CloudFront](https://aws.amazon.com/cloudfront/)
to the domain on October 26. Now most of these resources are served from
the CloudFront CDN, which is fast and often closer to the MDN user (for
example, served to French users from a server in Europe rather than
California).  Over a week, 197 GB was served from the CDN, versus 3 GB (1.5%)
served from Kuma.

![Bytes to User]({{ site.baseurl }}/public/images/kuma/2017-10-cdn-bytes-to-users.png
                 "Untrusted domain: 197 GB (98% of bytes) from CDN")

There is a reduced load on Kuma as well. The CDN can handle many requests, so
Kuma doesn't see them at all. The CDN periodically checks with Kuma that content
hasn't changed, which often requires a short ``304 Not Modified`` rather than
the full response.

Backend requests for attachments have dropped by 45%:

![Attachment Throughput]({{ site.baseurl }}/public/images/kuma/2017-10-attachment-throughput.png
                         "Weekly throughput drop for attachments from 599 to 330 requests per minute")

Code samples requests have dropped by 96%:
![Code Sample Throughput]({{ site.baseurl }}/public/images/kuma/2017-10-code-sample-throughput.png
                          "Weekly throughput drop for code samples from 390 to 16 requests per minute")

We continue to use a CDN for our static assets, but not for
developer.mozilla.org itself. We'd have to do similar work to add caching
headers, ideally splitting anonymous content from logged-in content. The
untrusted domain had 4 endpoints to consider, while developer.mozilla.org
has 35 to 50. We hope to do this work in 2018.

Continued Migration of Browser Compatibility Data
---
The [Browser Compatibility Data](https://github.com/mdn/browser-compat-data/)
project was the most active MDN project in October.  Another 700 MDN pages use
the BCD data, bringing us up to 2200 MDN pages, or 35.5% of the pages with
compatibility data.

[Daniel D. Beck](https://github.com/ddbeck) continues migrating the CSS data,
which will take at least the rest of 2017.
[wbamberg](https://github.com/wbamberg) continues to update WebExtension and
API data, which needs to keep up with browser releases.
[Chris Mills](https://github.com/chrisdavidmills) migrated the Web Audio data
with 32 PRs, starting with
[PR 433](https://github.com/mdn/browser-compat-data/pull/433). This data
includes mixin interfaces, and prompted some discussion about how to
represent them in BCD in
[issue #472](https://github.com/mdn/browser-compat-data/issues/472).

[Florian Scholz](https://github.com/Elchi3) added MDN URLs in
[PR 344](https://github.com/mdn/browser-compat-data/pull/344), which will help
BCD integrators to link back to MDN for more detailed information.

Browser names and versions are an important part of the compatibility data, and
Florian and [Jean-Yves Perrier](https://github.com/teoli2003) worked to
formalize their representation in BCD. This includes standardization of
the first version, preferring "33" to "33.0"
([PR 447](https://github.com/mdn/browser-compat-data/pull/447) and more),
and fixing some invalid version numbers
([PR 449](https://github.com/mdn/browser-compat-data/pull/449) and more).
In November, BCD will add more of this data, allowing automated validation
of version data, and enabling some alternate ways to present compat data.

Florian continues to release a new NPM package each Monday, and
enabled tag-based releases
([PR 565](https://github.com/mdn/browser-compat-data/pull/565))
for the most recent 0.0.12 release.
[mdn-browser-compat-data](https://www.npmjs.com/package/mdn-browser-compat-data)
had over 900 downloads last month.

Shipped Tweaks and Fixes
---
There were 276 PRs merged in August:

- [131 mdn/browser-compat-data PRs](https://github.com/mdn/browser-compat-data/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"&utf8=✓)
- [42 mozilla/kuma PRs](https://github.com/mozilla/kuma/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"&utf8=✓)
- [35 mdn/kumascript PRs](https://github.com/mdn/kumascript/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"&utf8=✓)
- [32 mozmeao/infra PRs](https://github.com/mozmeao/infra/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"+label:MDN&utf8=✓)
- [23 mdn/data PRs](https://github.com/mdn/data/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"&utf8=✓)
- [13 mdn/interactive-examples PRs](https://github.com/mdn/interactive-examples/pulls?page=1&q=is:pr+is:closed+merged:"2017-10-01..2017-10-31"&utf8=✓)

Many of these were from external contributors, including several first-time
contributions. Here are some of the highlights:

- Edge doesn't support `isIntersecting`
  ([BCD PR 430](https://github.com/mdn/browser-compat-data/pull/430)),
  from first-time contributor
  [Ivan Čurić](https://github.com/ivancuric).
- Add the PointerEvent api
  ([BCD PR 484](https://github.com/mdn/browser-compat-data/pull/484)),
  from first-time contributor
  [lpd-au](https://github.com/lpd-au).
- Split WebExt JSONs
  ([BCD PR 488](https://github.com/mdn/browser-compat-data/pull/488)),
  from
  [wbamberg](https://github.com/wbamberg).
- PointerEvents: Remove parentheses and add mdn_urls
  ([BCD PR 491](https://github.com/mdn/browser-compat-data/pull/491),
   [issue #490](https://github.com/mdn/browser-compat-data/issues/490)),
  first of 3 PRs from first-time BCD contributor
  [Maton Anthony](https://github.com/MatonAnthony).
- Change in `frame-ancestors` support
  ([BCD PR 505](https://github.com/mdn/browser-compat-data/pull/505),
  [Bug 1380755](https://bugzilla.mozilla.org/show_bug.cgi?id=1380755)),
  from first-time contributor
  [Jason Tarka](https://github.com/JasonTarka).
- Update let keyword notes
  ([BCD PR 517](https://github.com/mdn/browser-compat-data/pull/517)),
  from first-time BCD contributor
  [jsx](https://github.com/riverspirit).
- Update regex anchored sticky flag compatibility
  ([BCD PR 561](https://github.com/mdn/browser-compat-data/pull/561)),
  from first-time contributor
  [John Lenz](https://github.com/concavelenz).
- Update IE and Edge version compatibility for the button form attribute
  ([BCD PR 566](https://github.com/mdn/browser-compat-data/pull/566)),
  from first-time contributor
  [cb-josh-c](https://github.com/cb-josh-c).
- Add dns-prefetch, preconnect for editor iframe
  ([Kuma PR 4455](https://github.com/mozilla/kuma/pull/4455),
  [issue #238](https://github.com/mdn/interactive-examples/pull/283)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).
- Switch [docs](https://kuma.readthedocs.io/en/latest/) to alabaster theme
  ([Kuma PR 4457](https://github.com/mozilla/kuma/pull/4457)),
  from
  [John Whitlock](https://github.com/jwhitlock).
- Reduce padding and change bgcolor on inline code
  ([Kuma PR 4471](https://github.com/mozilla/kuma/pull/4471)),
  from
  [Stephanie Hobson](https://github.com/stephaniehobson).
- Prevent ISE when no file in cleaned data
  ([Kuma PR 4475](https://github.com/mozilla/kuma/pull/4475),
  [bug 1410559](https://bugzilla.mozilla.org/show_bug.cgi?id=1410559)),
  from
  [Ryan Johnson](https://github.com/escattone).
- Fix lazy loading fonts
  ([Kuma PR 4482](https://github.com/mozilla/kuma/pull/4482),
  [bug 1150118](https://bugzilla.mozilla.org/show_bug.cgi?id=1150118)),
  from
  [Stephanie Hobson](https://github.com/stephaniehobson).
- Delete CSSDataTypes.ejs
  ([KumaScript PR 337](https://github.com/mdn/kumascript/pull/337)),
  from
  [mfluehr](https://github.com/mfluehr).
- Typo in GamepadEventProperties.ejs
  ([KumaScript PR 341](https://github.com/mdn/kumascript/pull/341)),
  from first-time contributor
  [즈눅](https://github.com/xnuk).
- Add missing written articles to LearnSidebar (Client-side Web APIs)
  ([KumaScript PR 347](https://github.com/mdn/kumascript/pull/347)),
  from first-time KS contributor
  [Jean-Yves Perrier](https://github.com/teoli2003).
- Add translations for French (fr) locale
  ([KumaScript PR 353](https://github.com/mdn/kumascript/pull/353)),
  from first-time contributor
  [Kévin C](https://github.com/zecakeh).
- Added some Spanish translations
  ([KumaScript PR 376](https://github.com/mdn/kumascript/pull/376)),
  from first-time contributor
  [Juan Ferrer Toribio](https://github.com/juan-ferrer-toribio).
- Datadog implementation for MDN Redis monitoring
  ([Infra PR 561](https://github.com/mozmeao/infra/pull/561)),
  from
  [Dave Parfitt](https://github.com/metadave).
- Production configs for go-live day
  ([Infra PR 565](https://github.com/mozmeao/infra/pull/565)),
  from
  [Ryan Johnson](https://github.com/escattone).
- MDN MM Frankfurt support
  ([Infra PR 606](https://github.com/mozmeao/infra/pull/606)),
  from
  [Dave Parfitt](https://github.com/metadave).
- Add k8s job for doing MDN database migrations
  ([Infra PR 610](https://github.com/mozmeao/infra/pull/610)),
  from
  [Ryan Johnson](https://github.com/escattone).
- Change MDN CDN origin to developer.mozilla.org
  ([Infra PR 624](https://github.com/mozmeao/infra/pull/624)),
  from
  [Dave Parfitt](https://github.com/metadave).
- Add futuristic ASCII art diagram for MDN DNS
  ([Infra PR 628](https://github.com/mozmeao/infra/pull/628)),
  from
  [Dave Parfitt](https://github.com/metadave).
- Update Fragmentation-related properties
  ([Data PR 111](https://github.com/mdn/data/pull/111)),
  first of 15 Data PRs from
  [mfluehr](https://github.com/mfluehr).
- Add inheritance file (from ``{{ '{{' }}InterfaceData}}``) and its schema
  ([Data PR 122](https://github.com/mdn/data/pull/122)),
  from first-time Data contributor
  [Jean-Yves Perrier](https://github.com/teoli2003).
- Add font-variation-settings descriptor to @font-face
  ([Data PR 125](https://github.com/mdn/data/pull/125)),
  from first-time Data contributor
  [jsx](https://github.com/riverspirit).
- Fix broken reference to units.md
  ([Data PR 137](https://github.com/mdn/data/pull/137)),
  from first-time contributor
  [Jonathan Neal](https://github.com/jonathantneal).
- Copy edit of the readme file
  ([Interactive Examples PR 297](https://github.com/mdn/interactive-examples/pull/297)),
  from first-time Interactive Examples contributor
  [Chris Mills](https://github.com/chrisdavidmills).
- Further performance improvements, and adds Jest for testing
  ([Interactive Examples PR 317](https://github.com/mdn/interactive-examples/pull/317)),
  from
  [Schalk Neethling](https://github.com/schalkneethling).

Planned for November
===

Ship New Compat Table to Beta Users
---
[Stephanie Hobson](https://github.com/stephaniehobson) and Florian are
collaborating on a
[new compat table design](http://stephaniehobson.github.io/browsercompat/5.0/#here)
for MDN, based on the BCD data.
The new format summarizes support across desktop and mobile browsers, while
still allowing developers to dive into the implementation details. We'll ship
this to beta users on 2200 MDN pages in November.

![New Compat Table]({{ site.baseurl }}/public/images/kuma/2017-10-BCD-table.png)


Improve Performance of MDN and the Interactive Editor
---
Page load times have increased with the move to AWS.  We're looking into ways
to increase performance across MDN. You can follow our
[MDN Post-migration project](https://github.com/mozmeao/infra/projects/5)
for more details.
We also want to enable the
[interactive editor](https://discourse.mozilla.org/t/interactive-editors-in-beta/18548)
for all users, but we're concerned about further increasing page load times. You can
follow the remaining issues in the
[interactive-examples repo](https://github.com/mdn/interactive-examples/issues).

Update Localization of KumaScript Macros
---
In August, we planned the toolkit we'd use to extract strings from
KumaScript macros (see
[bug 1340342](https://bugzilla.mozilla.org/show_bug.cgi?id=1340342#c4)).
We put implementation on hold until after the AWS migration. In November,
we'll dust off the plans and get some sample macros converted. We're hopeful
the community will make short work of the rest of the macros.

<a name="aws-intro"></a>MDN in AWS
===
The AWS migration project started in
[November 2014](https://public.etherpad-mozilla.org/p/r.c171c5789092370bcb021ccd7e320375),
[bug 1110799](https://bugzilla.mozilla.org/show_bug.cgi?id=1110799).
The original plan was to switch by summer 2015, but the technical and
organizational hurdles proved harder than expected. At the same time, the team
removed many legacy barriers making Kuma hard to migrate. A highlight of the
effort was the Mozilla All Hands in December 2015, where the team merged
[several branches of work-in-progress code](https://github.com/mozilla/kuma/compare/mozlando)
to get Kuma running in [Heroku](https://en.wikipedia.org/wiki/Heroku).
Thanks to
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
and everyone else who worked on or influenced this first phase of the project.

The migration project
[rebooted in Summer 2016](https://docs.google.com/document/d/1q0rNBieya_9NPqjWYX93_QwEge-K2wqLPPvdtZGyinE).
We switched to targeting Mozilla Marketing's deployment environment. I split
the work was split into smaller steps leading up to AWS.  I thought each step
would take about a month. They took about 3 months each. Estimating is hard.

![2016 MDN Tech Plan]({{ site.baseurl }}/public/images/kuma/2017-10-MDN-Tech-Plan-2016.svg)

Changes to MDN Services
---
MDN no longer uses Apache to serve files and proxy Kuma.
Instead, Kuma serves requests directly with
[gunicorn](https://en.wikipedia.org/wiki/Gunicorn) with the
[meinheld](http://meinheld.org/) worker. I did
[some analysis](https://docs.google.com/document/d/1-s343yxBMiugPQm5w2ho7EcSAcaLU4uOF6p2MLgbS1I/edit#heading=h.7ffa1k4x57xe)
in January, and
[Dave Parfitt](https://github.com/metadave) and
[Ryan Johnson](https://github.com/escattone) led the effort to port Apache
features to Kuma:

* Redirects are implemented with
  [Paul McLanahan](https://github.com/pmac)'s
  [django-redirect-urls](https://github.com/pmac/django-redirect-urls).
* Static assets (CSS, JavaScript, etc.) are served directly with
  [WhiteNoise](http://whitenoise.evans.io/en/stable/).
* Kuma handles the domain-based differences between the main website
  and the untrusted domain.
* Miscellaneous files like robots.txt, sitemaps, and legacy files (from the
  early days of MDN) are served directly.
* Kuma adds security headers to responses.

Another big change is how the services are run. The base unit of implementation
in SCL3 was multi-purpose virtual machines (VMs). In AWS, we are switching to
application-specific [Docker](https://en.wikipedia.org/wiki/Docker_(software))
containers.

In SCL3, the VMs were split into 6 user-facing web servers and 4 backend
[Celery](https://en.wikipedia.org/wiki/Celery_(software)) servers.
In AWS, the EC2 servers act as Docker hosts. Docker uses
[operating system virtualization](https://en.wikipedia.org/wiki/Operating-system-level_virtualization),
which has several advantages over machine virtualization for our use cases.
The Docker images are distributed over the EC2 servers, as chosen by Kubernetes.

![SCL3 versus AWS Servers]({{ site.baseurl }}/public/images/kuma/2017-10-scl3-vs-aws-servers.svg)

The SCL3 servers were maintained as long-running servers, using
[Puppet](https://en.wikipedia.org/wiki/Puppet_(software)) to install
security updates and new software. The servers were multi-purpose, used
for Kuma, KumaScript, and backend Celery processes. With Docker, we
instead use a Python/Kuma image and a
[node.js](https://en.wikipedia.org/wiki/Node.js)/KumaScript image to
implement MDN.

![SCL3 versus AWS MDN units]({{ site.baseurl }}/public/images/kuma/2017-10-scl3-vs-aws-units.svg)

The Python/Kuma image is configurable through
[environment variables](https://12factor.net/config) to run in different
domains (such as staging or production), and to be configured as one of our
three main Python services:

* **web** - User-facing Kuma service
* **celery** - Backend Kuma processes outside of the request loop
* **api** - A backend Kuma service, used by KumaScript to render pages. This
  avoids an issue in SCL3 where KumaScript API calls were competing with MDN
  user requests.

Our node.js/KumaScript service is also configured via environment variables,
and implements the fourth main service of MDN:
* **kumascript** - The [node.js](https://en.wikipedia.org/wiki/Node.js)
  service that renders wiki pages

Building the Docker images involves installing system software, installing the
latest code, creating the static files, compiling translations, and preparing
other run-time assets. AWS deployments are the relatively fast process of
switching to newer Docker images. This is an improvement over SCL3, which
required doing most of the work during deployment while developers watched.

<a name="k8s-intro"></a>An Introduction to Kubernetes
---
[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)
is a system for automating the deployment, scaling, and management of
containerized applications.  Kubernetes's view of MDN looks like this:

![AWS MDN from Kubernetes' Perspective]({{ site.baseurl }}/public/images/kuma/2017-10-aws-k8s.svg)

A big part of understanding Kubernetes is learning the vocabulary.
[Kubernetes Concepts](https://kubernetes.io/docs/concepts/) is a good place
to start. Here's how some of these concepts are implemented for MDN:

* Ten EC2 instances in AWS are configured as
  **[Nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)**, and
  joined into a Kubernetes **Cluster**. Our "Portland Cluster" is in the
  ``us-west2`` (Oregon) AWS region. Nine Nodes are available for application
  usage, and the master Node runs the Cluster.
* The ``mdn-prod``
  **[Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)**
  collects the resources that need to collaborate to make MDN work. The
  ``mdn-stage`` Namespace is also in the Portland Cluster, as well as other
  Mozilla projects.
* A **[Service](https://kubernetes.io/docs/concepts/services-networking/service/)**
  defines a service provided by an application at a TCP port. For example,
  a webserver provides an HTTP service on port 80.
  * The ``web`` service is connected to the outside world via an AWS
    Elastic Load Balancer (ELB), which can reach it at
    https://developer.mozilla.org (the main site) and
    https://mdn.mozillademos.org (the untrusted resources).
  * The ``api`` and ``kumascript`` services are available inside the cluster,
    but not routed to the outside world.
  * ``celery`` doesn't accept HTTP requests, and so it doesn't get a Service.
* The application that provides a service is defined by a
  **[Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#writing-a-deployment-spec)**,
  which declares what Docker image and tag will be used, how many replicas are
  desired, the CPU and memory budget, what disk volumes should be mounted, and
  what the environment configuration should be.
* A Kubernetes Deployment is a higher-level object, implemented with a
  **[ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)**,
  which then starts up several
  **[Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/)**
  to meet the demands. ReplicaSets are named after the Service plus a random
  number, such as ``web-61720``, and the Pods are named after the ReplicaSets
  plus a random string, like ``web-61720-s7l``.

ReplicaSets and Pods come into play when new software is rolled out.  The
Deployment creates a new ReplicaSet for the desired state, and creates new Pods
to implement it, while it destroys the Pods in the old ReplicaSet.  This
rolling deployment ensures that the application is fully available while new
code and configurations are deployed. If something is wrong with the new code
that makes the application crash immediately, the deployment is cancelled.  If
it goes well, the old ReplicaSet is kept around, making it easier to rollback
for subtler bugs.

![Kubernetes Rolling Deployment]({{ site.baseurl }}/public/images/kuma/2017-10-k8s-deployment.svg)

This deployment style puts the burden on the developer to ensure that the two
versions can run at the same time. Caution is needed around database changes
and some interface changes. In exchange, deployments are smooth and safe with no
downtime. Most of the setup work is done when the Docker images are created,
so deployments take about a minute from start to finish.

Kubernetes takes control of deploying the application and ensures it keeps
running. It allocates Pods to Nodes (called **Scheduling**), based on the CPU
and memory budget for the Pod, and the existing load on each Node. If a Pod
terminates, due to an error or other cause, it will be restarted or recreated.
If a Node fails, replacement Pods will be created on surviving Nodes.

The Kubernetes system allows several ways to scale the application. We used
some for handling the unexpected load of the user attachments:

* We went from 10 to 12 Nodes, to increase the total capacity of the Cluster,
  then back down again when we got things under control.
* We scaled the ``web`` Deployment from 6 to 20 Pods, to handle more
  simultaneous connections, including the slow file requests.
* We scaled the ``celery`` Deployment from 6 to 10 Pods, to handle the load of
  populating the cold cache.
* We adjusted the ``gunicorn`` worker threads from 4 to 8, to increase
  the simultaneous connections
* We rolled out new code to improve caching

There are many more details, which you can explore by reading our
[configuration files](https://github.com/mozmeao/infra/tree/master/apps/mdn/mdn-aws/k8s)
in the [infra repo](https://github.com/mozmeao/infra). We use
[Jinja](http://jinja.pocoo.org/) for our templates, which we find more
readable than the [Go templates](https://golang.org/pkg/text/template/)
used by many Kubernetes projects. We'll continue to refine these as we
adjust and improve our infrastructure. You can see our current tasks by
following the
[MDN Post-migration project](https://github.com/mozmeao/infra/projects/5).
