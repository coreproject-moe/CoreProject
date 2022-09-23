from ninja import ModelSchema
from pydantic import AnyUrl

from django.conf import settings
from django.contrib.auth import get_user_model

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
        print(settings.AIOHTTP_AVATAR_URL)
        url = settings.AIOHTTP_AVATAR_URL + str(obj.pk)
        return f"{url}"


# Extra Imports
# __ DO NOT MODIFY __

from .sign_up import SignupSchema as SignupSchema
