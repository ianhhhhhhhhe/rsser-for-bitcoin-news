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
        page['tag'] = mark(item.category)
        page['photo'] = None
        page['lang'] = 'cn'
        res.append(page)
    return res

def mark(tag):
    if tag == u'比特币' or tag == 'Bitcoin':
        tag = 'bitcoin'
    elif tag == u'区块链':
        tag = 'blockchain'
    else:
        tag = 'digitalcoin'
    return tag
