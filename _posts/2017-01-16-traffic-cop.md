---
layout: post
title: Traffic Cop - Simple & lightweight A/B testing
author: Jon Petto
---

We [recently added](https://github.com/mozilla/bedrock/pull/4361) a home-grown A/B testing framework to bedrock, the codebase powering [mozilla.org](https://www.mozilla.org). We named it Traffic Cop, as most of our content experiments simply redirect users to a different URL.

## Why did we build it?

Prior to Traffic Cop, we were using [Optimizely](https://www.optimizely.com/) to handle both visitor redirection and content changes. While Optimizely has been functionally sound, there are a number of downsides that we've been grumbling about for some time:

1. **Security** — Optimizely is a potential [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting) vector. This has nothing to do with Optimizely per se - any JavaScript loaded from a third-party presents this risk. Anything that increases the chances of a user downloading a compromised build of Firefox is something we want to avoid.
2. **Performance** — To avoid content flicker, any JavaScript performing redirects should be loaded in the `<head>` of the document. All users are forced to download this render-blocking JavaScript payload (even those not chosen for the experiment), so it makes sense to keep it as small as possible. In addition to loading code for *all* running experiments (not just those targeting the current page), Optimizely also bundles a separate build of jQuery <sup>[1](#trafficcop-footnote1)</sup>. As you might guess, this results in a rather large JavaScript bundle. (Around **200KB** at last check.)
3. **Code Quality** — Optimizely code must be written and reviewed within a textarea on a web page, making for more error-prone development and time-consuming code review.
4. **Cost** — Optimizely is a paid service. We're not crying poor here, but perhaps that money can be better spent [elsewhere](https://www.mozilla.org/internet-health/).

Have we cancelled our Optimizely account? No. Not all of our experiments are of the simple "redirect a visitor" variety. Optimizely is still providing some value for us, but we try to make sure all experiments that *can* use Traffic Cop do.

## How does it work?

A visitor hits a URL running an experiment, e.g. `https://www.mozilla.org/en-US/internet-health/`. Traffic Cop picks a random number, and, if that random number falls within the range specified by a variation, redirects the visitor to that variation, e.g. `https://www.mozilla.org/en-US/internet-health/?v=2`.

Traffic Cop assumes all variations are loaded through a querystring parameter appended to the original URL. This keeps things simple, as no new URL patterns need to be defined (and later removed) for each experiment. We simply check for the querystring parameter (either in the view or in the template <sup>[2](#trafficcop-footnote2)</sup>) and load different content accordingly. An added benefit of this approach is that we are free to make content changes in separate HTML, CSS, and JavaScript files, whereas Optimizely operates only via JavaScript DOM manipulation.

Implementing Traffic Cop requires two <sup>[3](#trafficcop-footnote2)</sup> other JavaScript files: one to configure the experiment, and [MDN’s handy cookie framework](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie/Simple_document.cookie_framework). The configuration file is fairly straightforward. Simply instantiate a new Traffic Cop with your experiment configuration, and then initialize it.

```javascript
// this is an example of a configuration file
// assume Traffic Cop & the MDN cookie helper scripts are already loaded
var wiggum = new Mozilla.TrafficCop({
  id: 'experiment-home-page-hero-image-fall-2016',
  variations: {
    'v=1': 20,
    'v=2': 30
  }
});

wiggum.init();
```

In the above example, the `id` parameter is the unique identifier placed in a cookie to determine if a user has already been chosen for a specific variation. The variations object has keys that correspond with the intended querystring value, and values that map to a percent chance of that variation being chosen. For example, a visitor would have a 30% chance of being redirected to `{currentURL}?v=2`.

[Read the docs](http://bedrock.readthedocs.io/en/latest/mozilla-traffic-cop.html#mozillatrafficcop) to see examples and get more technical details.

In summary, Traffic Cop allows us to write code in a text editor, review code in a pull request, and avoid heavy and potentially insecure third-party JavaScrit code injection for free.

<br><br>

<a name="trafficcop-footnote1">1</a>: This is technically avoidable by loading our version of jQuery in the head of all pages, but that would result in worse performance site-wide.

<a name="trafficcop-footnote2">2</a>: [pmac](https://github.com/pmac) wrote a really handy [mixin and view](https://github.com/mozilla/bedrock/commit/71d528ea36bd58017da15143d318c173e61c53b1#diff-529dc1131d3cef60d7b817029d3314b3) to make working with Traffic Cop even easier.

<a name="trafficcop-footnote3">3</a>: Okay, yes, you looked at [the source](https://github.com/mozilla/bedrock/blob/master/media/js/base/mozilla-traffic-cop.js#L76) and saw Traffic Cop looks for a globally scoped function by the name of `_dntEnabled`. Guilty. However, Traffic Cop carries on just fine if `_dntEnabled` doesn’t exist, so simmer down. As you’ve probably already guessed, [`_dntEnabled` is a function that checks the doNotTrack status of the visitor’s browser](https://github.com/mozilla/bedrock/blob/2fb16c05fbb847b57e0fbbea8a5b51d51d554e43/media/js/base/dnt-helper.js). Be a conscientious developer and respect this setting for your visitors as well.
