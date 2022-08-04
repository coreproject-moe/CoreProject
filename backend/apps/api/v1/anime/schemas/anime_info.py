from ..models import AnimeInfoModel
from ninja import ModelSchema


class AnimeInfoSchema(ModelSchema):
    class Config:
        model = AnimeInfoModel
        model_fields = "__all__"
