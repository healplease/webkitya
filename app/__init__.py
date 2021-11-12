from urllib.parse import urlencode

import dotenv
import flask_bootstrap
from flask import Flask, request
from flask_mongoengine import MongoEngine
from flask_wtf import CSRFProtect
from flask_moment import Moment

from app.auth import auth
from config import environment_configs

dotenv.load_dotenv()

# bootstrap 4.2.1 supports spinners
flask_bootstrap.BOOTSTRAP_VERSION = "4.2.1"
flask_bootstrap.POPPER_VERSION = "1.14.6"
flask_bootstrap.JQUERY_VERSION = "3.6.0"

mongoengine = MongoEngine()
bootstrap = flask_bootstrap.Bootstrap()
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

    bootstrap.init_app(app)
    mongoengine.init_app(app)
    csrf_protect.init_app(app)
    moment.init_app(app)

    from app.admin import admin_init_app
    admin = admin_init_app(app)

    @app.before_request
    @auth.login_required
    def protect_admin_views():
        pass

    from app.views.main import main_bp
    from app.views.portfolio import portfolio_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(portfolio_bp)

    return app
