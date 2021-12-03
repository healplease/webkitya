from flask import Blueprint

from app.views.portfolio.views import portfolio

portfolio_bp = Blueprint("portfolio", __name__)

portfolio_bp.add_url_rule("/art", "portfolio", portfolio)
