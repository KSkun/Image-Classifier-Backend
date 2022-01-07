import json

from model.main import mongo_db, redis_client

_col_task = mongo_db['task']

_stream_name: str = 'spider_cmd'
_group_name: str = 'spider'


def init_task_stream():
    if redis_client.exists(_stream_name):
        redis_client.delete(_stream_name)

    redis_client.xadd(_stream_name, {'cmd': json.dumps({
        'operation': 'init',
        'task_id': '',
        'keyword': '',
        'engines': [],
        'limit': 0
    })})
    redis_client.xgroup_create(_stream_name, _group_name, 0)


def insert_task(task):
    return _col_task.insert_one(task).inserted_id


def push_task(task):
    redis_client.xadd(_stream_name, {'cmd': json.dumps(task)})
