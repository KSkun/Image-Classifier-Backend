from flask import Blueprint

main_bp = Blueprint('main', __name__, url_prefix='/api')  # /api

user_bp = Blueprint('user', __name__, url_prefix='/user')  # /api/user
from controller.user import *

task_bp = Blueprint('task', __name__, url_prefix='/task')  # /api/task
from controller.task import *

image_bp = Blueprint('image', __name__, url_prefix='/image')  # /api/image
from controller.image import *


def init_controller():
    main_bp.register_blueprint(user_bp)
    main_bp.register_blueprint(task_bp)
    main_bp.register_blueprint(image_bp)
