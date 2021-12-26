import json

from model.main import mongo_db, redis_client

_col_task = mongo_db['task']

_stream_name: str = 'spider_cmd'
_group_name: str = 'spider'


def insert_task(task):
    return _col_task.insert_one(task).inserted_id


def push_task(task):
    redis_client.xadd(_stream_name, {'cmd': json.dumps(task)})
