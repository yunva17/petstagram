from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    """ User Model """
    GENDER_CHOICES = (
        ('m', "Male"),
        ('F', "Female"),
        ('C', "Custom"),
    )

    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    gender = models.CharField(
        blank=True, choices=GENDER_CHOICES, max_length=255)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
