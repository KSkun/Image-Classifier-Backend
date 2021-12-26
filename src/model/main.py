from pymongo import MongoClient

from config import C

client = MongoClient(C.mongo_addr, C.mongo_port)
database = client[C.mongo_db]
