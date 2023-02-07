import hashlib
import textwrap

import httpx
from django.http import FileResponse
from django.core.management.utils import get_random_secret_key
from django.core.validators import URLValidator
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from .models import CustomUser


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse:
    CLIENT = httpx.AsyncClient()

    try:
        user = await CustomUser.objects.aget(pk=user_id)
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
        response = FileResponse(avatar_file)

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

    await CLIENT.aclose()
    return response
