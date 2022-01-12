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

    # create new stream & consumer group
    redis_client.xadd(_spider_stream_name, {'cmd': json.dumps({
        'operation': 'init',  # init command
        'task_id': '',
        'keyword': '',
        'engines': [],
        'limit': 0
    })})
    redis_client.xgroup_create(_spider_stream_name, _spider_group_name, 0)


def init_classifier_stream():
    if redis_client.exists(_classifier_stream_name):
        redis_client.delete(_classifier_stream_name)

    # create new stream & consumer group
    redis_client.xadd(_classifier_stream_name, {'op': 'init'})  # init command
    redis_client.xgroup_create(_classifier_stream_name, _classifier_group_name, 0)


def insert_task(task):
    """
    Create task document in MongoDB

    :arg task: task document
    """
    return _col_task.insert_one(task).inserted_id


def push_spider_cmd(cmd):
    """
    Create spider command

    :param cmd: command object
    """
    redis_client.xadd(_spider_stream_name, {'cmd': json.dumps(cmd)})


def get_task_list_by_user(user_id: ObjectId):
    """
    Find tasks by user ObjectId

    :param user_id: user ObjectId
    :return: list of tasks
    """
    return list(_col_task.find({'user': user_id}))


def get_task(task_id: ObjectId):
    """
    Find task by its ObjectId
    
    :param task_id: task ObjectId 
    :return: task document
    """
    return _col_task.find_one({'_id': task_id})
