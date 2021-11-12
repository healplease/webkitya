from flask import url_for
from flask_admin import Admin

from app import admin
from app.admin.main import MainPageAdminView, SocialMediaAdminView
from app.models.main import MainPage, SocialMedia


class Categories:
    MAIN_PAGE = "Main Page"


def admin_init_app(app):
    admin = Admin()
    admin.init_app(app)
    admin.add_view(MainPageAdminView(MainPage, category=Categories.MAIN_PAGE))
    admin.add_view(SocialMediaAdminView(SocialMedia, category=Categories.MAIN_PAGE))
