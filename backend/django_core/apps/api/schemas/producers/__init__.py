from ninja import ModelSchema

from ....producers.models import ProducerModel


class ProducerGETSchema(ModelSchema):
    class Config:
        model = ProducerModel
        model_fields = "__all__"


class ProducerPOSTSchema(ModelSchema):
    kitsu_id: int | None = None

    class Config:
        model = ProducerModel
        model_exclude = [
            "id",
            "created_at",
            "updated_at",
            "is_locked",
        ]
