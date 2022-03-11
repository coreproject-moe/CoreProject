from uuid import uuid4
from hashlib import md5
from typing import NoReturn

from django.db import models
from django.contrib.auth.models import AbstractUser

from .mixins.resize import ResizeImageMixin


class CustomUser(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)

    def save(self, *args, **kwargs) -> NoReturn:
        if self.avatar:
            file = self.resize(self.avatar)
            self.avatar.save(f"{uuid4()}.avif", file, save=False)

        super().save(*args, **kwargs)
