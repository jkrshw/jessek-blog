Title: Using Pelican Static Site Generator
Date: 2014-05-04 19:24
Tags: blog, pelican, python
Slug: pelican-static-blog

Hello! Welcome to the updated [jessek.co.nz](jessek.co.nz).

[Blogger](www.blogger.com) wasn't really working out. A wysiwyg editor is nice and all but code snippets looked awful and the template was over the top. I wanted something simpler for my blog and something new to try out.

The two options I considered were [jekyll](http://jekyllrb.com/) and [Pelican](http://blog.getpelican.com/). <!-- PELICAN_END_SUMMARY --> After a moments deliberation I decided to try out Pelican. Pelican is written in Python, with only a little Python experience it sounded fun.

## Porting

Pelican does have some import tools, but none for blogger. As I'm not a terribly prolific writer it was easy enough to copy and paste everything into Sublime and adding markdown for formatting.

To ensure URLs from blogger were preserved I modified the default settings to match blogger's, allowing existing links follow through to the new site.

```python
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
```

## Theme

I tried a few of the pelican themes and eventually settled on [Pure](https://github.com/PurePelicanTheme/pure). I like the cover image layout and with few tweaks it works OK. There are a few more things I want to try out but I'm happy with it for now. I did find an error in the theme and through the magic of OSS was able to let the author know and it was [fixed](https://github.com/PurePelicanTheme/pure/pull/7) almost immediately.

## Hosting

As a static site there are quite a few options for hosting. The one I liked the sound of the most was using Amazon Web Services S3. I used a blog post on [lexual.com](http://lexual.com/blog/setup-pelican-blog-on-s3/) to get started and then found that Amazon provide a lot of [user guides](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) and it was fairly straight forward to upload the content and make it available on the web.

My DNS provider was a little harder to set up. The admin console is over simplified and it took me a while to realise I could change the name servers and use Amazon Route 53 for all of the configuration options.

After a month my frist bill from Amazon has arrived and is a mighty $0.51. I'll leave it to you to infer as to whether Amazon is very cheap or this blog doesn't get a lot of visits.

## Plugins

Pelican has a large list of [plugins](https://github.com/getpelican/pelican-plugins). I haven't explored much yet but would really like something that ties the blog in with a git repository for version tracking. If it doesn't exist I might look at building one...