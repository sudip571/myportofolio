
from .. import app, mail, db
from flask_mail import Message
from threading import Thread


def send_emails(subject,sender,recipients,text_body,html_body):
    msg=Message(subject=subject,sender=sender,recipients=recipients)
    msg.body = text_body
    msg.html = html_body    
    thr = Thread(target=send_async_email, args=[app,msg])
    thr.start()

def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)