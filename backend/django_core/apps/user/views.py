import hashlib

from core.utility import sendbytes, sendfile
from yarl import URL

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.utils import get_random_secret_key
from django.http import HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render

from aiohttp_client_cache.backends import RedisBackend
from aiohttp_client_cache.session import CachedSession

from .models import CustomUser

CHUNK_SIZE = 512  # 512 bytes


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
                response = sendbytes(
                    await r.read(),
                    content_type=r.headers["content-type"],
                )

    return response
