from ninja import ModelSchema

from ....staffs.models import StaffModel


class StaffSchema(ModelSchema):
    alternate_names: list[str] | None

    class Config:
        model = StaffModel
        model_exclude = [
            "id",
        ]

    @staticmethod
    def resolve_alternate_names(obj: StaffModel) -> list[str]:
        # Modify the list from ['hello,world'] to ['hello','world']
        return obj.alternate_names[0].split(",")
