from http import HTTPStatus

from bson import ObjectId
from flask import request, abort

from controller.auth import auth
from controller.main import image_bp
from controller.response import response_error, response_success
from model.image import find_image_list_by_task
from model.task import get_task


@image_bp.route('/list', methods=['GET'])
@auth.login_required
def get_image_list():
    self_id = ObjectId(auth.current_user())

    task_id_str = request.args.get('task')
    if task_id_str is None:
        abort(response_error(HTTPStatus.BAD_REQUEST, None, 'invalid username or password'))
        return
    try:
        task_id = ObjectId(task_id_str)
    except Exception as e:
        abort(response_error(HTTPStatus.BAD_REQUEST, e, 'invalid task'))
        return
    task = get_task(task_id)
    if task['user'] != self_id:
        abort(response_error(HTTPStatus.FORBIDDEN, None, 'permission denied'))
        return

    _images = find_image_list_by_task(task_id)
    images = []
    for _img in _images:
        image = {
            'url': _img['url'],
            'class': _img['class']
        }
        images.append(image)
    return response_success({'images': images})
