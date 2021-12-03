from mongoengine import Document, StringField, URLField, BooleanField, IntField


class PortfolioPage(Document):
    body = StringField(required=False)
    background_image = URLField(required=False)


class PortfolioImage(Document):
    active = BooleanField(default=True)
    url = URLField(required=True)
    thumbnail_url = URLField(required=False)
    name = StringField(required=False)
