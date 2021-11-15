from flask_admin.contrib.mongoengine import ModelView

from app.models.commissions import CommissionsPage


class CommissionsPageAdminView(ModelView):
    page_size = 10
