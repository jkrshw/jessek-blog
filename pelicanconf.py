#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jesse Kershaw'
SITENAME = u'Jessek'
SITEURL = 'http://www.jessek.co.nz'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Menu link
MENUITEMS = (('Archive', './archives.html'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/jkrshw/'),
    ('twitter-square', 'https://twitter.com/jkrshw'),
    ('google-plus-square', 'https://plus.google.com/+JesseKershaw'),
)

TWITTER_USERNAME = "jkrshw"

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Urls
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['sitemap', 'summary', 'optimize_images', 'representative_image', 'assets']

SITEMAP = {'format': "xml"}

# Theme
THEME = "pure"
COVER_IMG_URL = "/images/cover.jpg"
