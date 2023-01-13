from apps.user.models import CustomUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from ninja import ModelSchema
from pydantic import AnyUrl


class UserSchema(ModelSchema):
    avatar: AnyUrl

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
        return f"{settings.HOSTNAME}{url}"
