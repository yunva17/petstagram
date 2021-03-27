from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ UserAdmin Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            "users",
            {
                "fields": (
                    "name",
                    "photo",
                    "website",
                    "bio",
                    "phone",
                    "gender",
                )
            },
        ),
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )
