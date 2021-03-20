from django.db import models


class User(models.Model):
    """ User Model """
    email = models.CharField(max_length=50, unique=True, null=True)
    phone = models.CharField(max_length=50, unique=True, null=True)
    full_name = models.CharField(max_length=50)
    username = models, models.CharField(max_length=50)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
