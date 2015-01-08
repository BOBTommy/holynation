from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


class UsersManager(BaseUserManager):
    def create_user(self, user_name, email=None, password=None, **kwargs):
        self.validate_kwargs(kwargs)
        self.validate_password(password=password)
        u = User()
        u.user_email = email
        u.user_name = user_name
        u.set_password(raw_password=password)
        u.gender = kwargs['gender']

        u.save()

        return u

    def validate_kwargs(self, kwargs):
        if not "gender" in kwargs:
            raise ValidationError("Gender must be specified.")

    def validate_password(self, password):
        if password is None:
            raise ValidationError("Password must be set.")

class User(AbstractBaseUser):
    MALE = 0
    FEMALE = 1
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=128)
    gender = models.IntegerField(default=MALE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UsersManager()
