from ninja import ModelSchema

from .models import ProducerModel


class ProducerSchema(ModelSchema):
    class Config:
        model = ProducerModel
        model_exclude = [
            "id",
        ]
