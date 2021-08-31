from datetime import datetime

from flask import Blueprint, current_app, render_template, request, redirect, url_for

from app.auth import auth
from app.models import Settings, Admin, SocialMedia, Album

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin", methods=["GET"])
@auth.login_required
def admin():
    Admin.objects(username=auth.current_user()).update(last_login=datetime.utcnow())
    current_user = Admin.objects(username=auth.current_user()).first()
    settings = Settings.get(env=current_app.env)
    return render_template("admin.html", settings=settings, current_user=current_user)


@admin_bp.route("/admin/add-album", methods=["POST"])
def admin_add_album():
    Album.new(link_or_album_id=request.json["link_or_album_id"])

    settings = Settings.get(env=current_app.env)
    album_to_add = Album.objects(link_or_album_id=request.json["link_or_album_id"]).first()

    settings.albums.append(album_to_add)
    settings.save()

    return "OK", 200

@admin_bp.route("/admin/delete-album", methods=["POST"])
def admin_delete_album():
    settings = Settings.get(env=current_app.env)

    for album in settings.albums:
        if album.album_id == request.json["album_id"]:
            settings.albums.remove(album)
    settings.save()

    Album.objects(album_id=request.json["album_id"]).delete()
    return "OK", 200

@admin_bp.route("/admin/edit-album", methods=["POST"])
def admin_edit_album():
    Album.upd(old_album_id=request.json["album_id"], link_or_album_id=request.json["link_or_album_id"])
    return "OK", 200
