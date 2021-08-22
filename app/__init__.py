from flask import Flask
import dotenv

from config import environment_configs
from flask_mongoengine import MongoEngine

from app.views import blueprints_to_register

dotenv.load_dotenv()

mongoengine = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(f"config.{environment_configs[app.env].__name__}")

    mongoengine.init_app(app)

    for blueprint in blueprints_to_register:
        app.register_blueprint(blueprint)

    return app
