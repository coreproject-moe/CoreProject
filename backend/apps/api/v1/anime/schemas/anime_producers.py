from ninja import ModelSchema

from ..models import AnimeProducerModel


class AnimeProducerSchema(ModelSchema):
    class Config:
        model = AnimeProducerModel
        model_fields = "__all__"
