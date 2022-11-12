from ninja import File, Form, Router
from ninja.files import UploadedFile
from pydantic import AnyUrl, EmailStr

from django.conf import settings
from django.http import HttpRequest

from ..models import CustomUser
from ..schemas import UserSchema

router = Router()


@router.post("/sign_up", response=UserSchema)
def post_user_signup_info(
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
    user = CustomUser.objects.create_user(
        email,
        password,
        first_name=first_name,
        last_name=last_name,
        username=username,
        username_discriminator=username_discriminator,
        avatar=avatar,
        avatar_provider=avatar_provider,
    )
    return user
