from ninja import Form, Router
from pydantic import EmailStr

from django.http import Http404, HttpRequest

from ..backends import EmailOrUsernameModelBackend
from ..models import Token
from ..schemas.login import LoginSchema

router = Router()


@router.post("/login", response=LoginSchema)
def post_user_login_info(
    request: HttpRequest,
    username: str | EmailStr = Form(...),
    password: str = Form(...),
):
    print(username)
    user = EmailOrUsernameModelBackend.get_user_given_username_and_password(
        username, password
    )

    if not user:
        raise Http404("No such user exists")

    token, _ = Token.objects.get_or_create(user=user)
    return token
