from typing import TYPE_CHECKING, Any

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.conf import settings
from django.db.models.query import QuerySet

if TYPE_CHECKING:
    from .models import CustomUser


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self,
        email: str,
        password: str,
        **extra_fields: Any,
    ) -> "CustomUser":
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user: CustomUser = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        **extra_fields: Any,
    ) -> "CustomUser":
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

    def get_username_with_discriminator(self) -> QuerySet["CustomUser"]:
        return self.annotate(
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
        )
