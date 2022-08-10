from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

from ..schemas import UserSchema

router = Router(tags=["user"])


@router.get("/", response=UserSchema)
def get_user_info(request: HttpRequest):
    user = get_user_model().objects.get(id=request.user.id)
    return user


@router.get("/{str:username}/", response=UserSchema)
def get_individual_user_info(request: HttpRequest, username: str):
    user = get_object_or_404(
        get_user_model().objects.annotate(
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
        ),
        username_with_discriminator=username,
    )

    return user


# Router Configuration
# __ DO NOT MODIFY __

from .signup import router as signup_router

router.add_router("", signup_router, tags=["user"])
