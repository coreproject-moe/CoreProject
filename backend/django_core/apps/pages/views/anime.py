from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render

from ..data.anime import icons, latest_animes

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


async def anime_home_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        print("HTMX home")
        return render(
            request,
            "anime/_partial_home.html",
            context={"latest_animes": latest_animes},
        )

    return render(
        request,
        "anime/_layout.html",
        context={"icons": icons, "latest_animes": latest_animes},
    )


async def anime_explore_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        print("HTMX explore")
        return render(request, "anime/_partial_explore.html")

    return render(
        request,
        "anime/_layout.html",
        context={"icons": icons},
    )
