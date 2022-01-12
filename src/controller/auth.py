from datetime import datetime

import jwt
from flask_httpauth import HTTPTokenAuth

from config import C

auth = HTTPTokenAuth(scheme='Bearer')  # auth via Authorization header, Bearer token


@auth.verify_token
def verify_token(token):
    """Verify the JWT token"""
    payload = jwt.decode(token, key=C.jwt_secret, algorithms=[C.jwt_algorithm])
    # token expired
    if 'exp' not in payload or datetime.fromtimestamp(payload['exp']) < datetime.now():
        return None
    # id not set
    if 'id' not in payload:
        return None
    return payload['id']
