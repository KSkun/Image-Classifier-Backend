from typing import Any

from flask import make_response, jsonify

from config import C


def response_error(status: int, error: Any, error_mask: str, data: Any = None):
    """Error response template"""
    if not C.debug or error is None:
        error = error_mask
    return make_response(jsonify({'success': False, 'error': str(error), 'data': data}), status)


def response_success(data: Any):
    """Success response template"""
    return {'success': True, 'error': None, 'data': data}
