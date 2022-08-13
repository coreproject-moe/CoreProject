from django.conf import settings

# @todo
# Modify it with AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from .mixins.resize import ResizeImageMixin
from .validators import username_validator

# Create your models here.


class User(AbstractUser, ResizeImageMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # We dont want unique usernames
        # We also (don't) want unique emails | Hours wasted : 0.1
        self._meta.get_field("username")._unique = False
        self._meta.get_field("username")._validators = [username_validator]
        self._meta.get_field("username")._error_messages = None

    username_discriminator = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^(?=[\S\s]{1,%d}$)[\S\s]*"
                % settings.USERNAME_DISCRIMINATOR_LENGTH,
                message="Length has to be 4",
                code="nomatch",
            ),
            MinValueValidator(1),  # Same thing but remove negative digits
        ],
    )
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)
    ip = models.GenericIPAddressField(null=False, blank=False)

    def get_username_with_discriminator(self) -> str:
        return f"{self.username}#{str(self.username_discriminator).zfill(4)}"

    def save(self, *args, **kwargs) -> None:
        # if self.avatar:
        #     file = self.resize(self.avatar)
        #     self.avatar.save(f"{self.username}.avif", file, save=False)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.get_username_with_discriminator()

    class Meta:
        unique_together = ("username", "username_discriminator")
