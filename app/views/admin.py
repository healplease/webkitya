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

##################################################################
# albums

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

##################################################################
# social media

@admin_bp.route("/admin/add-media", methods=["POST"])
def admin_add_media():
    SocialMedia.objects.create(link=request.json["link"], icon=request.json["icon"])

    settings = Settings.get(env=current_app.env)
    media_to_add = SocialMedia.objects(link=request.json["link"]).first()

    settings.social_medias.append(media_to_add)
    settings.save()

    return "OK", 200


@admin_bp.route("/admin/delete-media", methods=["POST"])
def admin_delete_media():
    settings = Settings.get(env=current_app.env)

    for media in settings.social_medias:
        if media.link == request.json["link"]:
            settings.social_medias.remove(media)
    settings.save()

    SocialMedia.objects(link=request.json["link"]).delete()
    return "OK", 200


@admin_bp.route("/admin/edit-media", methods=["POST"])
def admin_edit_media():
    SocialMedia.objects(link=request.json["updated"]).update(link=request.json["link"], icon=request.json["icon"])
    return "OK", 200

##################################################################
# admins

@admin_bp.route("/admin/add-admin", methods=["POST"])
def admin_add_admin():
    Admin.new(username=request.json["username"], password=request.json["password"])
    Admin.objects(username=request.json["username"]).update(disabled=bool(request.json["disabled"]))

    settings = Settings.get(env=current_app.env)
    admins_to_add = Admin.objects(username=request.json["username"]).first()

    settings.admins.append(admins_to_add)
    settings.save()

    return "OK", 200


@admin_bp.route("/admin/delete-admin", methods=["POST"])
def admin_delete_admin():
    settings = Settings.get(env=current_app.env)

    for _admin in settings.admins:
        if _admin.username == request.json["username"]:
            settings.admins.remove(_admin)
    settings.save()

    Admin.objects(username=request.json["username"]).delete()
    return "OK", 200


@admin_bp.route("/admin/edit-admin", methods=["POST"])
def admin_edit_admin():
    if request.json.get("old_password") and request.json.get("new_password"):
        Admin.upd(request.json["username"], request.json["old_password"], request.json["new_password"])
    Admin.objects(username=request.json["username"]).update(disabled=bool(request.json["disabled"]))
    return "OK", 200

##################################################################
# cols

@admin_bp.route("/admin/change-cols", methods=["POST"])
def admin_change_cols():
    settings = Settings.get(env=current_app.env)
    settings.cols = int(request.json["cols"])
    settings.save()
    return "OK", 200
