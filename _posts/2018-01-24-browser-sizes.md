---
layout: post
title: How to make a chart of your users' window sizes
author: Stephanie Hobson
excerpt_separator: <!--more-->
---

In preparation for the MDN redesign I examined our analytics to get an idea
of how wide our users' browser windows were. I wanted window widths, not screen
sizes and I thought a chart would tell a more compelling story than a table.

<!--more-->

Here's the chart I made:

![Chart of MDN window widths showing spikes at 1350 and 1900 pixels and very
little between 420 and 930 pixels.]({{ site.baseurl }}/public/images/2018-01-24-browser-sizes/browser-sizes.png)

I found this view useful because it shows us "clumps" of window sizes.

## How to make a chart of browser window widths

### The basic idea is:
1. Create and export a Custom Report for Browser Size.
1. Filter the Browser Size to just include widths.
1. Aggregate the number of users for each width.
1. Make a chart.

### Working with Google Analytics and Google Sheets the specific steps I used were:
1. Create a custom report for browser sizes.
    1. **Customization** > **Custom Reports** > **New Custom Report**
    1. Set the **Metric Group** to `Users`
    1. Set **Dimension Drilldowns** to `Browser Size`
    1. Save
1. View the custom report.
1. Set **Show rows:** to `5000`.
1. Export to Google Sheets.
1. Delete the extra stuff from the top and bottom of the export, you just want
   two columns: **Browser Size**, and **Users**.
1. Create a new column (C) called **Width**. Add this regex to it and fill down:
   `=REGEXEXTRACT(A2, "^[0-9]+")`. This gives you a column with just the width
   part of the browser size.
1. Create a new column (D) called **Unique List**. Add this formula to it (you
   don't need to fill down): `=UNIQUE(C2:C5001)`.This gives you a list of
   widths with no repeating values. That means 1900x950 and 1900x970 will be
   treated the same in our final chart.
1. Create a new column (E) called **Conditional Sums**. Add this formula and
   fill down the height of your Unique List: `=SUMIF(C$2:C$5001,D2,B$2:B$5000)`.
1. Copy the **Unique List** and **Conditional Sums** columns.
1. Create a new sheet in your document.
1. Use **Edit** > **Paste special** > **Paste values only** to paste only the
   computed values of these columns.
1. Rename **Unique List** to **Width** and **Conditional Sums** to **Total
   Users**.
1. Find the *(not set)* row and delete it.
1. Make sure both columns are being treated as numbers (a hint this is happening
   properly is that they are right aligned). If you have headings on the columns
   make sure they're frozen (**View** > **Freeze** > **1 row**).
1. Sort on **Width** from A→Z.
1. Select both columns and create a chart (**Insert** > **Chart**). (I made a
   "Stepped area chart")
1. Set **Width** as the X-axis.
1. Done!

___

This answered a question I've been curious about for ages: *Do people with
large monitors use MDN full screen?* About 40% of our users have a screen
resolution of 1900px or wider and 25% of our users use MDN at 1900px or wider.
