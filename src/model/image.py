from bson import ObjectId

from model.main import mongo_db

_col_image = mongo_db['image']


def find_image_list_by_task(task_id: ObjectId):
    """
    Find images by task ObjectId

    :arg task_id: task ObjectId
    :return: list of images
    """
    return list(_col_image.find({'task_id': task_id}))
