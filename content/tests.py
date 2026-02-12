from rest_framework import status
from rest_framework.test import APITestCase

from content.models import Lesson, Course
from users.models import User

class LessonCRUDTestCase(APITestCase):

    """ Тестирование CRUD уроков """

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            email="user@test.com",
            password="123456"
        )

        self.other_user = User.objects.create_user(
            username="test2",
            email="other@test.com",
            password="123456"
        )

        self.course = Course.objects.create(
            title="Test course",
            description="Desc",
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title="Lesson 1",
            description="Desc",
            owner=self.user,
            course=self.course
        )

    def test_lesson_create(self):

        """ Тестирование создания обьекта """

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "New lesson",
            "description": "Desc",
            "course": self.course.pk
        }

        response = self.client.post("/content/lesson/create/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_update(self):

        """Тестирование обновления обьекта"""

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f"/content/lesson/update/{self.lesson.pk}/",
            {"title": "Updated"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):

        """Тетсирование удаления обьекта"""

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f"/content/lesson/delete/{self.lesson.pk}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_read(self):

        """ Тестирование чтения обьекта"""

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            f"/content/lesson/{self.lesson.pk}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete_not_owner(self):
        self.client.force_authenticate(user=self.other_user)

        response = self.client.delete(
            f"/content/lesson/delete/{self.lesson.pk}/"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_lesson_update_not_owner(self):
        self.client.force_authenticate(user=self.other_user)

        response = self.client.patch(
            f"/content/lesson/update/{self.lesson.pk}/",
            {"title": "Hack"}
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
