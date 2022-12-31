from ninja import ModelSchema

from ....producers.models import ProducerModel


class ProducerSchema(ModelSchema):
    class Config:
        model = ProducerModel
        model_exclude = [
            "id",
        ]
