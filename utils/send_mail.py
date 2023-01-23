import os
from flask_mail import Message
from config.extensions import mail


def send_mail(to_whom, subject, template):
    msg = Message(
        subject,
        sender=os.environ.get("MAIL_USERNAME"),
        recipients=[to_whom],
    )
    msg.body = template
    mail.send(msg)
