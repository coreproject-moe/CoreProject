from typing import NoReturn

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .mixins.resize import ResizeImageMixin

# Create your models here.


class User(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)
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


class MalModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=1024, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


class KitsuModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=64, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


class AnilistModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=64, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
