from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


def home_view(request: "HtmxHttpRequest"):
    return render(request, "home/index.html")
