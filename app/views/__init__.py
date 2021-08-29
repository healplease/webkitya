from .main import main_bp
from .admin import admin_bp
from .devonly import devonly_bp

blueprints_to_register = [
    main_bp,
    admin_bp
]

blueprints_to_register_dev_only = [
    devonly_bp
]
