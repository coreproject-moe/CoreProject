from apps.__user__.models import MalModel
from ninja import ModelSchema


class MALSchema(ModelSchema):
    class Config:
        model = MalModel
        model_fields = "__all__"
