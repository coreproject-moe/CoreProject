from apps.user.models import CustomUser
from django.http import HttpRequest
from ninja import Form, Router
from pydantic import EmailStr

from ...schemas.user import UserSchema

router = Router()


@router.post("/sign_up", response=UserSchema)
def post_user_signup_info(
    request: HttpRequest,
    username: str = Form(...),
    password: str = Form(...),
    email: EmailStr = Form(...),
):
    user = CustomUser.objects.create_user(
        email=email,
        password=password,
        username=username,
    )
    return user
