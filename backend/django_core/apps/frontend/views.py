from pregex import Pregex
from pregex.core import cl, gr, op
from user_agents import parse

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import Resolver404

from ..anime.models import AnimeModel

# Create your views here.


def animecore(request: HttpRequest) -> HttpResponse:
    user_agent_parsed = parse(request.headers["user-agent"])

    if user_agent_parsed.is_bot:
        MAL_PATH: Pregex = (
            "/animecore/"
            + op.Either("mal", "myanimelist")
            + "/"
            + gr.Capture(cl.AnyDigit())
        )
        ANILIST_PATH: Pregex = "/animecore/anilist/" + gr.Capture(cl.AnyDigit())
        KISTU_PATH: Pregex = "/animecore/kitsu/" + gr.Capture(cl.AnyDigit())

        # /animecore/mal/<int:myanimelist_number>
        if myanimelist_path := MAL_PATH.get_captures(request.get_full_path()):
            myanimelist_number = myanimelist_path[0][0]
            anime_model = get_object_or_404(AnimeModel, mal_id=myanimelist_number)
            context = {
                "opengraph_title": anime_model.anime_name,
                "opengraph_type": "webpage",
                "opengraph_image": anime_model.anime_banner,
                "opengraph_url": request.build_absolute_uri(),
                "info_dump": [
                    anime_model.anime_background,
                    anime_model.anime_synopsis,
                ],
            }

        # /animecore/anilist/<int:anilist_number>
        elif anilist_path := ANILIST_PATH.get_captures(request.get_full_path()):
            anilist_number = anilist_path[0][0]
            anime_model = get_object_or_404(AnimeModel, anilist_id=anilist_number)
            context = {
                "opengraph_title": anime_model.anime_name,
                "opengraph_type": "webpage",
                "opengraph_image": anime_model.anime_banner,
                "opengraph_url": request.build_absolute_uri(),
                "info_dump": [
                    anime_model.anime_background,
                    anime_model.anime_synopsis,
                ],
            }

        # /animecore/kitsu/<int:kitsu_number>
        elif kitsu_path := KISTU_PATH.get_captures(request.get_full_path()):
            kitsu_number = kitsu_path[0][0]
            anime_model = get_object_or_404(AnimeModel, kitsu_id=kitsu_number)
            context = {
                "opengraph_title": anime_model.anime_name,
                "opengraph_type": "webpage",
                "opengraph_image": anime_model.anime_banner,
                "opengraph_url": request.build_absolute_uri(),
                "info_dump": [
                    anime_model.anime_background,
                    anime_model.anime_synopsis,
                ],
            }

        else:
            raise Resolver404()

        return render(
            request,
            "frontend/bot_response.html",
            context=context,
        )

    else:
        return render(request, "frontend/animecore.html")


def user(request: HttpRequest) -> HttpResponse:
    return render(request, "frontend/user.html")
