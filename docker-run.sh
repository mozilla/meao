#!/bin/bash -ex

export JEKYLL_VERSION=3.5
export JEKYLL_DEBUG=1
export JEKYLL_UID=$(id -u)
CMD="jekyll serve --watch --drafts"
echo "It will take 2-3 minutes, with no output, to start on macOS."
docker run --rm --label=jekyll --volume=$(pwd):/srv/jekyll -it -p 4000:4000 jekyll/jekyll:$JEKYLL_VERSION $CMD
