Title: Pelican Blogging Improvements
Date: 2014-09-07 17:47
Tags: pelican, blog, performance
Slug: continuous-blogging-pt2
status: draft

It's been a while since I moved my blog to Pelican + Gihub + Travis + S3. As an introduction to pulic speaking I'm going to give a lighting talk at the [Auckland Continuous Delivery](http://www.meetup.com/Auckland-Continuous-Delivery/events/170237202/) meetup and there were a few things I wanted to get sorted before I did.

Asset Management
----------------

The theme I use doesn't rely on a lot of assets but when content is static, why not squeeze every bit of optimatization out?

The [webassets](http://docs.getpelican.com/en/3.1.1/plugins.html#asset-management) plugin provides filters for truncating and minifing css and js assets.

To install, add the ```assets``` plugin to ```PLUGINS``` list in ```pelicancont.py``` and install the required dependenencies. I used [cssmin](https://pypi.python.org/pypi/cssmin/0.2.0) for css and [Google's Closure](https://developers.google.com/closure/) for Javascript:

```bash
pip install cssmin closure
pip freeze > requirements.txt 
```

Use the assets tag in templates to apply filters to one or more resources to generate a single output file:

```python
# minify css
{% assets filters="cssmin", output="css/theme.min.css", "css/pure.css", "css/pygments.css" %}
    <link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
{% endassets %}

# minify javascript
{% assets filters="closure_js", output="js/packed.js", "js/scroll.js" %}
    <script src="{{ SITEURL }}/{{ ASSET_URL }}"></script>
{% endassets %}
```

GZIP Compression
----------------

GZIP compression was the improvement I most wanted to add the to the site's build chain. The content is largly html, which compresses quite nicely. Optimized images and minified css will drop a few K but are unlikely to make a big difference. 

First time around it felt too hard, and possibly impossible with the Travis S3 deployer. In order for S3 to correctly serve an html page that has been compressed, the Content-Encoding metadata for the file has be set correctly. Thanks to the new option [```detect_encoding: true```](https://github.com/travis-ci/travis-ci/issues/2400) it is possible for Travis to guess and set the Encoding type of a file.

![S3 Content Encoding](|filename|/images/s3-content-encoding.png)

The gzip_cache plugin compresses content into a ``.gz`` file along side the original file. Some web servers (e.g. Ngnix) are able to use the ``.gz`` files as a cache and do not need to perform real time compression.

Since I'm not using Ngnix (the whole point is to have no moving parts), this plugin wasn't quite going to do. But with a [few modiciations](https://github.com/getpelican/pelican-plugins/pull/298/commits) I was able to have it overwrite the originals, keeping the file name intact.

The results were quite impressive on paper. The file size of the index page halved from 8K to 4K. The overal reduction in all content was from 4.4M down to 3.4M and that includes 2.5M of images that didn't change. Excluding images that is around a 50% reduction in size with no noticable increase in build time.

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

The last major improvement I need to figure out is fixing the cache invalidation. Amazon seems pretty good at setting cache headers, but Travis does a full upload each build which causes S3 to invalidate all the cache headers.

Syncing on change is a more demanding build time process as it requires checking each existing file, but I think the benefits tot he end user will be pretty great as half the site's content won't change often!