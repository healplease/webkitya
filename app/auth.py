from flask import current_app, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def protect_admin_views(username: str, password: str):
    if str(request.url_rule).startswith("/admin"): 
        is_username_corrent = username == current_app.config["ADMIN_USERNAME"]
        is_password_correct = check_password_hash(current_app.config["ADMIN_PASSWORD_HASH"], password)
        return username if is_username_corrent and is_password_correct else False
    return True
