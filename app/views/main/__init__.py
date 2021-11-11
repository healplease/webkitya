from flask import Blueprint

from app.views.main.views import index

main_bp = Blueprint("main", __name__)

main_bp.add_url_rule("/", "index", index)
