import os

from django.http import FileResponse, HttpRequest
from django.urls.resolvers import _route_to_regex

# Create your views here.


async def opengraph(request: HttpRequest) -> FileResponse:
    SCRIPT_DIR = os.path.dirname(__file__)

    # Do some logics on this
    print(_route_to_regex("<str:hello>/"))
    if False:
        pass

    else:
        OPENGRAPH_IMAGE = os.path.join(SCRIPT_DIR, "images", "base.jpg")

    return FileResponse(open(OPENGRAPH_IMAGE, "rb"))
