from flask_mail import Message

from app import mail

def send_mail(contact: str, subject: str, body: str):
    try:
        msg = Message()
        msg.subject = f"[Commission] {subject}"
        msg.body = f"From: {contact}\n\n{body}"
        msg.add_recipient("gavaalex2012@gmail.com")
        msg.sender = ("Portfolio", "noreply@kitya.com")
        mail.send(msg)
    except Exception:  # don't raise an exception on fail email send
        return False
    return True
