from rest_framework import serializers
from .models import Lesson, Course

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()

    @staticmethod
    def get_count_lessons(obj):
        return obj.lessons_set.count()

    class Meta:
        model = Course
        fields = '__all__'