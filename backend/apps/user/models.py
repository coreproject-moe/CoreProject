from typing import NoReturn

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .mixins.resize import ResizeImageMixin

# Create your models here.


def default_kitsu():
    return {
        "access_token": "",
        "created_at": 0,
        "expires_in": 0,
        "refresh_token": "",
    }


def default_myanimelist():
    return {
        "access_token": "",
        "created_at": 0,
        "expires_in": 0,
        "refresh_token": "",
    }


class User(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)
    # Tracker sync related data ( JSON FIELDS )
    myanimelist = models.JSONField(default=default_myanimelist, null=True, blank=True)
    kitsu = models.JSONField(default=default_kitsu, null=True, blank=True)
    # Custom user fields
    video_volume = models.PositiveIntegerField(
        default=100,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )

    def save(self, *args, **kwargs) -> NoReturn:
        if self.avatar:
            file = self.resize(self.avatar)
            self.avatar.save(f"{self.username}.avif", file, save=False)

        super().save(*args, **kwargs)
