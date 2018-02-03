#!/bin/bash -ex

export JEKYLL_VERSION=3.5
export JEKYLL_DEBUG=1
export JEKYLL_UID=$(id -u)
CMD="jekyll serve --watch --drafts"
docker run --rm --label=jekyll --volume=$(pwd):/srv/jekyll -it -p 4000:4000 jekyll/jekyll:$JEKYLL_VERSION $CMD
