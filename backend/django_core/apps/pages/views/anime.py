from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render

from ..data.anime import icons, latest_animes

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


async def anime_home_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(
            request,
            "anime/_partial/home.html",
            context={"latest_animes": latest_animes},
        )

    return render(
        request,
        "anime/_layout.html",
        context={"icons": icons, "latest_animes": latest_animes},
    )


async def anime_explore_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(request, "anime/_partial/explore.html")

    return render(request, "anime/_layout.html", context={"icons": icons})


async def anime_info_view(request: "HtmxHttpRequest", pk: int) -> HttpResponse:
    return render(request, "anime/_layout.html", context={"icons": icons})
