from django.conf import settings
from django.shortcuts import resolve_url
from ninja import ModelSchema
from pydantic import AnyUrl

from ..models import AnimeModel
from ..schemas.anime_synonym import AnimeSynonymSchema


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

    @staticmethod
    def resolve_episode(obj):
        url = resolve_url("api-1.0.0:get_individual_anime_episodes", anime_id=obj.id)
        return f"{settings.HOSTNAME}{url}"


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
from .anime_producers import AnimeProducerSchema
from .anime_studios import AnimeStudioSchema
from .anime_theme import AnimeThemeSchema
from .episode import EpisodeGETSchema, EpisodePOSTSchema
from .episode_comment import EpisodeCommentGETSchema, EpisodeCommentPOSTSchema
from .episode_timestamp import (
    EpisodeTimestampGETSchema,
    EpisodeTimestampPOSTSchema,
    EpisodeTimestampTotalTimestampSchema,
)
