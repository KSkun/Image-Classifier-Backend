import logging

from pymongo import MongoClient
from redis.client import Redis

from config import C

# mongo client instance
mongo_client = MongoClient(C.mongo_addr, C.mongo_port)
try:
    mongo_client.server_info()
except Exception as e:
    logging.getLogger('image-classifier-backend').error('mongo error, ' + str(e))
    exit(1)
mongo_db = mongo_client[C.mongo_db]

# redis client instance
redis_client = Redis(C.redis_addr, C.redis_port, C.redis_db)
try:
    redis_client.ping()
except Exception as e:
    logging.getLogger('image-classifier-backend').error('redis error, ' + str(e))
    exit(1)
