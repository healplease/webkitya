import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

    MONGODB_DB = "kitya-dev"
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = os.environ.get("FLASK_MONGODB_USERNAME")
    MONGODB_PASSWORD = os.environ.get("FLASK_MONGODB_PASSWORD")


class LocalConfig(Config):
    pass


class HerokuConfig():
    pass


class DevelopmentConfig(HerokuConfig, Config):
    pass


class ProductionConfig(HerokuConfig, Config):
    MONGODB_DB = "kitya-prod"


environment_configs = {
    "local": LocalConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
