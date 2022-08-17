from django.conf import settings
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.utils.translation import gettext_lazy as _



class UserAdmin(DjangoUserAdmin):
    model = get_user_model()

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
                    "ip",
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
        # (
        #     _("Customization"),
        #     {
        #
        #     },
        # ),
    )

    @admin.display(description="username")
    def get_username(self, obj, *args, **kwargs):
        print(CustomUserAdmin.form)
        return obj

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )

        if search_term:
            queryset = self.model.objects.annotate(
                username_discriminator_as_string=Cast(
                    "username_discriminator", output_field=CharField()
                ),
                username_with_discriminator=Concat(
                    "username",
                    Value("#"),
                    LPad(
                        "username_discriminator_as_string",
                        int(settings.USERNAME_DISCRIMINATOR_LENGTH),
                        Value("0"),
                    ),
                    output_field=CharField(),
                ),
            ).filter(username_with_discriminator__in=search_term.split(","))

        return queryset, may_have_duplicates


admin.site.register(get_user_model(), UserAdmin)
