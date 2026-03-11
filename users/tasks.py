from celery import shared_task
from django.core.mail import send_mail

from config import settings
from django.utils import timezone
from datetime import timedelta

from users.models import User


@shared_task
def send_update_email(user_email, course_name):
    subject = "Новый материал в курсе!"
    message = f"Здравствуйте, в курсе {course_name} появился новый материал!"

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
        )
    except Exception as e:
        print(f"Ошибка отправки email: {e}")


@shared_task
def block_inactive_users():

    month_ago = timezone.now() - timedelta(days=30)

    users = User.objects.filter(last_login__lt=month_ago, is_active=True)

    users.update(is_active=False)