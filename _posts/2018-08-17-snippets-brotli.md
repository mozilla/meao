---
layout: post
title: "Using Brotli compression to reduce CDN costs"
author: Giorgos Logiotatidis
author_url: https://giorgos.sealabs.net
excerpt_separator: <!--more-->
---

The [Snippets Service](https://github.com/mozilla/snippets-service/) allows
Mozilla to communicate with Firefox users directly by placing a snippet of text
and an image on their new tab page. Snippets share exciting news from the
Mozilla World, useful tips and tricks based on user activity and sometimes
jokes.

To achieve personalized, activity based messaging in a privacy respecting and
efficient manner, the service creates a Bundle of Snippets per locale. Bundles
are HTML documents that contain all Snippets targeted to a group of users,
including their Style-Sheets, images, metadata and the JS decision engine.

The Bundle is transferred to the client where the locally executed decision
engine selects a snippet to display. A carefully designed system with multiple
levels of caching takes care of the delivery. One layer of caching is a
CloudFront CDN.


## The problem

During the last months we observed a significant uptake of our CDN costs as
Mozilla's Lifecycle Marketing Team was increasing the number of Snippets for the
English language from about 10 to 150.

The Bundle file-size increased from about 200 KiB to more than 4MiB. Given that
Firefox requests new Bundles every 4 hours that translated to about 75 TB of
transferred data per day or about 2.25 PB (yes, that's Petabytes!) of data
transferred per month, despite the local browser caching.

<!--more-->

## The solution

Bundles include everything a Snippet needs to be displayed: the targeting rules,
the text and the image in a base64 encoded format. First hypothesis was that we
could reduce the Bundle size by reducing the image size. We run
[optipng](http://optipng.sourceforge.net/) against all images in the bundle to
prove the hypothesis. The images were optimized but the Bundle shrunk for only
100KiB, about 2.5% of the total size.

Second hypothesis was to replace the images with links to images. Since not all
Snippets are displayed to all users, we can benefit by not transferring all
images to all users. This reduced the Bundle size to 1.1MiB without accounting
for the size of the images that will be transferred.

Third hypothesis was to replace GZip with Brotli compression.
[Brotli](https://en.wikipedia.org/wiki/Brotli) is a modern compression algorithm
supported by Firefox and all other major browsers as alternative method for HTTP
Compression.

Brotli reduced the size of the bundle down to 500KiB, about 25% of the size of
the CloudFront GZip mechanism which compressed the bundle to about 2.2MiB.

Since CloudFront does not support on the fly Brotli compression, we prepare and
compress the Bundles on the app level before uploading to S3. By adding the
correct Content-Encoding headers, the S3 objects are ready to be served by the
CDN.

## Conclusions

Although all three solutions can reduce the Bundle size, the third provided the
best performance to effort ratio and we proceeded with implementation. Next day
reports graphed a significant drop on costs marking the project a success. From
the original average of 75TB transferred data per day, we dropped down to 15TB.
We are going to further improve in the future by moving the images outside the
Bundle.

It's clear that Brotli compression can achieve significantly higher compression
rates compared to GZip at the expense of more CPU time. Even though our CDN of
choice doesn't support Brotli, assets can be pre-compressed and uploaded ready
for use.

## Relevant Links

 - [Brotli Compression](https://en.wikipedia.org/wiki/Brotli) on Wikipedia
 - [Snippets Service](https://github.com/mozmeao/snippets-service) on GitHub
