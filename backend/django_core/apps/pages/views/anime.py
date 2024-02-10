from typing import TYPE_CHECKING

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response

from ..data.anime import (
    anime,
    anime_episode,
    latest_animes,
    latest_episodes,
    my_list,
)

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


async def anime_home_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(
            request,
            "anime/index.html",
            context={
                "latest_animes": latest_animes,
                "my_list": my_list,
                "latest_episodes": latest_episodes,
            },
        )

    return render(
        request,
        "anime/_layout.html",
        context={
            "latest_animes": latest_animes,
            "my_list": my_list,
            "latest_episodes": latest_episodes,
        },
    )


async def anime_explore_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(request, "anime/explore/index.html")

    return render(request, "anime/_layout.html")


async def anime_info_view(
    request: "HtmxHttpRequest",
    platform: str,
    pk: int,
) -> HttpResponse:
    if request.htmx:
        return render(
            request,
            "anime/info/index.html",
            context={"anime": anime, "episodes": [anime_episode for _ in range(0, 10)]},
        )

    return render(request, "anime/_layout.html", context={})


async def anime_episode_view(
    request: "HtmxHttpRequest", platform: str, mal_id: int, pk: int
) -> HttpResponse:
    if request.htmx:
        return render(
            request,
            "anime/episode/index.html",
            context={},
        )

    return render(request, "anime/_layout.html", context={})


async def anime_latest_episodes(request: HttpRequest):
    return JsonResponse(latest_episodes, safe=False)

async def anime_latest_animes(request: HttpRequest):
    return JsonResponse(latest_animes, safe=False)