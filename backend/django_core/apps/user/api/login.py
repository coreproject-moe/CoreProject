from ninja import Form, Router
from pydantic import EmailStr

from django.http import HttpRequest

from ..models import Token
from ..schemas.login import LoginSchema
from ..backends import EmailOrUsernameModelBackend

router = Router()


@router.post("/login", response=LoginSchema)
def post_user_signup_info(
    request: HttpRequest,
    username: str | EmailStr = Form(...),
    password: str = Form(...),
):
    user = EmailOrUsernameModelBackend.get_user_given_username_and_password(
        username, password
    )
    token, _ = Token.objects.get_or_create(user=user)
    return token
