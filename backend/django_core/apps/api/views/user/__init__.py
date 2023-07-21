from apps.user.models import CustomUser
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, Form, Router, UploadedFile
from pydantic import AnyUrl, EmailStr

from ...auth import AuthBearer
from ...schemas.user import UserSchema

router = Router()


@router.get("/", response=UserSchema, auth=AuthBearer())
def get_user_info(request: HttpRequest) -> CustomUser:
    user = CustomUser.objects.get(pk=request.auth.id)
    return user


@router.patch("/", response=UserSchema, auth=AuthBearer())
def patch_individual_user_info(
    request: HttpRequest,
    username: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
    email: EmailStr = Form(...),
    avatar_provider: AnyUrl = Form(...),
    avatar: UploadedFile = File(...),
) -> None:
    pass


@router.get("/{str:username}/", response=UserSchema)
def get_individual_user_info(
    request: HttpRequest,
    username: str,
) -> CustomUser:
    user = get_object_or_404(
        CustomUser,
        username=username,
    )
    return user
