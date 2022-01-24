import random
from celery import shared_task
from django.core.mail import send_mail
from cario import settings


@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)


@shared_task(name="send_email_to")
def send_email_to(to_email, email_title, email_message):

    title = email_title
    message = str(email_message)
    mail_sent = send_mail(title, message, settings.EMAIL_HOST_USER, [to_email, ])
    return mail_sent
