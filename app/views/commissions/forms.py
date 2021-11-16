from flask import request

from flask_wtf import FlaskForm
from flask_wtf.file import FileSize, FileField
from wtforms import StringField, EmailField, SubmitField, TextAreaField, MultipleFileField, Form, Field, ValidationError
from wtforms.validators import DataRequired


class ContactUsForm(FlaskForm):
    subject = StringField("subject", validators=[DataRequired()])
    contact = EmailField("email", validators=[DataRequired()])
    body = TextAreaField("body", validators=[DataRequired()])
    references = FileField('Upload your references', validators=[FileSize(2 * 1024 * 1024)])
    submit = SubmitField()
