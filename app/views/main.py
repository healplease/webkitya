from flask import Blueprint, current_app, render_template

from app.domain.imgur import get_album_images

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    images = get_album_images(
        album_id=current_app.config["IMGUR_ALBUM_NAME"],
        client_id=current_app.config["IMGUR_CLIENT_ID"],
        client_secret=current_app.config["IMGUR_CLIENT_SECRET"]
    )
    return render_template("index.html", images=images)
