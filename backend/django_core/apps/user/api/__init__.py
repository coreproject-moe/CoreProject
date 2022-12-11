from core.auth import AuthBearer
from ninja import File, Form, Router, UploadedFile
from pydantic import AnyUrl, EmailStr

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from core.auth import AuthBearer

from ..schemas import UserSchema

router = Router(tags=["user"])


@router.get("/", response=UserSchema, auth=AuthBearer())
def get_user_info(request: HttpRequest):
    user = get_user_model().objects.get(id=request.auth.id)
    return user


@router.patch("/", response=UserSchema, auth=AuthBearer())
def patch_individual_user_info(
    request: HttpRequest,
    username: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
    email: EmailStr = Form(...),
    username_discriminator: int = Form(
        default=None, gt=0, lt=int(str(settings.USERNAME_DISCRIMINATOR_LENGTH * "9"))
    ),
    avatar_provider: AnyUrl = Form(...),
    avatar: UploadedFile = File(...),
):
    pass


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
from .login import router as login_router

router.add_router("", signup_router, tags=["user"])
router.add_router("", login_router, tags=["user"])
