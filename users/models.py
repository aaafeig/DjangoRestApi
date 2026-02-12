from django.contrib.auth.models import AbstractUser
from django.db import models
from content.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    username = None

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
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField()
    paid_method = models.CharField(max_length=10, choices=PAYMENTS_METHOD_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.date} - {self.amount} - {self.paid_method}"

    class Meta:
        verbose_name = "payment"
        verbose_name_plural = "payments"
        ordering = ("-date",)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
        ordering = ['user', 'course']

