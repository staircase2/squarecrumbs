#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Staircase 2 Productiosn Pte Ltd'
SITENAME = u'SquareCrumbs - Learning Together, Everywhere'
SITEURL = 'http://staircase2.github.io/squarecrumbs_landing'
RELATIVE_URLS = True


PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#INDEX_SAVE_AS = '/index.html'
#INDEX_URL = '/'

LOAD_CONTENT_CACHE = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_ORDER_BY = "sortorder"
