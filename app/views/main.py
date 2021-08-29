from flask import Blueprint, current_app, render_template

from app.models import Settings
from app.domain.imgur import get_album_images

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    images = []
    settings = Settings.objects(environment=current_app.env).first()
    album_ids = settings.get_album_ids()
    for album_id in album_ids:
        images.extend(get_album_images(
            album_id=album_id,
            client_id=current_app.config["IMGUR_CLIENT_ID"],
            client_secret=current_app.config["IMGUR_CLIENT_SECRET"]
        ))

    return render_template("index.html", images=images)
