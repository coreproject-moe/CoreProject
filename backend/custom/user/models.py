from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File

from io import BytesIO
from PIL import Image
import pillow_avif


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars", default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        im = Image.open(self.avatar)

        in_memory = BytesIO()
        im.save(in_memory, format="avif")

        self.avatar = File(in_memory)

        super(CustomUser, self).save(*args, **kwargs)
