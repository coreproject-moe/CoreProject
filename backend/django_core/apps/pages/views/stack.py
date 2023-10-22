from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..data.stack import context

# Create your views here.


def stack_view(request: HttpRequest) -> HttpResponse:
    return render(request, "stack/index.html", context)
