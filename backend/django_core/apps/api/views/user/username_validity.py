from http import HTTPStatus

from apps.user.models import CustomUser
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from ninja import Form, Router

from ...schemas.user.username_validity import UsernameValiditySchema

router = Router()


@router.post(
    "",
    response={
        302: UsernameValiditySchema,
        404: UsernameValiditySchema,
        406: UsernameValiditySchema,
    },
)
def post_username_validity_info(
    request: HttpRequest,
    username: str = Form(...),
) -> HttpResponse:
   pass