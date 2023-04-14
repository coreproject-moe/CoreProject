from django.db import models
from dynamic_filenames import FilePattern
from mixins.brightness import BrightnessMixin
from mixins.background_color import BackgroundColorMixin

# Create your models here.
image_upload_pattern = FilePattern(filename_pattern="{uuid:s}{ext}")


class Image(models.Model):
    image = models.ImageField(upload_to=image_upload_pattern)

    class Meta:
        verbose_name = "Image"


class ImageWithBrightnessAndBackgroundColor(Image, BrightnessMixin, BackgroundColorMixin):
    class Meta:
        verbose_name = "Image with brightness and background color"
        verbose_name_plural = "Images with brightness and background color"
