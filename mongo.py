#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import pymongo
from logger import logger
from config import MONGO_URL, MONGO_DATABASE, MONGO_COLLECTION

class MongoPipeline(object):
    def __init__(self):
        self.mongo_url = MONGO_URL
        self.mongo_database = MONGO_DATABASE
        self.mongo_collection = MONGO_COLLECTION
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_database]
        self.collection = self.db[self.mongo_collection]
    
    def insert_db(self, item):
        self.collection.insert(item)

    def close_db(self):
        self.client.close()