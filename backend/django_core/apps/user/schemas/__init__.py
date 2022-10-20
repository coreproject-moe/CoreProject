from ninja import ModelSchema
from pydantic import AnyUrl

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from ..models import CustomUser


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


# Extra Imports
# __ DO NOT MODIFY __

from .sign_up import SignupSchema as SignupSchema
