from flask import Flask
from loader.views import loader
from main.views import main
import config_logger

def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(loader)
    app.register_blueprint(main)
    # app.register_blueprint(bp_api, url_prefix='/api')
    # app.config.from_pyfile(config_path)
    config_logger.config()
    return app

app = create_and_config_app('config.py')

app.run()