---
layout: post
title: Bedrock - from code to production
author: Alex Gibson &amp; Paul McLanahan
---

## Introduction

Bedrock is the code name for the project that runs [www.mozilla.org](https://www.mozilla.org/). It is shiny, awesome, and [open source](https://github.com/mozilla/bedrock/). Mozilla.org is the site where everyone comes to download Firefox, and is also the main public facing web property for Mozilla as an organization. It represents [who we are](https://www.mozilla.org/en-US/about/) and [what we do](https://www.mozilla.org/en-US/mission/).

Bedrock is a large [Django](https://www.djangoproject.com/) app that has many moving parts, with web pages translated into [many](https://www.mozilla.org/de/) [different](https://www.mozilla.org/fr/) [languages](https://www.mozilla.org/es-ES/) ([99 locales](https://github.com/mozilla/bedrock/blob/5ab2a7df5d1d5f03e79c7b04c48b69559edacca4/bedrock/settings/base.py#L129-L141) at time of writing!). This post aims to follow a piece of code through the development lifecycle; from bug, to pull request, to code review, localization, and finally pushed live to production. Hopefully it may prove insightful and give some things to think about when requesting changes or creating new content.

## The change request

All development work should start with [filing a bug](https://bugzilla.mozilla.org/enter_bug.cgi?product=www.mozilla.org&component=Pages%20%26%20Content). [Bugzilla](https://bugzilla.mozilla.org/) is our tool of choice for tracking changes, and links to bugs can be found throughout our [commit history](https://github.com/mozilla/bedrock/commits/master) for reference. This gives us a paper trail for *when and why* changes were made. For a site that has existed over many years, this is *very* useful.

A well written bug should provide a clear summary, and provide as much additional information that may be relevant to resolving the bug. If the bug is reporting an error or mistake on a web page, providing clear *steps to reproduce* is a great start to helping it get fixed quickly. MDN has an excellent set of [guidelines for bug reporting](https://developer.mozilla.org/docs/Mozilla/QA/Bug_writing_guidelines) with a lot more detail.

An example bug summary for creating a new web page might be like so:

```
Please create a new Firefox download page at the following URL:

https://www.mozilla.org/firefox/example-download-page/

Page assets are linked below:
[link to design file]
[link to copy file]

The download page needs to be live in production by: 1 April, 2017.
Locales required for translation on launch: en-US, de, fr, es-ES.
```

If a bug is requesting the creation of new content or updates to existing content, related design and copy assets should be linked directly in the bug. For time sensitive requests, a clear due date should also be provided.

If a change requires localization, it also needs to be clearly stated. Our web pages are translated by teams of volunteers, so adequate time and warning **must be given** if there are hard deadlines involved. We will not show untranslated text to non-English locales on our web pages.

Once a bug has been triaged and contains enough information to act on, it can be assigned to a developer. When a bug has been assigned, any changes or feedback should be added **directly to the bug** (email is a great place for information to get lost).

## Creating a new page

When we're ready to start working on our bug, we first create a new feature branch on the bedrock [GitHub repo](https://github.com/mozilla/bedrock/). This allows us work on the bug in parallel to all the other changes landing in the `master` branch of the the repository. You can learn more about git workflows using [GitHub's introduction guide](https://guides.github.com/introduction/flow/).

Creating a new page on bedrock is pretty simple. All pages are built using the [Jinja](http://jinja.pocoo.org/docs/latest/) template engine, inheriting from a common [base template](https://github.com/mozilla/bedrock/blob/master/bedrock/base/templates/base-pebbles.html). This base template scaffolds out everything we need to start creating a new page. Then it's just a case of adding in content and any additional styling or behavior the page might need.

When we're finished creating our new template and adding in content, our example download page might look something like this:

![Example download page screenshot]({{ site.baseurl }}/public/images/bedrock-code-to-production/example-page-en-us.png)

Because our example page inherits from a common base template it automatically receives the following characteristics:

- [Responsive and *mobile-first*](http://bradfrost.com/blog/web/mobile-first-responsive-web-design/) by default. All pages should be designed with responsiveness in mind. Designs that start with small (mobile) viewports first and then expand up toward desktop sizes work better than the other way around.
- Page component styling using [Pebbles](https://github.com/mozilla/bedrock/tree/master/media/css/pebbles); our own lightweight CSS framework. Pebbles consists of a shared library of styles for common elements that appear throughout the site (e.g. page headers, navigation, footers, email signup forms, download buttons). Working with common design components allows us to create and update pages quickly.
- Pre-built for [localization](http://bedrock.readthedocs.io/en/latest/l10n.html) (l10n). All pages are coded with strings wrapped ready for l10n. This means that copy and visuals should be suitable for different languages and designed to work well with variable length strings.
- Built-in platform detection for Firefox downloads. We go to great lengths to try and make sure users get the correct binary file for their operating system and language when clicking on a download button. All pages get this logic for free should they need it.
- Privacy friendly. We work hard to make sure all our pages respect user privacy as much as possible. We support [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) (DNT), so users with this enabled are not tracked in Google Analytics or entered into [Firefox Desktop Attribution](https://support.mozilla.org/t5/Protect-your-privacy/About-Firefox-Desktop-Attribution/ta-p/1361183). They will also not be entered into A/B experiments using libraries such as [Traffic Cop](http://bedrock.readthedocs.io/en/latest/mozilla-traffic-cop.html).
- Security focused. We enforce an active [Content Security Policy](https://en.wikipedia.org/wiki/Content_Security_Policy) (CSP) that limits the scope of third-party content allowed to run on the site. This aims to protect our users from security attacks and also helps ensure the integrity of Firefox downloads. It is a critical feature for our visitors.
- Built using [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement) and with [accessibility](https://en.wikipedia.org/wiki/Web_accessibility) in mind. User experiences need to work well with keyboard, mouse and touch, and work well with [screen reading software](https://en.wikipedia.org/wiki/Screen_reader). Pages should still function or degrade gracefully even if JavaScript fails, or is disabled by the user.

### A note about browser support

Bedrock currently supports first-class CSS and JavaScript for all major *evergreen* browsers, as well as for Internet Explorer 9 and upward. Internet Explorer 8 and below get a simplified, *universal stylesheet*. This ensures that content is readable and accessible, but nothing more.

Here's how our example download page might look in old browsers:

![Example download page screenshot in Internet Explorer 8]({{ site.baseurl }}/public/images/bedrock-code-to-production/example-page-old-ie.png)

Not much to it right? The key here is that all the page information is still perfectly readable and accessible, meaning the user can still accomplish their goal. By providing a more basic set of styling to older browsers, we are free to use more modern web platform features in order to accomplish more sophisticated designs and experiences.

### Special considerations for download pages

For critical download pages such as our example page, we still need to ensure that users can successfully download Firefox, even in older browsers. When the user clicks the download button, they still need to receive the correct file for their operating system and language.

Because of this added support requirement, download pages may require additional testing and QA. For really high traffic pages such as `/firefox/new/`, we may still make extra effort to provide a higher level of CSS support to older browsers. The pages won't look look exactly the same, but they should still degrade gracefully.

### Localization (l10n)

Many mozilla.org pages are translated into multiple languages. While much of our marketing focus is primarily for English language locales first and foremost, non-English traffic actually makes up around 60% of our overall site traffic. Unless there is a specific request for a page to be in English only, we create all pages assuming they will be translated should our volunteer community wish to do the work.

Here's how our example download page might look in Italian:

![Example download page screenshot in Italian]({{ site.baseurl }}/public/images/bedrock-code-to-production/example-page-it.png)

Because our translations are done by volunteers, we try our best to minimize the number of string changes we ask them for. If a page is translated in over 40 locales and we change one string, that still requires 40 new translations to be made. If strings are changing every week, this can begin put a lot of strain on the goodwill of our community. To minimize this churn we try to:

  - Only change strings if absolutely necessary.
  - Try and batch up string changes to send out in one go.
  - Reuse existing strings that may already be translated (if similar to what's being asked for).
  - For new or redesigned pages that need to be translated for a set launch date, we typically ask for a lead time of 3-4 weeks.

Of course, each time we change a string on an existing page, we can't always wait 4 weeks before merging the change. For situations like this we often use an *l10n conditional tag* in the Jinja template. For example, if we wanted to change the main heading on our download page we could do:

{% raw %}
```jinja
<h1>
  {% if l10n_has_tag('page_heading_update') %}
    {{ _('Download Firefox today!') }}
  {% else %}
    {{ _('Get Firefox today') }}
  {% endif %}
</h1>
```
{% endraw %}

This allows locales to opt-in to the new translated string one by one, else they fall back to the original string.

We can also do this type of thing for entirely redesigned pages in our view logic, so locales only see the new design once they have it translated.

```python
def example_download_page(request):
    locale = l10n_utils.get_locale(request)

    if lang_file_is_active('firefox/example-page/redesign', locale):
        template = 'firefox/example-page/redesign.html'
    else:
        template = 'firefox/example-page/index.html'

    return l10n_utils.render(request, template)
```

Doing this does still come with technical debt of course, as the old content, conditional logic and `.lang` files still need cleaning up later on, once everyone is using the new translations.

## GitHub pull request

Once our page is coded and we're ready for the next step, we can open a [pull request on GitHub](https://help.github.com/articles/creating-a-pull-request/). Once this is done the following things typically happen:

  - Our continuous integration service, [CircleCI](https://circleci.com/), runs a series of automated checks on the pull request. This runs unit tests as well as checks the code for both syntax and style errors. Running these automated checks saves us significant time during code review by picking out routine errors.
  - The pull request must then be code reviewed by another human. Every code change gets reviewed by at least one other developer before merging.
  - If the change requires localization, strings are extracted from the branch and checked by our l10n team. If they look good, they are sent out to our volunteers for translation. Once this has begun, it is **very bad** to make a breaking change to a piece of copy.

## Other useful things to know about

When preparing for the launch of new content, there are several other commonly available tools and systems that are useful to know about:

### Demo servers (pmac?)

  - Demo deployments from feature branches via Jenkins
  - Link demo URLs in Bugzilla for stakeholder review & QA.

### A/B testing

For A/B testing bedrock has two options available, [Traffic Cop](http://bedrock.readthedocs.io/en/latest/mozilla-traffic-cop.html) and [Optimizely](https://www.optimizely.com/). [Jon](https://github.com/jpetto/) wrote a great blog post on the pros and cons of using each solution so we won't repeat them here. You should [go read it]({{ site.baseurl }}/2017/01/16/traffic-cop/).

### Analytics

Analytics on bedrock are provided using [Google Tag Manager](https://www.google.com/analytics/tag-manager/) (GTM). Most of bedrocks shared components and pages are pre-built for analytics using common [event handlers and data attributes](http://bedrock.readthedocs.io/en/latest/analytics.html#gtm-listeners-data-attributes). We can also create and fire [custom events](http://bedrock.readthedocs.io/en/latest/analytics.html#datalayer-push-example) as required.

GTM on bedrock is implemented in such a way that it respects DNT, and user experiences should not break if tracking protection or content blocking software is installed.

### Feature toggling (pmac?)

  - Use of switches for timed announcements
  - Avoid the need for scheduled production pushes, which can be disruptive.

## Ready for deployment (pmac?)

  - Once our code has passed review and is ready to merge

### Environments (pmac?)

  - Explain AWS infrastructure

  - Dev: [https://www-dev.allizom.org/](https://www-dev.allizom.org/)
    - US: [https://bedrock-dev.us-west.moz.works/](https://bedrock-dev.us-west.moz.works/)
    - EU: [https://bedrock-dev.eu-west.moz.works/](https://bedrock-dev.eu-west.moz.works/)
  - Stage: [https://www.allizom.org/](https://www.allizom.org/)
    - US: [https://bedrock-stage.us-west.moz.works/](https://bedrock-stage.us-west.moz.works/)
    - EU: [https://bedrock-stage.eu-west.moz.works/](https://bedrock-stage.eu-west.moz.works/)
  - Prod: [https://www.mozilla.org/](https://www.mozilla.org/)
    - US: [https://bedrock-prod.us-west.moz.works/](https://bedrock-prod.us-west.moz.works/)
    - EU: [https://bedrock-prod.eu-west.moz.works/](https://bedrock-prod.eu-west.moz.works/)

### Merges to master (pmac?)

  - Deployment pipeline
  - Run integration smoke tests in docker container
  - If all pass, deploy to dev environment.
  - Once deployed to dev, run integrations tests in Firefox.

### Production pushes (pmac?)

  - Tagged commits to `/prod` branch triggers push to stage
  - Full cross browser integration tests (plus sanity tests for legacy browsers) against stage usw.
  - If staging tests pass, push to prod usw.
  - Integration tests run again agains prod usw.
  - If prod usw is green, start pushing stage -> prod for euw.
