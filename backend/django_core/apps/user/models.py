from pathlib import Path
from typing import Self, Any, NoReturn
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager
from .validators import username_validator


class FileField:
    # Thanks Stackoverflow
    # https://stackoverflow.com/questions/1190697/django-filefield-with-upload-to-determined-at-runtime
    @staticmethod
    def avatar(*args, **kwargs) -> Path:
        return Path("avatar", str(uuid.uuid4()))


# Create your models here.


class CustomUser(
    AbstractBaseUser,
    PermissionsMixin,
):
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(
        _("email address"),
        blank=True,
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
    username_discriminator = models.BigIntegerField(
        blank=True,
        null=True,
        help_text=(
            "Optional. "
            f"{settings.USERNAME_DISCRIMINATOR_LENGTH} characters or fewer. "
            "If not provided a random `username_discriminator` will be selected."
        ),
        validators=[
            MaxValueValidator(int(9 * settings.USERNAME_DISCRIMINATOR_LENGTH)),
            MinValueValidator(1),  # Same thing but remove negative digits
        ],
    )
    avatar = models.ImageField(
        upload_to=FileField.avatar,
        default=None,
        blank=True,
        null=True,
    )
    avatar_provider = models.URLField(
        default="https://seccdn.libravatar.org/avatar/{EMAIL}?s=512"
    )

    ip = models.GenericIPAddressField(null=True, blank=True)
    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "username_discriminator",
    ]

    def get_username_with_discriminator(self) -> str:
        return f"""{
                self
                .username
            }#{
                str(
                    self
                    .username_discriminator
                )
                .zfill(
                    settings.USERNAME_DISCRIMINATOR_LENGTH
                )
            }"""

    def save(self: Self, *args: tuple, **kwargs: dict[str, Any]) -> NoReturn:
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.get_username_with_discriminator()

    class Meta:
        db_table = "user"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        unique_together = [
            ("username", "username_discriminator"),
        ]


class Token(models.Model):
    token = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_token"
        verbose_name = _("token")
        verbose_name_plural = _("tokens")
