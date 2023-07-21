from apps.user.models import CustomUser
from django.http import HttpRequest
from ninja import Form, Router
from pydantic import EmailStr

from ...schemas.user import UserSchema
from django.conf import settings


router = Router()


@router.post("/signup", response=UserSchema)
def post_user_signup_info(
    request: HttpRequest,
    username: str = Form(
        ...,
        regex=rf"^[a-zA-Z0-9_-]+#[0-9]{{{settings.DISCRIMINATOR_LENGTH}}}$",
    ),
    password: str = Form(...),
    email: EmailStr = Form(...),
) -> CustomUser:
    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        username=username,
    )

    return user
