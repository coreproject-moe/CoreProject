import hashlib

from core.utility import sendfile
import httpx

from django.contrib.auth import get_user_model
from django.core.management.utils import get_random_secret_key
from django.core.validators import URLValidator
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from .models import CustomUser


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse:
    response: StreamingHttpResponse

    try:
        user: CustomUser = await get_user_model().objects.aget(id=user_id)
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
        client = httpx.AsyncClient()

        try:
            avatar_url = user.avatar_provider.format(
                EMAIL=hashlib.md5(user.email.strip().lower().encode()).hexdigest()
            )
            # Just a check Here
            URLValidator(avatar_url)

            _request_ = client.build_request("GET", avatar_url)
            avatar_response = await client.send(_request_)
            response = StreamingHttpResponse(
                avatar_response.iter_bytes(),
                content_type=avatar_response.headers["content-type"],
            )
        except Exception as e:
            response = HttpResponse(
                f"""
                Please Check your email string.
                <br/>
                It is {avatar_url} which is not a valid string
                <br />
                Error : {e}
                """
            )

    return response
