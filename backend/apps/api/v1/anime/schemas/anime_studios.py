from ninja import ModelSchema

from ..models import AnimeStudioModel


class AnimeStudioSchema(ModelSchema):
    class Config:
        model = AnimeStudioModel
        model_fields = "__all__"
