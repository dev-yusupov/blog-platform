from django.test import TestCase
from django.contrib.auth import get_user_model

class TestUserModel(TestCase):
    """Tests which tests user model."""

    def test_create_user_object_with_username_successful(self):
        """Test creates a new user with email and password successfully."""
        user = get_user_model().objects.create_user(username="testuser", password="1234test")

        self.assertEqual(str(user), "testuser")
        self.assertTrue(get_user_model().objects.filter(username="testuser").exists())
    
    def test_create_superuser(self):
        """Test creates a new superuser."""
        superuser = get_user_model().objects.create_superuser(username="adminuser", password="1234test")

        self.assertEqual(str(superuser), "adminuser")
        self.assertTrue(superuser.check_password("1234test"))
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
    
    def test_create_new_user_return_error_without_username(self):
        """Test creates a new user without username and it will raise error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username = "", password="1234test")
    
    def test_create_new_user_return_error_without_password(self):
        """Test creates a new user without password and it will raise error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(username="admin", password="")
    