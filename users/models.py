from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Model """

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
