#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'AC Craft'
SITENAME = 'AC Craft - Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

THEME='pelican-blueidea'

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/ace_d0g'),)

DEFAULT_PAGINATION = 10

PAGE_EXCLUDES = ('extras')

STATIC_PATHS = ['embedded']	

ARTICLE_EXCLUDES = [
    'extras'
	,'embedded'
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
