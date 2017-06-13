#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import pymongo
from logger import logger
from config import MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION
import time
import datetime


class MongoPipeline(object):
    def __init__(self):
        self.mongo_url = MONGO_URL
        self.mongo_database = MONGO_DATABASE
        self.mongo_collection = MONGO_COLLECTION
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_database]
        self.collection = self.db[self.mongo_collection]

    def insert_db(self, items):
        if not type(items) == type(list()):
            raise TypeError('Type of item must be list')
        for item in items:
            it = list(self.collection.find({'title': item['title']}))
            item = self.process_item(item)
            if it:
                print('item is found')
            else:
                self.collection.insert(item)
                print('item inserted')

    def close_db(self):
        self.client.close()

    def process_item(self, item):
        item['time'] = datetime.datetime.fromtimestamp(
            time.mktime(
                time.strptime(
                    item['time'][:24], '%a, %d %b %Y %H:%M:%S'))).strftime('%Y-%m-%d-%H-%M-%S')
        return item
