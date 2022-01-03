import base64
import binascii
from datetime import datetime, timedelta
from http import HTTPStatus

import bcrypt
import jwt as jwt
from flask import request, abort

from config import C
from controller.main import user_bp
from controller.response import response_error, response_success
from model.user import *


@user_bp.route('/token', methods=['GET'])
def user_get_token():
    username = request.args.get('username')
    password_encoded = request.args.get('password')
    if username is None or password_encoded is None:
        abort(response_error(HTTPStatus.BAD_REQUEST, None, 'invalid username or password'))
        return
    try:
        password = base64.b64decode(password_encoded, validate=True)
    except binascii.Error as e:
        abort(response_error(HTTPStatus.BAD_REQUEST, e, 'invalid username or password'))
        return

    # check password
    user = find_user_by_name(username)
    if user is None or not bcrypt.checkpw(password, user['password'].encode()):
        abort(response_error(HTTPStatus.BAD_REQUEST, None, 'invalid username or password'))
        return

    # sign token
    token_exp = datetime.now() + timedelta(minutes=C.jwt_expire)
    token = jwt.encode({'id': str(user['_id']), 'iat': datetime.now().timestamp(), 'exp': token_exp.timestamp()},
                       C.jwt_secret, algorithm=C.jwt_algorithm)
    return response_success({'token': token, 'expire_at': token_exp.timestamp()})
