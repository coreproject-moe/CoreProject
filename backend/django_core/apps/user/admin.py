from typing import Any

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

USER_MODEL: type[CustomUser] = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    model = USER_MODEL
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = (
        "get_username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )
    list_filter = (
        "ip",
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
                    "discriminator",
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
                    "ip",
                    "email",
                    "avatar",
                    "avatar_provider",
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
    )

    # Needed to invoke forms
    # Hours wasted 0.5
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "discriminator",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    @admin.display(description="username")
    def get_username(
        self,
        obj: CustomUser,
    ) -> CustomUser:
        return obj

    def get_search_results(
        self,
        request: HttpRequest,
        queryset: QuerySet[CustomUser],
        search_term: str,
    ) -> tuple[Any | QuerySet[CustomUser], bool]:
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )

        if search_term:
            search_term_list = [
                # Remove trailing whitespace
                # We might have something like
                # user = ['baseplate-admin ', ' baseplate-foot']
                # make it
                # user = ['baseplate-admin','baseplate-foot']
                item.strip()
                for item in search_term.split(",")
            ]
            queryset = self.model.objects.get_username_with_discriminator().filter(
                Q(username_with_discriminator__in=search_term_list)
                | Q(email__in=search_term_list)
            )

        return queryset, may_have_duplicates


# MoneyPatch
# https://stackoverflow.com/questions/6191662/django-admin-login-form-overriding-max-length-failing
from django.contrib.auth.forms import AuthenticationForm  # noqa

AuthenticationForm.base_fields["username"].label = "Email | Username (with discriminator) "
