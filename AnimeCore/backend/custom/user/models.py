from uuid import uuid4
from hashlib import md5
from typing import NoReturn

from django.db import models
from django.contrib.auth.models import AbstractUser

from .mixins.resize import ResizeImageMixin


class CustomUser(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)

    def email_md5(self) -> str:
        email = self.email
        return md5(email.encode("utf-8")).hexdigest()

    def save(self, *args, **kwargs) -> NoReturn:
        if self.avatar:
            file = self.resize(self.avatar)
            self.avatar.save(f"{uuid4()}.avif", file, save=False)

        super(CustomUser, self).save(*args, **kwargs)
