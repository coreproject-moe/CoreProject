from ninja import File, Form, Router
from ninja.files import UploadedFile

from django.http import HttpRequest

from ..models import CustomUser
from ..schemas import SignupSchema, UserSchema

router = Router()


@router.post("/sign_up", response=UserSchema)
def post_user_signup_info(
    request: HttpRequest,
    payload: SignupSchema = Form(...),
    avatar: UploadedFile = File(...),
):
    return CustomUser.objects.create(
        avatar=avatar,
        **payload.dict(exclude_none=True),
    )
