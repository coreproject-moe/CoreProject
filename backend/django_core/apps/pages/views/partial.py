from django.http import HttpResponse

from ..request import HtmxHttpRequest
from ..templatetags.markdown import markdown


async def markdown_endpoint(request: "HtmxHttpRequest") -> "HttpResponse":
    return HttpResponse(markdown(request.body.decode()))
