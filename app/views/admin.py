from datetime import datetime

from flask import Blueprint, current_app, render_template, request, redirect

from app.auth import auth
from app.models import Settings, Admin, SocialMedia

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin", methods=["GET", "POST"])
@auth.login_required
def admin():
    Admin.objects(username=auth.current_user()).update(last_login=datetime.utcnow())
    current_user = Admin.objects(username=auth.current_user()).first()
    settings = Settings.get(env=current_app.env)
    return render_template("admin.html", settings=settings, current_user=current_user)
