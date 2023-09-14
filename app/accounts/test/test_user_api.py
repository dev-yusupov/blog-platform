from django.test import TestCase

from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("accounts:registeration")
TOKEN_URL = reverse("accounts:login")
USER_PROFILE_URL = reverse("accounts:profile")

def create_user(**params):
    """Create a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test cases for unauthorized users."""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_user_succesfull(self):
        """Test creates a new user."""
        payload = {
            "email": "test@test.com",
            "password": "1234test",
            "username": "test_user",
            "first_name": "Test",
            "last_name": "Testov"
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(username=payload["username"])

        self.assertEqual(user.first_name, payload["first_name"])
        self.assertEqual(user.last_name, payload["last_name"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", response.data)
    
    