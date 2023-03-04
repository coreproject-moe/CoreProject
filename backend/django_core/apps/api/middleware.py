from django.utils.decorators import sync_and_async_middleware
from typing import Callable
from django.http import HttpRequest, HttpResponse
from asgiref.sync import sync_to_async

import asyncio


@sync_and_async_middleware
def process_put_patch(get_response: Callable) -> Callable:
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request: HttpRequest) -> HttpResponse:
            if (
                request.method in ("PUT", "PATCH")
                and request.content_type != "application/json"
            ):
                initial_method = request.method
                request.method = "POST"
                request.META["REQUEST_METHOD"] = "POST"
                await sync_to_async(request._load_post_and_files)()
                request.META["REQUEST_METHOD"] = initial_method
                request.method = initial_method

            return await get_response(request)

    else:

        def middleware(request: HttpRequest) -> HttpResponse:
            if (
                request.method in ("PUT", "PATCH")
                and request.content_type != "application/json"
            ):
                initial_method = request.method
                request.method = "POST"
                request.META["REQUEST_METHOD"] = "POST"
                request._load_post_and_files()
                request.META["REQUEST_METHOD"] = initial_method
                request.method = initial_method

            return get_response(request)

    return middleware
