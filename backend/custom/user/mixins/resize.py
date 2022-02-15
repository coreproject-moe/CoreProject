import pillow_avif
from PIL import Image
from io import BytesIO

from django.db.models import ImageField
from django.core.files import File


class ResizeImageMixin(object):
    def resize(self, image: ImageField) -> File:
        im = Image.open(image)

        in_memory = BytesIO()
        im.save(in_memory, format="avif")

        return File(in_memory)
