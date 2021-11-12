from mongoengine import Document, StringField, URLField, BooleanField


class MainPage(Document):
    header = StringField(required=True)
    body = StringField(required=True)
    button_text = StringField(required=True)
    background_image = URLField(required=False)


class SocialMedia(Document):
    active = BooleanField(default=True)
    link = URLField(required=True)
    icon = URLField(required=True)
    name = StringField(required=False)
