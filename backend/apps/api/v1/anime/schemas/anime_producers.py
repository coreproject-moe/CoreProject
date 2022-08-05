from ..models import AnimeProducerModel

from ninja import ModelSchema


class AnimeProducerSchema(ModelSchema):
    class Config:
        model = AnimeProducerModel
        model_fields = "__all__"
