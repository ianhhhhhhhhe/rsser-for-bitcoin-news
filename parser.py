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
        print(page)
        res.append(page)
    return res

def mark(tag):
    if tag == '比特币' or tag == 'Bitcoin':
        tag = 'bitcoin'
    if tag == '区块链':
        tag = 'blockchain'
    tag = 'digitalcoin'
    return tag