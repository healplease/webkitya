from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    ListField,
    ReferenceField,
    URLField,
    DateTimeField,
    BooleanField,
    IntField
)


class Admin(Document):
    username = StringField(required=True, unique=True)
    password_hash = StringField(required=True)
    last_login = DateTimeField(default=datetime.utcnow)
    is_owner = BooleanField(default=False)
    disabled = BooleanField(default=False)

    @classmethod
    def new(cls, username, password):
        password_hash = generate_password_hash(password)
        return cls.objects.create(username=username, password_hash=password_hash)

    @classmethod
    def upd(cls, username, old_password, new_password):
        if check_password_hash(self.password_hash, old_password):
            new_password_hash = generate_password_hash(new_password)
            return cls.objects(username=username).update(password_hash=new_password_hash)
        return False
        

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


class Album(Document):
    link_or_album_id = StringField(required=True)
    album_id = StringField(unique=True)
    permalink = URLField()

    @classmethod
    def new(cls, link_or_album_id):
        album_id = link_or_album_id.strip("/").split("/")[-1]
        permalink = f"https://imgur.com/a/{album_id}"
        return cls.objects.create(link_or_album_id=link_or_album_id, album_id=album_id, permalink=permalink)

    @classmethod
    def upd(cls, old_album_id, link_or_album_id):
        album_id = link_or_album_id.strip("/").split("/")[-1]
        permalink = f"https://imgur.com/a/{album_id}"
        return cls.objects(album_id=old_album_id).update(
            link_or_album_id=link_or_album_id,
            album_id=album_id,
            permalink=permalink
        )

    @property
    def as_dict(self):
        return {
            "link_or_album_id": self.link_or_album_id,
            "album_id": self.album_id,
            "permalink": self.permalink
        }


class Settings(Document):
    environment = StringField(required=True, unique=True)
    cols = IntField(min_value=1, max_value=12, choices=(1, 2, 3, 4, 6, 12), default=4)
    admins = ListField(ReferenceField(Admin))
    social_medias = ListField(ReferenceField(SocialMedia))
    albums = ListField(ReferenceField(Album))

    @property
    def as_dict(self):
        return {
            "environment": self.environment,
            "cols": self.cols,
            "admins": [x.as_dict for x in self.admins],
            "social_medias": [x.as_dict for x in self.social_medias],
            "albums": [x.as_dict for x in self.albums]
        }

    @classmethod
    def get(cls, env):
        return cls.objects(environment=env).first()
