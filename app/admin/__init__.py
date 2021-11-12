from flask import url_for
from flask_admin import Admin

from app import admin
from app.admin.main import MainPageAdminView, SocialMediaAdminView
from app.admin.portfolio import PortfolioImageAdminView, PortfolioPageAdminView
from app.models.main import MainPage, SocialMedia
from app.models.portfolio import PortfolioImage, PortfolioPage


class Categories:
    PAGES = "Pages"
    MAIN_PAGE = "Main page"
    PORTFOLIO = "Portfolio"


def admin_init_app(app):
    admin = Admin()
    admin.init_app(app)
    views = (
        MainPageAdminView(MainPage, category=Categories.PAGES, name="Home page"),
        PortfolioPageAdminView(PortfolioPage, category=Categories.PAGES, name="Portfolio"),
        SocialMediaAdminView(SocialMedia, category=Categories.MAIN_PAGE, name="Social media"),
        PortfolioImageAdminView(PortfolioImage, category=Categories.PORTFOLIO, name="Images"),
    )

    for view in views:
        admin.add_view(view)

    return admin
