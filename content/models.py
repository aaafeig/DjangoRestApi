from django.conf import settings
from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="название")
    preview = models.ImageField(
        upload_to="content_course/", null=True, blank=True, verbose_name="превью"
    )
    description = models.TextField(verbose_name="описание")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="название")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    preview = models.ImageField(
        upload_to="content_lesson/", null=True, blank=True, verbose_name="превью"
    )
    link_video = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="ссылка"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="курс", related_name="lessons"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
