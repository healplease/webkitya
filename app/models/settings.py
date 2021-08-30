from datetime import datetime

from werkzeug.security import generate_password_hash
from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    ListField,
    ReferenceField,
    URLField,
    DateTimeField,
    BooleanField
)


class Admin(Document):
    username = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    last_login = DateTimeField(default=datetime.utcnow)
    is_owner = BooleanField(default=False)
    disabled = BooleanField(default=False)

    @classmethod
    def new(cls, username, password):
        return cls.objects.create(username=username, password_hash=generate_password_hash(password))

    @property
    def last_login_timestamp(self):
        return int(self.last_login.timestamp())

    @property
    def as_dict(self):
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "last_login": self.last_login_timestamp,
            "is_owner": self.is_owner,
            "disabled": self.disabled
        }


class SocialMedia(Document):
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
    admins = ListField(ReferenceField(Admin))
    social_medias = ListField(ReferenceField(SocialMedia))
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

    @classmethod
    def get(cls, env):
        return cls.objects(environment=env).first()
