from typing import TYPE_CHECKING, Any, Self

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.utils.translation import gettext_lazy as _
from typing import Self

if TYPE_CHECKING:
    from .models import CustomUser


class UsernameWithDiscriminatorManager(models.Manager):
    def get_username_with_discriminator(
        self: Self,
        prefix: str = "",
    ) -> "UsernameWithDiscriminatorManager":
        prefix = prefix + "__" if prefix else ""
        return self.annotate(
            username_discriminator_as_string=Cast(
                f"{prefix}username_discriminator", output_field=CharField()
            ),
            username_with_discriminator=Concat(
                f"{prefix}username",
                Value("#"),
                LPad(
                    "username_discriminator_as_string",
                    int(settings.USERNAME_DISCRIMINATOR_LENGTH),
                    Value("0"),
                ),
                output_field=CharField(),
            ),
        )


class UserManager(BaseUserManager, UsernameWithDiscriminatorManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self: Self,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
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
        self: Self,
        email: str,
        password: str,
        **extra_fields: dict[str, Any],
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
