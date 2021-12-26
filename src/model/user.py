from model.main import database

col_user = database['user']


def get_user_by_name(username: str):
    return col_user.find_one({'username': username})
