from mongoengine import Document, StringField, URLField, BooleanField


class CommissionsPage(Document):
    body = StringField(required=True)
    background_image = URLField(required=False)
