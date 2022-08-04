from ninja import ModelSchema

from ..models import AnimeInfoModel


class AnimeInfoSchema(ModelSchema):
    class Config:
        model = AnimeInfoModel
        model_fields = "__all__"
