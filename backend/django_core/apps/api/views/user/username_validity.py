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
    discriminator: int
    | None = Form(
        default=None,
    ),
) -> HttpResponse:
    if CustomUser.objects.filter(username=username).distinct("discriminator").count() > int(
        "9" * settings.DISCRIMINATOR_LENGTH
    ):
        # Return status code 406 if username with discriminator is not available in db
        return JsonResponse(
            {
                "status": 406,
                "message": "Your username is too popular. Please pick another one",
            },
            safe=False,
            status=HTTPStatus.NOT_ACCEPTABLE,
        )

    if (
        CustomUser.objects.get_username_with_discriminator()
        .filter(
            username_with_discriminator=f"{username}#{str(discriminator).zfill(settings.DISCRIMINATOR_LENGTH)}"
        )
        .exists()
    ):
        # Return status code 406 if username with discriminator exists
        return JsonResponse(
            {
                "status": 406,
                "message": "Username with discriminator is unavailable",
            },
            safe=False,
            status=HTTPStatus.FOUND,
        )

    else:
        # Return status code 200 if username with discriminator is available
        return JsonResponse(
            {
                "status": 200,
                "message": "Username available",
            },
            safe=False,
            status=HTTPStatus.NOT_FOUND,
        )
