from ninja import ModelSchema

from ....studios.models import StudioModel


class StudioGETSchema(ModelSchema):
    class Config:
        model = StudioModel
        model_fields = "__all__"


class StudioPOSTSchema(ModelSchema):
    class Config:
        model = StudioModel
        model_exclude = [
            "id",
        ]
