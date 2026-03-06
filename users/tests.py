from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Subscription
from content.models import Course
from django.test import TestCase
from unittest.mock import patch

from content.services import (
    create_stripe_product,
    create_stripe_price,
    create_stripe_session
)

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



class StripeServiceTestCase(TestCase):

    @patch("content.services.stripe.Product.create")
    def test_create_stripe_product(self, mock_product_create):
        """Тест создания продукта в Stripe"""

        mock_product_create.return_value = {"id": "prod_test123"}

        product_id = create_stripe_product("Test Course")

        self.assertEqual(product_id, "prod_test123")
        mock_product_create.assert_called_once_with(name="Test Course")

    @patch("content.services.stripe.Price.create")
    def test_create_stripe_price(self, mock_price_create):
        """Тест создания цены в Stripe"""

        mock_price_create.return_value = {"id": "price_test123"}

        price_id = create_stripe_price("prod_test123", 100)

        self.assertEqual(price_id, "price_test123")
        mock_price_create.assert_called_once_with(
            unit_amount=100 * 100,
            currency="usd",
            product="prod_test123",
        )

    @patch("content.services.stripe.checkout.Session.create")
    def test_create_stripe_session(self, mock_session_create):
        """Тест создания checkout-сессии"""

        mock_session_create.return_value = {"url": "https://test-session-url.com"}

        session_url = create_stripe_session("price_test123")

        self.assertEqual(session_url, "https://test-session-url.com")

        mock_session_create.assert_called_once_with(
            payment_method_types=["card"],
            line_items=[{
                "price": "price_test123",
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
