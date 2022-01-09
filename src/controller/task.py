from http import HTTPStatus
from typing import Dict, Any, List

from flask import request, abort

from controller.auth import auth
from controller.main import task_bp
from controller.response import response_success, response_error
from model.task import *

_available_engines = [
    {'name': 'baidu', 'display_name': '百度'},
    {'name': 'google', 'display_name': 'Google'},
]

_available_engine_names = ['baidu', 'google']


@task_bp.route('/engines', methods=['GET'])
def get_available_engines():
    return response_success({'engines': _available_engines})


@task_bp.route('', methods=['POST'])
@auth.login_required
def create_task():
    task: Dict[str, Any] = request.get_json()

    if 'keyword' not in task or 'engines' not in task or 'limit' not in task:
        abort(response_error(HTTPStatus.BAD_REQUEST, None, 'missing required fields'))
        return
    for engine in task['engines']:
        if engine not in _available_engine_names:
            abort(response_error(HTTPStatus.BAD_REQUEST, None, 'unsupported engine name'))
            return

    mongo_task = task.copy()
    mongo_task['user'] = ObjectId(auth.current_user())
    mongo_task['spider_done'] = False
    mongo_task['classifier_done'] = False
    task_id = insert_task(mongo_task)

    redis_task = task.copy()
    redis_task['operation'] = 'crawl'
    redis_task['task_id'] = str(task_id)
    push_spider_cmd(redis_task)

    return response_success({'_id': str(task_id)})


@task_bp.route('/list', methods=['GET'])
@auth.login_required
def get_task_list():
    self_id = ObjectId(auth.current_user())
    tasks = []
    db_tasks: List[Dict[str, object]] = get_task_list_by_user(self_id)
    for db_task in db_tasks:
        task = db_task.copy()
        task['id'] = str(task['_id'])
        task.pop('_id')
        task.pop('user')
        tasks.append(task)
    return response_success({'tasks': tasks})


@task_bp.route('/<id>', methods=['GET'])
@auth.login_required
def get_task_info(id):
    self_id = ObjectId(auth.current_user())
    try:
        task_id = ObjectId(id)
    except Exception as e:
        abort(response_error(HTTPStatus.BAD_REQUEST, e, 'invalid id'))
        return
    task = get_task(task_id)
    if task['user'] != self_id:
        abort(response_error(HTTPStatus.FORBIDDEN, None, 'permission denied'))
        return
    task.pop('user')
    task.pop('_id')
    return response_success(task)
