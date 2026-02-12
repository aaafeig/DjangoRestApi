from rest_framework import serializers

from users.models import Subscription
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
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if not user.is_authenticated:
            return False

        return Subscription.objects.filter(user=user, course=obj).exists()

    @staticmethod
    def get_count_lessons(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
