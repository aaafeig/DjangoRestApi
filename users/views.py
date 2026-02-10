from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payments, User
from .serializers import PaymentsSerializer, UserSerializer


#контроллер платежей
class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('payment_date', 'course', 'lesson', 'payment_method')

#контроллер пользователей

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
