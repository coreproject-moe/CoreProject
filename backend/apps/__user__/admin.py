from pprint import pprint
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = get_user_model()

    list_display = (
        "get_username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "username_discriminator",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "avatar",
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
        (
            _("Important dates"),
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
        (
            _("Customization"),
            {
                "fields": ("video_volume",),
            },
        ),
    )

    @admin.display(description="username")
    def get_username(self, obj, *args, **kwargs):
        # Obj is a reference to user model
        return f"{obj.username}#{str(obj.username_discriminator).zfill(4)}"


admin.site.register(get_user_model(), CustomUserAdmin)
