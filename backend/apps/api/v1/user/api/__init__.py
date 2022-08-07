from django.contrib.auth import get_user_model
from django.http import HttpRequest
from ninja import Router
from django.db.models.functions import Cast, Concat, LPad
from django.db.models import CharField, Value
from django.conf import settings

from ..schemas import UserSchema

router = Router()


@router.get("/", response=UserSchema, tags=["user_info"])
def get_user_info(request: HttpRequest):
    user = get_user_model().objects.get(username=request.user)
    return user


@router.get("/{str:username}/", response=UserSchema, tags=["user_info"])
def get_individual_user_info(request: HttpRequest, username: str):
    user = (
        get_user_model()
        .objects.annotate(
            username_discriminator_as_string=Cast(
                "username_discriminator", output_field=CharField()
            ),
            username_with_discriminator=Concat(
                "username",
                Value("#"),
                LPad(
                    "username_discriminator_as_string",
                    int(settings.USERNAME_DISCRIMINATOR_LENGTH),
                    Value("0"),
                ),
                output_field=CharField(),
            ),
        )
        .get(username_with_discriminator=username)
    )

    return user
