from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest

from ..data.stack import context

# Create your views here.


async def stack_view(request: "HtmxHttpRequest") -> HttpResponse:
    return render(request, "stack/index.html", context)
