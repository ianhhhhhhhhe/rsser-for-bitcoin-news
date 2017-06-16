#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parser
import mongo
import time

list = [
    ('https://news.bitcoin.com/feed/','newsbitcoin'),
    ('http://www.coindesk.com/feed/','coindesk'),
    ('https://bitcoinmagazine.com/feed/','bitcoinmagazine'),
    ('http://www.newsbtc.com/feed/','newsbtc'),
]
db = mongo.MongoPipeline()

def main():
    for url in list:
        res = parser.parser(url[0],url[1])
        try:
            db.insert_db(res)
        finally:
            db.close_db()

if __name__ == '__main__':
    main()