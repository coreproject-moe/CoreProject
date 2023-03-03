from ninja import ModelSchema

from ....producers.models import ProducerModel


class ProducerGETSchema(ModelSchema):
    class Config:
        model = ProducerModel
        model_fields = "__all__"


class ProducerPOSTSchema(ModelSchema):
    class Config:
        model = ProducerModel
        model_exclude = [
            "id",
            "type",
        ]
