import traceback

from flask import current_app, request
from flask_mail import Message, Attachment
from wtforms import MultipleFileField
from werkzeug.formparser import FileStorage

from app import mail

def send_mail(contact: str, subject: str, body: str, files: list[FileStorage]):
    msg = Message()
    msg.subject = f"[Commission] {subject}"
    msg.body = f"From: {contact}\n\n{body}"
    for recipient in current_app.config.get("MAIL_RECIPIENTS", "").split(","):
        msg.add_recipient(recipient)
    msg.sender = ("Portfolio", current_app.config["MAIL_USERNAME"])

    for file in files:
        msg.attach(file.filename, file.headers.get("Content-Type", "image/jpeg"), file.stream.read())

    mail.send(msg)
