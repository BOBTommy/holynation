from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError


class UsersManager(BaseUserManager):
    def create_user(self, user_name, email=None, password=None, **kwargs):
        self.validate_kwargs(kwargs)
        self.validate_password(password=password)
        u = self.model(user_email=email,
                       user_name=user_name,)
        u.set_password(raw_password=password)
        u.gender = kwargs['gender']

        u.save(using=self.db)

        return u

    def create_super_user(self, user_name, email, password, **kwargs):
        super_user = self.create_user(
            user_name=user_name,
            email=email,
            password=password,
            gender=kwargs['gender']
        )
        super_user.is_admin = True

        super_user.save(using=self.db)

        return super_user

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
