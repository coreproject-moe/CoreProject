import hashlib
import textwrap
from collections.abc import Iterator

import requests
from django.core.management.utils import get_random_secret_key
from django.core.validators import URLValidator
from django.http import FileResponse, HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from .models import CustomUser

# Create your views here


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse | FileResponse:
    try:
        user = await CustomUser.objects.aget(pk=user_id)
    except CustomUser.DoesNotExist:
        return render(
            request,
            "user/user_does_not_exist.php",
            context={
                "database_name": "postgres",
                "database_user": "animecore",
                "database_password": str(get_random_secret_key()),
                "user_id": user_id,
            },
        )

    if user.avatar:
        avatar_file = open(user.avatar.path, "rb")
        return FileResponse(avatar_file)

    try:
        avatar_url = user.avatar_provider.format(
            EMAIL=hashlib.md5(user.email.strip().lower().encode()).hexdigest()
        )
        # Just a check Here
        URLValidator()(avatar_url)
        _request_ = requests.get(avatar_url, stream=True)

        def streaming_content() -> Iterator[bytes]:
            # Iterate over the response content, and yield it in chunks
            yield from _request_.iter_content(chunk_size=1024)

        return StreamingHttpResponse(
            streaming_content(),
            content_type=_request_.headers["content-type"],
        )

    except Exception as e:
        return HttpResponse(
            textwrap.dedent(
                f"""
                    Please Check your <b>email</b> string.
                    <br/>
                    It is |> <b>{avatar_url}</b>
                    which might not a valid string
                    <br />
                    <b>Error</b> : {e}
                """
            )
        )
