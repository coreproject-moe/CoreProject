from apps.api.models import Token
from apps.user.backends import EmailOrUsernameModelBackend
from django.http import Http404, HttpRequest
from django_ratelimit.decorators import ratelimit
from ninja import Form, Router
from pydantic import EmailStr

from ...schemas.user.login import LoginSchema

router = Router()


@router.post("/login", response=LoginSchema)
@ratelimit(key="ip", rate="1/s")
def post_user_login_info(
    request: HttpRequest,
    username: str | EmailStr = Form(...),
    password: str = Form(...),
) -> Token:
    user = EmailOrUsernameModelBackend.get_user_given_username_and_password(
        username,
        password,
    )

    if not user:
        raise Http404("No such user exists")

    token, _ = Token.objects.get_or_create(user=user)
    return token
