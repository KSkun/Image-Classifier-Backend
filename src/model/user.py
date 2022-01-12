from model.main import mongo_db

_col_user = mongo_db['user']


def find_user_by_name(username: str):
    """
    Find user by username

    :param username: user's username
    :return: user document
    """
    return _col_user.find_one({'username': username})
