---
layout: post
title: "Bedrock: The SQLitening"
author: Paul McLanahan
excerpt_separator: <!--more-->
---

On it's face [www.mozilla.org](https://www.mozilla.org/) doesn't look like it'd be a complex application to write, maintain, or run.
But when you throw over 100 million unique visitors per week at any site it can complicate things quickly. Add to that translations
of the content into over 100 languages and you can start to get the idea of where it might get interesting. So we take every
opportunity to simplify and reduce hosting complexity and cost we can get. This is the place from which the idea to
[switch to using SQLite](https://github.com/mozilla/bedrock/pull/5334) for our database needs in production was born.

<!--more-->

The traditional answer to the question "should we use SQLite for our web application in production?" is an emphatic ***NO***. But,
again, [bedrock][] is different. It uses its database as a read-only data store as far as the web application is concerned. We run a
single data updater process (per cluster) that does the writing of the updates to the DB server that all of the app instances use.
Most of bedrock is static content coded directly into templates, but we use the database to store things like product release
notes, security advisories, blog posts, twitter feeds, and the like; basically anything that needs updating more often than
we deploy the site. SQLite is indeed a bad solution for a typical web application which is writing and reading data in its
normal function because SQLite rightly locks itself to a single writer at a time, and a web app with any traffic almost certainly
needs to write more than one thing at a time. But when you only need to read data then SQLite is an incredibly fast and robust
solution to data storage.

## Data Updates

The trick with a SQLite store is refreshing the data. We do still need to update all those bits of data I mentioned before. Our
solution to this is to keep the aforementioned single process updating the data, but this time it will update a local SQLite file,
calculate a hash of said file, and upload the database and its metadata (a JSON file that includes the SHA256 hash) to AWS S3.
The Docker containers for the web app will also have a separate process running that will check for a new database file on a schedule
(every 5 min or so), compare its metadata to the one currently in use, download the newer database, check its hash against the one from
the metadata to ensure a successful download, and swap it with the old file atomically with the web app none the wiser. Using Python's
`os.rename` function to swap the database file ensures an atomic switch with zero errors due to a missing DB file. We thought about using
symlinks for this but it turns out to be harder to re-point a symlink than to just do the rename which atomically overwrites the old file
with the new (I'm pretty sure it's actually just updating the inode to which the name points but I've not verified that).

When all of this is working it means that bedrock no longer requires a database server. We can turn of our AWS RDS instances and never
have to worry about DB server maintenance or downtime. The site isn't all that much faster since like I said it's mostly spending time
rendering Jinja templates, but it is a lot cheaper to run and less likely to go down. We are also making DB schema changes easier and
more error-free since the DB filenames include the git hash of the version of bedrock that created it. This means that the production
Docker images contain an updated and migrated database file, and it will only download an update once the same version of the site
is the one producing database files.

And production advantages aren't the only win: we also have a much more simple development bootstrap process now since getting all of
the data you need to run the full site is a simple matter of either running `bin/run-db-download.py` or pulling the prod docker image
(`mozorg/bedrock:latest`) which will contain a decently up-to-date database and the machinery to keep it updated that requires no AWS
credentials since the database is publicly available.

## Verifying Updates

Along with actually performing the updates in every running instance of the site we also need to be able to monitor that said updates
are actually happening. To this end we created [a page on the site](https://www.mozilla.org/healthz-cron/) that will give us some
data on when the last time that instance ran the update, the git hash of bedrock that is currently running, the git hash used to
create the database in use, and how long ago said database was updated. This page will also respond with a 500 code instead of the normal 200 if the DB and L10n update tasks happened too long ago. At the time of writing the updates happen every 5 minutes, and the page would
start to fail at 10 minutes of no updates. Since the updates and the site are running in separate processes in the Docker container, we
need a way for the cron process to communicate to the web server the time of the last run for these tasks. For this we decided on
files in `/tmp` that the cron jobs will simply `touch`, and the web server can get the `mtime` (check out
[the source code](https://github.com/mozilla/bedrock/blob/c78da5c65b5b4a902b1e71f82a16a65aa90fcbf8/bedrock/base/views.py#L103-L129) for details).

To actually monitor this view we are starting with simply using New Relic Synthetics pings of this URL at each of our clusters
(currently oregon-b, tokyo, and frankfurt). This is a bit suboptimal because it will only be checking whichever pod happens to respond
to that particular request. In the near future our plan is to move to creating another process type for bedrock
that will query Kubernetes for all of the running pods in the cluster and ping each of them on a schedule. We'll then ping
[Dead Man's Snitch][] (DMS) on every fully successful round of checks, and if they fail more than a
couple of times in a cluster we'll be notified. This will mean that bedrock will be able to monitor itself for data update troubles.
We also ping DMS on every database update run, so we should know quickly if either database uploading or downloading is having trouble.

## Conclusions

We obviously don't yet know the long-term affects and consequences of this change (as of writing it's been in production less than a day),
but for now our operational complexity and costs are lower. I feel confident calling it a win for our deployment reliability for now.
Bedrock may eventually move toward having a large part of it pre-generated and hosted statically, but for now this version feels like the
one that will be as robust, resilient, and reliable as possible while still being one big Django web application.

[bedrock]: https://github.com/mozilla/bedrock/
[Dead Man's Snitch]: https://deadmanssnitch.com/
