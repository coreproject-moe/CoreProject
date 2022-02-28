# Thanks Random guy from here :
# https://note.nkmk.me/en/python-pillow-image-crop-trimming/

import pillow_avif
from PIL import Image
from io import BytesIO

from django.db.models import ImageField
from django.core.files import File

# Image height and width in pixel
CROP_WIDTH = 512
CROP_HEIGHT = 512


class ResizeImageMixin(object):
    def resize(self, image: ImageField) -> File:
        base_image = Image.open(image)
        width, height = base_image.size

        resized_image = base_image.crop(
            (
                (width - CROP_WIDTH) // 2,
                (height - CROP_HEIGHT) // 2,
                (width + CROP_WIDTH) // 2,
                (height + CROP_HEIGHT) // 2,
            )
        )

        in_memory = BytesIO()
        resized_image.save(in_memory, format="avif")

        return File(in_memory)
