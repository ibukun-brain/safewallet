from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "uid",
                    "email",
                    "mobile_no",
                    "gender",
                    "date_of_birth",
                    "profile_pic",
                    "verified",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "first_name", "last_name",
                "email", "mobile_no",
                "password1", "password2"), },), )
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        'date_joined',
        'last_login',
        "is_superuser",
        'is_staff',
        'verified'
    ]
    ordering = ("first_name", "last_name",)
    list_display_links = ["first_name", "email"]
    list_filter = ["date_joined", "gender", "verified"]
    readonly_fields = ['uid']
