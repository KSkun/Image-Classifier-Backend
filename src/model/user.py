from model.main import mongo_db

_col_user = mongo_db['user']


def find_user_by_name(username: str):
    return _col_user.find_one({'username': username})
