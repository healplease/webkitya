from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactUsForm(FlaskForm):
    subject = StringField("subject", validators=[DataRequired()])
    contact = EmailField("email")
    body = TextAreaField("body")
    submit = SubmitField()
