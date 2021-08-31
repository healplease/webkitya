from flask import current_app
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from app.models import Settings

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    settings = Settings.get(env=current_app.env)

    if not settings or not settings.admins:
        return False

    for admin in settings.admins:
        if check_password_hash(admin.password_hash, password) and not admin.disabled:
            return username
