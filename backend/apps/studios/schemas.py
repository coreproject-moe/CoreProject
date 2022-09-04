from ninja import ModelSchema

from .models import StudioModel


class StudioSchema(ModelSchema):
    class Config:
        model = StudioModel
        model_exclude = [
            "id",
        ]
