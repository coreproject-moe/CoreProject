from typing import List

from ninja import ModelSchema

from .models import StaffAlternateNameModel, StaffModel


class StaffAlternateNameSchema(ModelSchema):
    class Config:
        model = StaffAlternateNameModel
        model_fields = "__all__"


class StaffSchema(ModelSchema):
    alternate_names: list[str] | None

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
            "alternate_names",
        ]

    @staticmethod
    def resolve_alternate_names(obj):
        return [i.name for i in obj.alternate_names.all()]
