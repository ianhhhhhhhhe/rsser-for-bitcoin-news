#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parser
import mongo
import time

list = [
    ('http://www.8btc.com/feed', '8btc'),
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