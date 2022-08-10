from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from ninja import Router

from ..schemas import SignupSchema, UserSchema

router = Router()


@router.post("/signup", response=UserSchema)
def post_user_signup_info(request: HttpRequest, payload: SignupSchema):
    return user
