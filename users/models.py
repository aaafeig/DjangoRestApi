from django.contrib.auth.models import AbstractUser
from django.db import models
from content.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, verbose_name="имя пользователя", default="", max_length=20)

    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    image_user = models.ImageField(upload_to="user_image/", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payments(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"

    PAYMENTS_METHOD_CHOICES = ((CASH, "наличные"), (TRANSFER, "перевод"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=10, choices=PAYMENTS_METHOD_CHOICES)
    stripe_session_id = models.CharField(max_length=255, null=True, blank=True)
    payment_url = models.URLField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.created_at} - {self.amount} - {self.payment_method}"

    class Meta:
        verbose_name = "payment"
        verbose_name_plural = "payments"
        ordering = ("-created_at",)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ['user', 'course']

