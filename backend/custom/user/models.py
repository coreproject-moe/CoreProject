from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

from .mixins.resize import ResizeImageMixin


class CustomUser(AbstractUser, ResizeImageMixin):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id:
            file = self.resize(self.avatar)
            self.avatar.save(f"{self.id}-{uuid4()}.avif", file, save=False)

        super(CustomUser, self).save(*args, **kwargs)
