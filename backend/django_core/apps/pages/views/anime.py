from django.shortcuts import render
from django.http import HttpResponse
from typing import TYPE_CHECKING
from ..data.anime import icons

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


def anime_home_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(request, "anime/_partial.html")

    return render(request, "anime/home.html", context={"icons": icons})
