from urllib.parse import urlencode

import dotenv
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from flask_moment import Moment

from config import environment_configs

from app.views import blueprints_to_register, blueprints_to_register_dev_only

dotenv.load_dotenv()

mongoengine = MongoEngine()
bootstrap = Bootstrap()
csrf_protect = CSRFProtect()
moment = Moment()


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"config.{environment_configs[app.env].__name__}")

    # setting DB connection URL
    mongodb_settings = app.config.get_namespace("MONGODB_")
    mongodb_settings["port"] = f":{mongodb_settings.get('port')}" if mongodb_settings.get("port") else ""
    mongodb_settings["arguments"] = (
        f"?{urlencode(mongodb_settings.get('arguments'))}" if mongodb_settings.get("arguments") else ""
    )
    app.config["MONGODB_HOST"] = "{protocol}://{username}:{password}@{host}{port}/{db}{arguments}".format(
        **mongodb_settings
    )

    app.logger.info(f"Connection to database: {mongodb_settings['db']}")

    mongoengine.init_app(app)
    bootstrap.init_app(app)
    csrf_protect.init_app(app)
    moment.init_app(app)

    for blueprint in blueprints_to_register:
        app.register_blueprint(blueprint)

    if app.env == "local":
        for blueprint in blueprints_to_register_dev_only:
            app.register_blueprint(blueprint)

    return app
