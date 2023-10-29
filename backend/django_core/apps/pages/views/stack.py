from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from typing import TYPE_CHECKING
from ..data.anime import icons

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest

from ..data.stack import context

# Create your views here.


def stack_view(request: "HtmxHttpRequest") -> HttpResponse:
    return render(request, "stack/index.html", context)
