from django.conf import settings
from django.shortcuts import resolve_url
from ninja import ModelSchema
from pydantic import AnyUrl

from ..models import AnimeInfoModel
from ..schemas.anime_synonym import AnimeSynonymSchema


class AnimeInfoSchema(ModelSchema):
    anime_genres: AnyUrl
    anime_producers: AnyUrl
    anime_studios: AnyUrl
    anime_characters: AnyUrl
    anime_name_synonyms: list[AnimeSynonymSchema] = None
    anime_theme: AnyUrl

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
            "anime_name_synonyms",
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

    @staticmethod
    def resolve_anime_studios(obj):
        url = resolve_url("api-1.0.0:get_individual_anime_studio_info", anime_id=obj.id)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_anime_characters(obj):
        url = resolve_url(
            "api-1.0.0:get_individual_anime_character_info", anime_id=obj.id
        )
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_anime_theme(obj):
        url = resolve_url("api-1.0.0:get_individual_anime_theme_info", anime_id=obj.id)
        return f"{settings.HOSTNAME}{url}"
