import logging
import os

from flask import Flask

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('image-classifier-backend')
logger.info('starting Image Classifier Backend by KSkun')

app = Flask(__name__)

from config import load_config

config_file = os.getenv('CONFIG_FILE', default='default.json')
load_config(config_file)
logger.info('config file %s loaded' % config_file)

from controller.main import main_bp, init_controller

init_controller()
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run()
