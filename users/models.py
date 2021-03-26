from django.db import models


class User(models.Model):
    """ User Model """

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True, unique=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    password = models.CharField(max_length=300, editable=True)
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
