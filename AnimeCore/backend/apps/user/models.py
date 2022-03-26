from django.db import models

# Create your models here.
from typing import NoReturn

from django.db import models
from django.contrib.auth.models import AbstractUser

from .mixins.resize import ResizeImageMixin


class User(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)

    def save(self, *args, **kwargs) -> NoReturn:
        if self.avatar:
            file = self.resize(self.avatar)
            self.avatar.save(f"{self.username}.avif", file, save=False)

        super().save(*args, **kwargs)
