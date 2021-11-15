from flask import Blueprint

from app.views.commissions.views import commissions

commissions_bp = Blueprint("commissions", __name__)

commissions_bp.add_url_rule("/commissions", "commissions", commissions, methods=["GET", "POST"])
