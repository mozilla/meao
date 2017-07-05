# MEAO

This is the source code repository for the
[The Marketing Engineering And Operations Team Blog](https://mozilla.github.io/meao/).

## Run with Docker

1. Run the Docker container:

```
./docker-run.sh
```

The site (with drafts) is available at http://localhost:4000/meao/

## Run with Ruby

1. Install [Bundler](http://bundler.io/):

```
gem install bundler
```

2. Install dependencies:

```
bundle install --path vendor/bundle
```

3. Serve the site with or without drafts enabled:

```
bundle exec jekyll serve
bundle exec jekyll serve --drafts
```

The site is available at http://127.0.0.1:4000/meao/

## Posts and Drafts

[Posts](https://jekyllrb.com/docs/posts/) appear in the ``_posts`` folder and
have a date in the filename, such as
``_posts/2017-07-04-happy-birthday-america.md``.  These are displayed in time
order, and posts with future dates are not published.

[Drafts](https://jekyllrb.com/docs/drafts/) appear in the ``_drafts`` folder
and do not have a date in the filename, such as
``_drafts/my-cool-blog-post.md``. They are useful for authoring a post, and
then moving it to the ``_posts`` folder when you are ready for a PR.  Drafts
must be enabled in ``jekyll`` to view drafts.
