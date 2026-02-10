from .models import Lesson, Course
from rest_framework import generics, viewsets
from .serializers import LessonSerializer, CourseSerializer


#Контроллеры для курсов(viewsets)

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

#Контроллеры для уроков(generics)

class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
