from flask import Flask
import dotenv

from config import environment_configs

dotenv.load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"config.{environment_configs[app.env].__name__}")

    return app
