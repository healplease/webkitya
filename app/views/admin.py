from flask import Blueprint, current_app, render_template

from app.auth import auth

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@auth.login_required
def admin():
    return f"Hello, {auth.current_user()}"
