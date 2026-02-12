from rest_framework import serializers
from .models import Lesson, Course
from .validators import LinkValidator

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='link_video')]


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    @staticmethod
    def get_count_lessons(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
