from rest_framework import generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Course
from .models import Payments, Subscription
from .serializers import PaymentsSerializer, UserSerializer


# контроллер платежей
class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = DjangoFilterBackend
    filterset_fields = ("payment_date", "course", "lesson", "payment_method")


# контроллер пользователей

class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#контроллер для подписки

class SubscribeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        user = request.user
        course_id = request.data.get("course_id")

        course = get_object_or_404(Course, id=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            Subscription.objects.create(user=user, course=course)
            message = "Подписка добавлена"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
