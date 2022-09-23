from ninja import Router

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from ..schemas import UserSchema

router = Router(tags=["user"])


@router.get("/", response=UserSchema)
def get_user_info(request: HttpRequest):
    user = get_user_model().objects.get(id=request.user.id)
    return user


@router.get("/{str:username}/", response=UserSchema)
def get_individual_user_info(request: HttpRequest, username: str):
    user = get_object_or_404(
        get_user_model().objects.get_username_with_discriminator(),
        username_with_discriminator=username,
    )

    return user


# Router Configuration
# __ DO NOT MODIFY __

from .sign_up import router as signup_router

router.add_router("", signup_router, tags=["user"])
