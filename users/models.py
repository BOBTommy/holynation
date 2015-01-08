from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


class UsersManager(BaseUserManager):
    def create_user(self, user_name, email=None, password=None, **kwargs):
        self.validate_kwargs(kwargs)

    def validate_kwargs(self, kwargs):
        if not "gender" in kwargs:
            raise ValidationError("Gender must be specified.")


class User(AbstractBaseUser):
    MALE = 0
    FEMALE = 1
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=128)
    gender = models.IntegerField(default=MALE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsersManager()
