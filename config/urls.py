
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include('content.urls', namespace='content')),
    path('users/', include('users.urls', namespace='users')),
]
