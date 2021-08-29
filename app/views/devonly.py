from flask import Blueprint, current_app, render_template, redirect

from app.models import Settings, Admin

devonly_bp = Blueprint("devonly", __name__)


@devonly_bp.route("/settings")
def create_settings_if_not_exist():
    settings = Settings.objects(environment=current_app.env).first()
    if not settings:
        settings = Settings.objects.create(
            environment=current_app.env,
            admins=[Admin.new("admin", "admin")],
            social_medias=[],
            albums=[],
        )
    return Settings.objects(environment=current_app.env).first().as_dict
