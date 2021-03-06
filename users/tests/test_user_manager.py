from django.test import TestCase
from users.models import User
from django.core.exceptions import ValidationError


class TestUserManager(TestCase):
    def setUp(self):
        self.valid_email = "abc@abc.com"
        self.valid_username = "valid_name"
        self.valid_gender = 0
        self.valid_password = "abc123"

    def test_kwargs_must_contain_gender(self):
        self.assertRaises(
            ValidationError,
            User.objects.create_user,
            user_name=self.valid_username,
            email=self.valid_email,
            password=self.valid_password,
            not_gender=self.valid_gender)

    def test_password_must_be_contained(self):
        self.assertRaises(
            ValidationError,
            User.objects.create_user,
            user_name=self.valid_username,
            email=self.valid_email,
            gender=self.valid_gender)

    def test_valid_information_saved_successfully(self):
        self.assertIsNotNone(
            User.objects.create_user(
                user_name=self.valid_username,
                email=self.valid_email,
                password=self.valid_password,
                gender=self.valid_gender,
            )
        )

    def test_super_user_must_is_admin_true(self):
        super_user = User.objects.create_super_user(
            user_name=self.valid_username,
            email=self.valid_email,
            password=self.valid_password,
            gender=self.valid_gender,
        )
        self.assertTrue(super_user.is_admin)