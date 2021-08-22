import mongoengine as me

class Painting(me.Document):
    name = me.StringField()
