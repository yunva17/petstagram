from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):
    """ UserAdmin Admin """

    fieldsets = UserAdmin.fieldsets+(
        ("users", {
            "fields": (
                "avatar",
                "bio",
                "genter",

            ),
        }),
    )

    list_display = ("username",
                    "email",
                    "phone",
                    "is_active",
                    "is_staff",
                    "is_superuser"
                    )
