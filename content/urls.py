from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonUpdateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
)
from django.urls import path

app_name = "content"

router = DefaultRouter()
router.register(r"content", CourseViewSet, basename="content")
urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path("lessons/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/>", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
] + router.urls
