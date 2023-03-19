from apps.user.models import CustomUser
from ninja import Router, Form
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse

from http import HTTPStatus

router = Router()


@router.post(
    "",
    response={
        302: str,
        404: str,
        406: str,
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
        return JsonResponse(
            "Your username is too popular. Please pick another one",
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
            "Username with discriminator is unavailable",
            safe=False,
            status=HTTPStatus.FOUND,
        )

    else:
        # Return status code 200 if username with discriminator is available
        return JsonResponse(
            "Username available",
            safe=False,
            status=HTTPStatus.NOT_FOUND,
        )
