import inspect
from django.shortcuts import resolve_url
from ninja import ModelSchema
from pydantic import AnyUrl
from cache_memoize import cache_memoize
from django.http import HttpRequest

from ..models import AnimeModel
from ..schemas.anime_synonym import AnimeSynonymSchema


# So initial ovservation is that our code call was reduced from
#  1.     0.256s -> 0.020s ( Normal LRU Cache / Settings.py | Not persistant | Not Applicable for our use case / If we want to have a static url )
#  2.     0.256s -> 0.025s ( redis-lru / But it restarts on interpreter shutdown | Saves to Redis | Not applicable for our use case )
#  3.     0.256s -> 0.045s ( django-cache-memoize / Django-cache | Saves to Redis | Is applicable for our use case)
# We DO need to store this somewhere persistant.
# Since Gunicorn works by having a stateless nature,
# this function will get called only once and subsequently the output is cached for the rest of the call.


# HOT PATH OPTIMIZATION HERE
# DO NOT MODIFY IF YOU DONT KNOW WHAT YOU ARE DOING
@cache_memoize(timeout=None)
def get_url_from_requests() -> str:
    # https://stackoverflow.com/questions/4721771/get-current-user-log-in-signal-in-django
    request: HttpRequest | None = None
    for frame_record in inspect.stack():
        if frame_record[3] == "get_response":
            request = frame_record[0].f_locals["request"]
            break

    return request.build_absolute_uri() if request else ""


class AnimeInfoGETSchema(ModelSchema):
    anime_genres: AnyUrl
    anime_producers: AnyUrl
    anime_studios: AnyUrl
    anime_characters: AnyUrl
    anime_name_synonyms: list[AnimeSynonymSchema] = []
    anime_theme: AnyUrl
    episode: AnyUrl

    class Config:
        model = AnimeModel
        model_fields = [
            "mal_id",
            "anime_name",
            "anime_name_japanese",
            "anime_source",
            "anime_aired_from",
            "anime_aired_to",
            "anime_banner",
            "anime_cover",
            "anime_synopsis",
            "anime_background",
            "anime_rating",
            "updated",
            "anime_name_synonyms",
        ]

    @staticmethod
    def resolve_anime_genres(obj) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_genre_info", anime_id=obj.id)
        return f"{get_url_from_requests()}{url}"

    @staticmethod
    def resolve_anime_producers(obj) -> str:
        url = resolve_url(
            "api-1.0.0:get_individual_anime_producer_info", anime_id=obj.id
        )
        return f"{get_url_from_requests()}{url}"

    @staticmethod
    def resolve_anime_studios(obj) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_studio_info", anime_id=obj.id)
        return f"{get_url_from_requests()}{url}"

    @staticmethod
    def resolve_anime_characters(obj) -> str:
        url = resolve_url(
            "api-1.0.0:get_individual_anime_character_info", anime_id=obj.id
        )
        return f"{get_url_from_requests()}{url}"

    @staticmethod
    def resolve_anime_theme(obj) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_theme_info", anime_id=obj.id)
        return f"{get_url_from_requests()}{url}"

    @staticmethod
    def resolve_episode(obj) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_episodes", anime_id=obj.id)
        return f"{get_url_from_requests()}{url}"


class AnimeInfoPOSTSchema(ModelSchema):
    class Config:
        model = AnimeModel
        model_exclude = [
            "anime_genres",
            "anime_themes",
            "anime_studios",
            "anime_producers",
            "anime_name_synonyms",
            "anime_episodes",
            "anime_recommendation",
            "anime_characters",
        ]


# Extra imports


from .anime_genre import AnimeGenreSchema
from .anime_theme import AnimeThemeSchema
from .episode import EpisodeGETSchema, EpisodePOSTSchema
from .episode_comment import EpisodeCommentGETSchema, EpisodeCommentPOSTSchema
from .episode_timestamp import (
    EpisodeTimestampGETSchema,
    EpisodeTimestampPOSTSchema,
    EpisodeTimestampTotalTimestampSchema,
)
