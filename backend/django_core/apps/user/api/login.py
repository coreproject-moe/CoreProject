from ninja import Form, Router
from pydantic import EmailStr

from django.contrib.auth import authenticate
from django.http import HttpRequest

from ..schemas import UserSchema

router = Router()


@router.post("/login", response=UserSchema)
def post_user_login_info(
    request: HttpRequest,
    username: str | EmailStr = Form(...),
    password: str = Form(...),
):
    # This should work when we are in same domain
    user = authenticate(request, username=username, password=password)
    return user
