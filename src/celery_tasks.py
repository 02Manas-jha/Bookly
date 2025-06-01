from celery import Celery
from src.mail import mail, create_message


c_app = Celery()

c_app.config_from_object('src.config')

@c_app.task()
def send_email():
    pass