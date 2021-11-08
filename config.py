import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

    MONGODB_USERNAME = os.environ.get("FLASK_MONGODB_USER")
    MONGODB_PASSWORD = os.environ.get("FLASK_MONGODB_PASSWORD")
    MONGODB_HOST = os.environ.get("FLASK_MONGODB_HOST")
    MONGODB_PORT = os.environ.get("FLASK_MONGODB_PORT")
    MONGODB_DB = "kitya"

    MONGODB_PROTOCOL = "mongodb+srv"
    MONGODB_ARGUMENTS = {"retryWrites": "true", "w": "majority"}


class LocalConfig(Config):
    pass


class HerokuConfig():
    pass


class DevelopmentConfig(HerokuConfig, Config):
    pass


class ProductionConfig(HerokuConfig, Config):
    pass


environment_configs = {
    "local": LocalConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
