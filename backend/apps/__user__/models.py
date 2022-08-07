from typing import NoReturn

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .mixins.resize import ResizeImageMixin

# Create your models here.


class User(AbstractUser, ResizeImageMixin):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # We dont want unique usernames
        self._meta.get_field("username")._unique = False
        self._meta.get_field("username")._validators = []

    username_discriminator = models.IntegerField(
        default=1,
        blank=False,
        null=False,
        validators=[
            MaxValueValidator(9999),  # Allow upto 4 Digits
            MinValueValidator(1),  # Same thing but remove negative digits
        ],
    )
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)
    video_volume = models.PositiveIntegerField(
        default=100,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    @property
    def get_username_and_discriminator(self) -> str:
        return f"{self.username}#{str(self.username_discriminator).zfill(4)}"

    def save(self, *args, **kwargs) -> NoReturn:
        # if self.avatar:
        #     file = self.resize(self.avatar)
        #     self.avatar.save(f"{self.username}.avif", file, save=False)

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ("username", "username_discriminator")
