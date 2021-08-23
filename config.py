import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

    IMGUR_CLIENT_ID = os.environ.get("IMGUR_CLIENT_ID")
    IMGUR_CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")
    IMGUR_ALBUM_NAME = os.environ.get("IMGUR_ALBUM_NAME")


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
