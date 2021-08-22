import os


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")


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
