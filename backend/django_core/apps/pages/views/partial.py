from ..request import HtmxHttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from ..templatetags.markdown import markdown


async def markdown_endpoint(request: "HtmxHttpRequest") -> "HttpResponse":
    return HttpResponse(markdown(request.body.decode()))
