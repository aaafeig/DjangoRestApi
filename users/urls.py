from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserRegisterAPIView, SubscribeAPIView

app_name = "users"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("subscribe/", SubscribeAPIView.as_view(), name="subscribe"),
]
