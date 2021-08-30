from flask import current_app
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

from app.models import Settings

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    settings = Settings.objects(environment=current_app.env).first()

    if not settings or not settings.admins:
        return False

    admins = {admin.username: admin.password_hash for admin in settings.admins}

    if username in admins and check_password_hash(admins.get(username), password):
        return username
