from ninja import Form, Router
from pydantic import EmailStr

from django.http import HttpRequest

from ..models import CustomUser
from ..schemas import UserSchema

router = Router()


@router.post("/sign_up", response=UserSchema)
def post_user_signup_info(
    request: HttpRequest,
    username: str = Form(...),
    password: str = Form(...),
    email: EmailStr = Form(...),
):
    user = CustomUser.objects.create_user(
        email,
        password,
        username=username,
    )
    return user
