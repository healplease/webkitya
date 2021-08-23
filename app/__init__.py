import dotenv
from flask import Flask
# from flask_mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

from config import environment_configs

from app.views import blueprints_to_register

dotenv.load_dotenv()

# mongoengine = MongoEngine()
bootstrap = Bootstrap()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"config.{environment_configs[app.env].__name__}")

    # mongoengine.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)

    for blueprint in blueprints_to_register:
        app.register_blueprint(blueprint)

    return app
