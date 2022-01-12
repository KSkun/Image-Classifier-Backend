import logging
import os

from flask import Flask
from flask_cors import CORS

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('image-classifier-backend')
logger.info('starting Image Classifier Backend by KSkun')

# create flask instance
app = Flask(__name__)
CORS(app, supports_credentials=True)

# load config
from config import load_config, C

config_file = 'config/' + os.getenv('CONFIG_FILE', default='default.json')
load_config(config_file)
logger.info('config file %s loaded' % config_file)

# init model
from model.init import init_model

init_model()

# init controller
from controller.main import main_bp, init_controller

init_controller()
app.register_blueprint(main_bp)

# run flask
if __name__ == '__main__':
    app.run(host=C.host, port=C.port)
