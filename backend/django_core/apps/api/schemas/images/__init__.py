from ninja import ModelSchema
from ....images.models import ImageWithBrightnessAndBackgroundColor


class ImageWithBrightnessAndBackgroundColorSchema(ModelSchema):
    class Config:
        model = ImageWithBrightnessAndBackgroundColor
        model_fields = "__all__"
