from flask import Blueprint, current_app, render_template, redirect

from app.models import Settings, Admin, SocialMedia, Album

devonly_bp = Blueprint("devonly", __name__)


@devonly_bp.route("/settings")
def create_settings_if_not_exist():
    settings = Settings.get(env=current_app.env)
    if not Admin.objects():
        Admin.new("admin", "admin")
    if not SocialMedia.objects():
        SocialMedia.objects.create(
            icon="https://www.freepngimg.com/download/logo/69768-logo-computer-layout-instagram-icons-png-file-hd.png",
            link="https://www.instagram.com/stas_asket")
    if not Album.objects():
        Album.new("https://imgur.com/a/Ou009UG")
    if not settings:
        settings = Settings.objects.create(
            environment=current_app.env,
            admins=[x for x in Admin.objects()],
            social_medias=[x for x in SocialMedia.objects()],
            albums=[x for x in Album.objects()],
        )
    return Settings.get(env=current_app.env).as_dict
