import hashlib
import textwrap

from core.utility import sendfile
import httpx

from django.views.decorators.http import require_POST
from django.core.management.utils import get_random_secret_key
from django.core.validators import URLValidator
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.conf import settings

from .models import CustomUser
from .forms import UserRegistrationForm, UsernameDiscriminatorForm

CLIENT = httpx.AsyncClient()


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse:
    response: StreamingHttpResponse

    try:
        user = await CustomUser.objects.aget(id=user_id)
    except CustomUser.DoesNotExist:
        return render(
            request,
            "user/user_does_not_exist.htm",
            context={
                "database_name": "postgres",
                "database_user": "animecore",
                "database_password": str(get_random_secret_key()),
                "user_id": user_id,
            },
        )

    if user.avatar:
        avatar_file = open(user.avatar.path, "rb")
        response = sendfile(avatar_file)

    else:
        try:
            avatar_url = user.avatar_provider.format(
                EMAIL=hashlib.md5(user.email.strip().lower().encode()).hexdigest()
            )
            # Just a check Here
            URLValidator()(avatar_url)

            _request_ = CLIENT.build_request("GET", avatar_url)
            avatar_response = await CLIENT.send(_request_)
            response = StreamingHttpResponse(
                avatar_response.iter_bytes(),
                content_type=avatar_response.headers["content-type"],
            )
        except Exception as e:
            response = HttpResponse(
                textwrap.dendant(
                    f"""
                        Please Check your <b>email</b> string.
                        <br/>
                        It is |> <b>{avatar_url}</b>
                        which is not a valid string
                        <br />
                        <b>Error</b> : {e}
                    """
                )
            )

    return response


def signup_view(request: HttpRequest) -> HttpResponse:
    form = UserRegistrationForm(request.POST or None)

    return render(
        request,
        "user/signup.html",
        context={
            "form": form,
        },
    )


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "user/login.html")


@require_POST
def username_discriminator_endpoint(
    request: HttpRequest,
) -> HttpResponse:
    """
    Returns :
        - 404 : not found
        - 302 : found
    """
    form = UsernameDiscriminatorForm(request.POST or None)

    if form.is_valid() and not (
        CustomUser.objects.get_username_with_discriminator()
        .filter(
            username_with_discriminator=f"""{
                form.cleaned_data.get('username')
            }#{
                form.cleaned_data.get('username_discriminator')
                .zfill(
                    settings.USERNAME_DISCRIMINATOR_LENGTH
                )
            }
            """
        )
        .exists()
    ):
        return HttpResponse(status_code=404)
    else:
        return HttpResponse(status_code=302)
