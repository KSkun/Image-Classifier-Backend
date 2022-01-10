import json


class BackendConfig:
    """Classifier backend config data class"""

    host: str
    port: int

    image_tmp_dir: str
    image_text_dir: str
    image_nontext_dir: str
    image_url: str

    jwt_secret: str
    jwt_algorithm: str
    jwt_expire: int  # unit: minute

    mongo_addr: str
    mongo_port: int
    mongo_db: str

    redis_addr: str
    redis_port: int
    redis_db: str

    debug: bool


C = BackendConfig()


def load_config(file_path: str):
    file = open(file_path, 'r')
    json_str = file.read()
    file.close()

    json_obj = json.loads(json_str)

    var_list = BackendConfig.__annotations__
    for v in var_list:
        if v in json_obj:
            setattr(C, v, json_obj[v])
        else:
            raise ValueError('missing field %s in config file %s' % (v, file_path))
