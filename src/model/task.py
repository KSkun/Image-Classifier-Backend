import json

from bson import ObjectId

from model.main import mongo_db, redis_client

_col_task = mongo_db['task']

_spider_stream_name: str = 'spider_cmd'
_spider_group_name: str = 'spider'

_classifier_stream_name: str = 'classify_cmd'
_classifier_group_name: str = 'classifier'


def init_spider_stream():
    if redis_client.exists(_spider_stream_name):
        redis_client.delete(_spider_stream_name)

    redis_client.xadd(_spider_stream_name, {'cmd': json.dumps({
        'operation': 'init',
        'task_id': '',
        'keyword': '',
        'engines': [],
        'limit': 0
    })})
    redis_client.xgroup_create(_spider_stream_name, _spider_group_name, 0)


def init_classifier_stream():
    if redis_client.exists(_classifier_stream_name):
        redis_client.delete(_classifier_stream_name)

    redis_client.xadd(_classifier_stream_name, {'op': 'init'})
    redis_client.xgroup_create(_classifier_stream_name, _classifier_group_name, 0)


def insert_task(task):
    return _col_task.insert_one(task).inserted_id


def push_spider_cmd(task):
    redis_client.xadd(_spider_stream_name, {'cmd': json.dumps(task)})


def get_task_list_by_user(user_id: ObjectId):
    return list(_col_task.find({'user': user_id}))
