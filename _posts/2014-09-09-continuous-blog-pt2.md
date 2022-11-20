---
layout: post
title: Continuous Blogging Pt II
date: 2014-09-09 17:47
tags: pelican, blog, performance
slug: continuous-blogging-pt2
---

It's been a while since I moved my blog to Pelican + Github + Travis + S3. At the risk of only blogging about how I build this blog, I thought I'd do a follow up post to [Continuos Blogging](|filename|/Posts/continuous-blog.md). 

I'm going to give a lighting talk at the [Auckland Continuous Delivery](http://www.meetup.com/Auckland-Continuous-Delivery/events/170237202/) meetup on how I build the blog and there were a few improvements I wanted to get done before the talk. Here's what I did to improve the site's performance.

<!-- PELICAN_END_SUMMARY -->

Asset Management
----------------

The [webassets](http://docs.getpelican.com/en/3.1.1/plugins.html#asset-management) plugin provides filters for concatentating and minifing css and js assets. This reduces the size and number of web requests during page load.

To install, add the ```assets``` plugin to ```PLUGINS``` list in ```pelicancont.py``` and install the required dependenencies. I used [cssmin](https://pypi.python.org/pypi/cssmin/0.2.0) for css and Google's [Closure](https://developers.google.com/closure/) for Javascript:

```bash
pip install cssmin closure
pip freeze > requirements.txt 
```

Use the assets tag in templates to apply filters to one or more resources to generate a single output file:

```python
{% raw %}
# minify css
{% assets filters="cssmin", output="css/theme.min.css", "css/pure.css", "css/pygments.css" %}
    <link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
{% endassets %}

# minify javascript
{% assets filters="closure_js", output="js/packed.js", "js/scroll.js" %}
    <script src="{{ SITEURL }}/{{ ASSET_URL }}"></script>
{% endassets %}
{% endraw %}
```

Depending on the amount of css and javascript used in your theme, this will drop a few requests from each page load and reduce a bit of whitepsace from the downloads. The ```ASSET_URL``` variable takes care of caching by adding a small hash to the end of the src url.

```html
<link rel="stylesheet" href="./theme/css/theme.min.css?23675065">
<script src="./theme/js/packed.js?5c1654cd"></script>
```

GZIP Compression
----------------

GZIP compression was the improvement I most wanted to add the to the site's build chain. The content is largly html, which compresses quite nicely. Optimized images and minified css will drop a few K but are unlikely to make a big difference to percieved performance. 

First time around it felt too hard, and possibly impossible with the Travis S3 deployer. In order for S3 to correctly serve an html page that has been compressed, the Content-Encoding metadata for the file has to be set correctly. Thanks to the new option [```detect_encoding: true```](https://github.com/travis-ci/travis-ci/issues/2400) it is possible for Travis to guess and set the Encoding type of a file.

![S3 Content Encoding](|filename|/images/s3-content-encoding.png)

The [gzip_cache](https://github.com/getpelican/pelican-plugins/tree/master/gzip_cache) plugin compresses content into a ``.gz`` file along side the original file. Some web servers (e.g. Ngnix) are able to use the ``.gz`` files as a cache and do not need to perform real time compression.

Since I'm not using Ngnix (the whole point is to have no moving parts), this plugin wasn't quite going to do. But with a [few modiciations](https://github.com/getpelican/pelican-plugins/pull/298/commits) I was able to have it overwrite the originals, keeping the file name intact.

The results were quite impressive on paper. The file size of the index page halved from 8K to 4K. The overal reduction in size of all content was from 4.4M down to 3.4M and that includes 2.5M of images that didn't change. Excluding images that is around a 50% reduction in size with no noticable increase in build time.

```
original    gzip    
156K        88K     output/2011
116K        60K     output/2012
80K         40K     output/2013
108K        52K     output/2014
20K         4.0K    output/archives.html
84K         40K     output/author
4.0K        4.0K    output/authors.html
4.0K        4.0K    output/categories.html
84K         40K     output/category
16K         8.0K    output/drafts
288K        68K     output/feeds
2.5M        2.5M    output/images
8.0K        4.0K    output/index2.html
8.0K        4.0K    output/index3.html
8.0K        4.0K    output/index4.html
8.0K        4.0K    output/index5.html
8.0K        4.0K    output/index6.html
12K         4.0K    output/index7.html
12K         4.0K    output/index8.html
8.0K        4.0K    output/index9.html
8.0K        4.0K    output/index.html
192K        156K    output/posts
20K         4.0K    output/sitemap.xml
612K        304K    output/tag
8.0K        4.0K    output/tags.html
72K         60K     output/theme
```

Caching
-------

The Travis S3 deployer performs a full upload of the output folder each deploy. It does not handle deletions or detect unchanged files. So on each upload, every file is marked as being modified.

Since the images account for 50% of the content by size, and are the less likely to change it would be nice not to reupload them each deploy.

I decided it would be simple enough to create a file containing the hash of each image and upload it to the blog. Before deploying, compare the current hashes with the hashes downloaded from the live site and remove unchanged files from the output directory.  New and modified files will be uploaded and since Travis doesn't delete files from S3, the removed images will be left unchanged in the bucket.

Since this is a Pelican project I thought I'd have a go at scripting this simple sync algorithm in Python. I cheated a little (a lot) by using system calls to ```md5sum``` and ```wget``` to do the hard work of calculating the hashes and retrieving the old hashes from the live site and borrowed a few lines of code from [stackoverflow](http://stackoverflow.com/questions/4803999/python-file-to-dictionary) to read in the output. Then it was a simple matter of looking for unchanged hashes and deleting them from the output folder.

```python
import os
def read_hash(filename):
    with open(filename) as f:
        return dict([line.split() for line in f])

#########  main program ###########
os.system("wget -q -O old_images.md5 http://jessek.co.nz/images.md5")
os.system("md5sum output/images/* > output/images.md5")

new_hashes = read_hash("output/images.md5")
old_hashes = read_hash("old_images.md5")

for key in new_hashes.viewkeys() & old_hashes.viewkeys():
    print 'removing unchanged file %s' % new_hashes[key]
    os.remove(new_hashes[key])
```

That's it. You can see the full script in the [blog repository](https://github.com/jkrshw/jessek-blog/blob/master/deploy/simple-sync.py). Go easy on it, it's my first hack at Python. 

The script is invoked before the deploy by adding a ```before_deploy``` command to ```.travis.yml```

```yml
before_deploy: deploy/simple-sync.py
deploy:
  provider: s3
  ...
```

This little script solves the biggest bugbear with the blog. The flicker of the home page as the cover image is downloaded each time I visit the site after an update. Now that I'm mostly happy with the build maybe I'll have to think of some actual content to write...

_Update: After tinkering a bit more with the simple-sync script I extended it to check all files in the output directory for changes. I also hardended it a little against edge cases where I might have two files with the same md5 hash in different directories. See the [source](https://github.com/jkrshw/jessek-blog/blob/master/deploy/simple-sync.py) for changes_
