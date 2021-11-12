from flask_admin.contrib.mongoengine import ModelView

from app.models.main import MainPage, SocialMedia


class MainPageAdminView(ModelView):
    page_size = 10


class SocialMediaAdminView(ModelView):
    column_list = ("active", "link", "icon", "name", )
    column_sortable_list = ("active", )
    page_size = 10
