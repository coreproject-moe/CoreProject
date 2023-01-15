from ninja import ModelSchema

from ....staffs.models import StaffModel


class StaffSchema(ModelSchema):
    alternate_names: list[str] | None

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
        ]
