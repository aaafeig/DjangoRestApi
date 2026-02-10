from rest_framework import generics, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payments
from .serializers import PaymentsSerializer



class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('payment_date', 'course', 'lesson', 'payment_method')
