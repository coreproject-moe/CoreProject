from collections.abc import Generator
import hashlib
from io import BytesIO
import mimetypes
from typing import IO
from .forms import UserRegistrationForm, UsernameDiscriminatorForm

from yarl import URL

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, StreamingHttpResponse
from django.views.decorators.http import require_POST

from aiohttp_client_cache.backends import RedisBackend
from aiohttp_client_cache.session import CachedSession

from .models import CustomUser

CHUNK_SIZE = 512  # 512 bytes


def read_files_in_chunks(
    file_object: IO[bytes],
    chunk_size: int = CHUNK_SIZE,
) -> Generator[bytes, None, None]:
    """
    Lazy function to read a file piece by piece.
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

    file_object.close()


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse:
    response: StreamingHttpResponse

    try:
        user: CustomUser = await get_user_model().objects.aget(id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist")

    if user.avatar:
        avatar_file = open(user.avatar.path, "rb")
        file_iterator = read_files_in_chunks(avatar_file)
        response = StreamingHttpResponse(
            streaming_content=file_iterator,
        )
        response["content-type"] = str(
            mimetypes.MimeTypes().guess_type(
                url=user.avatar.path,
            )[0]
        )

    else:
        # Proxy from Libravatar
        url = str(
            URL(
                user.avatar_provider.format(
                    EMAIL=hashlib.md5(user.email.strip().lower().encode()).hexdigest()
                )
            ),
        )
        async with CachedSession(
            cache=RedisBackend(
                "avatar",
                expire_after=settings.CACHE_MIDDLEWARE_SECONDS,
            )
        ) as session:
            async with session.get(url, allow_redirects=True) as r:
                response = HttpResponse(
                    BytesIO(await r.read()),
                    headers={
                        "content-type": r.headers["content-type"],
                    },
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
