from pymongo import MongoClient
from redis.client import Redis

from config import C

mongo_client = MongoClient(C.mongo_addr, C.mongo_port)
mongo_db = mongo_client[C.mongo_db]

redis_client = Redis(C.redis_addr, C.redis_port, C.redis_db)
