from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(models.Admin):
    """ UserAdmin Admin """
    pass
