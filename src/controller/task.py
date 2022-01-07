from http import HTTPStatus

from flask import request, abort
from typing import Dict, Any

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
    mongo_task['status'] = 'pending'
    task_id = insert_task(mongo_task)

    redis_task = task.copy()
    redis_task['operation'] = 'crawl'
    push_task(redis_task)

    return response_success({'_id': str(task_id)})
