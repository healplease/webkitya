from datetime import datetime

from werkzeug.security import generate_password_hash
from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    ListField,
    EmbeddedDocumentListField,
    URLField,
    DateTimeField,
    BooleanField
)


class Admin(EmbeddedDocument):
    login = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    last_loggen_in = DateTimeField(default=datetime.utcnow)
    is_owner = BooleanField(default=False)

    @classmethod
    def new(cls, username, password):
        return cls(login=username, password_hash=generate_password_hash(password))

    @property
    def as_dict(self):
        return {
            "login": self.login,
            "password_hash": self.password_hash,
            "last_logged_in": self.last_loggen_in,
            "is_owner": self.is_owner
        }


class SocialMedia(EmbeddedDocument):
    icon = URLField()
    link = URLField()

    @property
    def as_dict(self):
        return {
            "icon": self.icon,
            "link": self.link
        }


class Settings(Document):
    environment = StringField(required=True, unique=True)
    admins = EmbeddedDocumentListField(Admin)
    social_medias = EmbeddedDocumentListField(SocialMedia)
    albums = ListField(URLField())

    def get_album_ids(self):
        return [x.strip("/").split("/")[-1] for x in self.albums]

    @property
    def as_dict(self):
        return {
            "environment": self.environment,
            "admins": [x.as_dict for x in self.admins],
            "social_medias": [x.as_dict for x in self.social_medias],
            "albums": self.albums
        }
