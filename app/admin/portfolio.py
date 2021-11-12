from flask_admin.contrib.mongoengine import ModelView

from app.models.portfolio import PortfolioImage, PortfolioPage


class PortfolioPageAdminView(ModelView):
    page_size = 10


class PortfolioImageAdminView(ModelView):
    page_size = 50
