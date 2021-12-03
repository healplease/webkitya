from flask import url_for
from flask_admin import Admin

from app import admin
from app.admin.main import MainPageAdminView, SocialMediaAdminView
from app.admin.portfolio import PortfolioImageAdminView, PortfolioPageAdminView
from app.admin.commissions import CommissionsPageAdminView
from app.models.main import MainPage, SocialMedia
from app.models.portfolio import PortfolioImage, PortfolioPage
from app.models.commissions import CommissionsPage

admin = Admin()


class Categories:
    PAGES = "Pages"
    MAIN_PAGE = "Main page"
    PORTFOLIO = "Portfolio"


def admin_init_app(app):
    admin.init_app(app)
    views = (
        MainPageAdminView(MainPage, category=Categories.PAGES, name="Home page"),
        PortfolioPageAdminView(PortfolioPage, category=Categories.PAGES, name="Portfolio"),
        CommissionsPageAdminView(CommissionsPage, category=Categories.PAGES, name="Commissions"),
        SocialMediaAdminView(SocialMedia, category=Categories.MAIN_PAGE, name="Social media"),
        PortfolioImageAdminView(PortfolioImage, category=Categories.PORTFOLIO, name="Images"),
    )

    for view in views:
        admin.add_view(view)

    return admin
