from typing import Any

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from dynamic_filenames import FilePattern
from mixins.models.created_at import CreatedAtMixin

from .validators import username_validator

avatar = FilePattern(filename_pattern="avatar/{uuid:s}{ext}")


# Create your models here.


class CustomUser(
    AbstractBaseUser,
    PermissionsMixin,
    CreatedAtMixin,
):
    username = models.CharField(
        _("username"),
        unique=True,
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[
            username_validator,
            RegexValidator(
                r"^[a-zA-Z0-9_-]+#[0-9]{4}$",
                message="Username is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`",
            ),
        ],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"),
        blank=False,
        unique=True,
        help_text=_("Required. A valid email with a valid domain"),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    avatar = models.ImageField(
        upload_to=avatar,
        default=None,
        blank=True,
        null=True,
    )
    avatar_provider = models.URLField(
        default="https://seccdn.libravatar.org/avatar/{EMAIL}?s=512"
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    objects = UserManager()

    # Django specific fields
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def save(self, *args: Any, **kwargs: Any) -> None:
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.username)

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        unique_together = [
            ("username", "email"),
        ]
