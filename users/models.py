from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
    )

    avatar = models.ImageField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    genter = models.CharField(choices=GENDER_CHOICES,
                              blank=True, max_length=10)
