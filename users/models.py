from django.db import models
from django.contrib.auth.models import User,UserManager


class User(User):
    MALE = 0
    FEMALE = 1
    user_email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=128)
    gender = models.IntegerField(default=MALE)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

