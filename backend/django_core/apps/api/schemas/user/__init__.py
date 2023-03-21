from apps.user.models import CustomUser
from ninja import ModelSchema

from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class UserSchema(ModelSchema):
    avatar: str

    class Config:
        model = get_user_model()
        model_exclude = [
            "password",
            "avatar",
            "ip",  # https://github.com/pydantic/pydantic/issues/333
        ]

    @staticmethod
    def resolve_avatar(obj: CustomUser) -> str:
        url = reverse_lazy(
            "avatar_view",
            kwargs={
                "user_id": obj.id,
            },
        )
        return f"{url}"
