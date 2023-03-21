from apps.user.models import CustomUser
from ninja import Form, Router
from pydantic import EmailStr
from django.conf import settings
from django.http import HttpRequest

from ...schemas.user import UserSchema

router = Router()


@router.post("/signup", response=UserSchema)
def post_user_signup_info(
    request: HttpRequest,
    username: str = Form(
        ...,
        regex=rf"^[a-zA-Z0-9]+#[0-9]{settings.DISCRIMINATOR_LENGTH}$",
    ),
    password: str = Form(...),
    email: EmailStr = Form(...),
) -> CustomUser:
    if "#" in username:
        splitted_username = username.split("#")
        username = splitted_username[0]
        discriminator = splitted_username[1]
    else:
        discriminator = None

    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        username=username,
    )

    if discriminator:
        user.discriminator = discriminator
        user.save()

    return user
