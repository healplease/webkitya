import traceback

from flask import current_app, request
from flask_mail import Message, Attachment
from wtforms import MultipleFileField

from app import mail

def send_mail(contact: str, subject: str, body: str):
    msg = Message()
    msg.subject = f"[Commission] {subject}"
    msg.body = f"From: {contact}\n\n{body}"
    msg.add_recipient("gavaalex2012@gmail.com")
    msg.sender = ("Portfolio", "noreply@kitya.com")

    for file in request.files.getlist("references"):
        msg.attach(file.filename, file.headers.get("Content-Type", "image/jpeg"), file.stream.read())

    mail.send(msg)
