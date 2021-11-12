from flask_admin.contrib.mongoengine import ModelView

from app.models.main import MainPage, SocialMedia


class MainPageAdminView(ModelView):
    page_size = 10


class SocialMediaAdminView(ModelView):
    page_size = 10
