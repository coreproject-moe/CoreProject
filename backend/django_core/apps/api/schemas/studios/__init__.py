from ninja import ModelSchema

from ....studios.models import StudioModel


class StudioSchema(ModelSchema):
    class Config:
        model = StudioModel
        model_exclude = [
            "id",
        ]
