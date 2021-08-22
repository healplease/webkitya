from flask import Blueprint

from app.models.painting import Painting

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    Painting.objects.create(name="Image " + str(Painting.objects.all().count()))
    paintings = Painting.objects.all()
    return ", ".join(x.name for x in paintings)
