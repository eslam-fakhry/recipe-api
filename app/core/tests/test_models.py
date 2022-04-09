from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test description"""
        email = "user@example.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """test user email get lowercased after registering"""

        email = "User@eXample.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_user_email_validated(self):
        """test user email is validated"""

        email = ""  # invalid email
        password = "Testpass123"

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_superuser(self):
        """Test super user is created succussfully"""
        email = "user@example.com"
        password = "Testpass123"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
