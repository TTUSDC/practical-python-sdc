
from pymongo import MongoClient


class MongoConnector(object):

    def __init__(self, app):
        self.app = app
        uri = ""
        self.db = MongoClient(uri)
