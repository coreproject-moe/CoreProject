# https://github.com/vitalik/django-ninja/issues/417#issuecomment-1092545699
from django.utils.decorators import sync_and_async_middleware
import asyncio
from django.http import HttpRequest


def check_and_patch(request: HttpRequest):
    if request.method in ("PUT", "PATCH") and request.content_type != "application/json":
        initial_method = request.method
        request.method = "POST"
        request.META["REQUEST_METHOD"] = "POST"
        request._load_post_and_files()
        request.META["REQUEST_METHOD"] = initial_method
        request.method = initial_method


@sync_and_async_middleware
def process_put_patch(get_response):
    if asyncio.iscoroutinefunction(get_response):

        async def middleware(request):
            check_and_patch(request)
            return await get_response(request)

    else:

        def middleware(request):
            check_and_patch(request)
            return get_response(request)

    def middleware(request):
        return get_response(request)

    return middleware
