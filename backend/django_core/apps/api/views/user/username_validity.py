
from django.http import HttpRequest, HttpResponse
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
