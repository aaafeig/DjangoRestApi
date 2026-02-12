from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Subscription
from content.models import Course
class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="user@test.com",
            password="123456"
        )

        self.course = Course.objects.create(
            title="Test course",
            description="Desc",
            owner=self.user
        )

        self.url = "/users/subscribe/"

    def test_subscribe_create(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.post(self.url, {"course_id": self.course.pk})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertTrue(
            Subscription.objects.filter(user=self.user, course=self.course).exists()
        )

    def test_subscribe_delete(self):
        self.client.force_authenticate(user=self.user)

        self.client.post(self.url, {"course_id": self.course.pk})

        response = self.client.post(self.url, {"course_id": self.course.pk})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.count(), 0)

    def test_subscribe_unauthorized(self):
        response = self.client.post(self.url, {"course_id": self.course.id})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
