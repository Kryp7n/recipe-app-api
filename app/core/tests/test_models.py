"""Test for Models"""

from django.test import TestCase;
from django.contrib.auth import get_user_model;

class ModelTests(TestCase):
    """Test Models"""
    
    def test_create_user_with_email_successful(self):
        """Test user creation with email is successful"""
        email = "testuser@example.com"
        password = "Test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@Example.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.Com', 'test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password="sample123"
            )

            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','sample123')

    
    def test_create_super_user(self):
        """Test super user creation"""
        user = get_user_model().objects.create_superuser(
            'superuser',
            'password123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)