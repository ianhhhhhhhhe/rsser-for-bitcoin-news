#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser

def parser(url, site_name):
    res = []
    parser = feedparser.parse(url)
    for item in parser.entries:
        page = dict()
        page['title'] = item.title
        page['link'] = item.link
        page['time'] = item.published
        page['site'] = site_name
        res.append(page)
    return res