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

        in_memory = BytesIO()

        # Square image, so just resize it?
        if width == height:
            resized_image = base_image.resize((128, 128), Image.ANTIALIAS)
            resized_image.save(in_memory, format="avif")

        else:
            cropped_image = base_image.crop(
                (
                    (width - CROP_WIDTH) // 2,  # left
                    (height - CROP_HEIGHT) // 2,  # upper
                    (width + CROP_WIDTH) // 2,  # right
                    (height + CROP_HEIGHT) // 2,  # lower
                )
            )
            resized_image = cropped_image.resize((128, 128), Image.ANTIALIAS)

            resized_image.save(in_memory, format="avif")

        return File(in_memory)
