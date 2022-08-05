from django.conf import settings
from django.shortcuts import resolve_url
from ninja import ModelSchema
from pydantic import AnyUrl

from ..models import AnimeInfoModel


class AnimeInfoSchema(ModelSchema):
    anime_genres: AnyUrl
    anime_producers: AnyUrl

    class Config:
        model = AnimeInfoModel
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
        ]

    @staticmethod
    def resolve_anime_genres(obj):
        url = resolve_url("api-1.0.0:get_individual_anime_genre_info", anime_id=obj.id)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_anime_producers(obj):
        url = resolve_url(
            "api-1.0.0:get_individual_anime_producer_info", anime_id=obj.id
        )
        return f"{settings.HOSTNAME}{url}"
