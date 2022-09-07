from typing import List
from ninja import ModelSchema, Field

from .models import StaffModel, StaffAlternateNameModel


class StaffAlternateNameSchema(ModelSchema):
    class Config:
        model = StaffAlternateNameModel
        model_fields = "__all__"


class StaffSchema(ModelSchema):
    alternate_names: List[str] | None

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
            "alternate_names",
        ]

    @staticmethod
    def resolve_alternate_names(obj):
        return [i.name for i in obj.alternate_names.all()]
