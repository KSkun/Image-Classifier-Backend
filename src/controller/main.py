from flask import Blueprint

main_bp = Blueprint('main', __name__, url_prefix='/api')

user_bp = Blueprint('user', __name__, url_prefix='/user')
from controller.user import *

task_bp = Blueprint('task', __name__, url_prefix='/task')
from controller.task import *


def init_controller():
    main_bp.register_blueprint(user_bp)
    main_bp.register_blueprint(task_bp)
