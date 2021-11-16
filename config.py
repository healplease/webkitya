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

    ADMIN_USERNAME = os.environ.get("FLASK_ADMIN_USERNAME")
    ADMIN_PASSWORD_HASH = os.environ.get("FLASK_ADMIN_PASSWORD_HASH")

    MAIL_SERVER = os.environ.get("FLASK_MAIL_SERVER")
    MAIL_PORT = os.environ.get("FLASK_MAIL_PORT")
    MAIL_USERNAME = os.environ.get("FLASK_MAIL_USERNAME")
    MAIL_PASSWORD =os.environ.get("FLASK_MAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class LocalConfig(Config):
    DEBUG = True


class HerokuConfig():
    DEBUG = False


class DevelopmentConfig(HerokuConfig, Config):
    MONGODB_DB = "kitya_dev"


class ProductionConfig(HerokuConfig, Config):
    MONGODB_DB = "kitya_prod"


environment_configs = {
    "local": LocalConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
