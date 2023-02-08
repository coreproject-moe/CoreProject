from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from ninja import ModelSchema
from pydantic import AnyUrl

from django.conf import settings
from django.shortcuts import resolve_url

## Observations from getting request from stack trace
# So initial ovservation is that our code call was reduced from
#  1.     0.256s -> 0.020s ( Normal LRU Cache / Settings.py | Not persistant | Not Applicable for our use case / If we want to have a static url )
#  2.     0.256s -> 0.025s ( redis-lru / But it restarts on interpreter shutdown | Saves to Redis | Not applicable for our use case )
#  3.     0.256s -> 0.045s ( django-cache-memoize / Django-cache | Saves to Redis | Is applicable for our use case)
# We DO need to store this somewhere persistant.
# Since Gunicorn works by having a stateless nature,
# this function will get called only once and subsequently the output is cached for the rest of the call.

# All in all i am reverting to settings.py


## future update ??
## Take a look at issue(526)


class AnimeNameSynonymSchema(ModelSchema):
    class Config:
        model = AnimeNameSynonymModel
        model_fields = ["name"]


class AnimeInfoGETSchema(ModelSchema):
    genres: AnyUrl
    producers: AnyUrl
    studios: AnyUrl
    characters: AnyUrl
    themes: AnyUrl
    episode: AnyUrl
    name_synonyms: list[AnimeNameSynonymSchema] = []

    class Config:
        model = AnimeModel
        model_fields = "__all__"

    @staticmethod
    def resolve_genres(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_genre_info", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_producers(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_producer_info", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_studios(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_studio_info", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_characters(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_character_info", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_themes(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_theme_info", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"

    @staticmethod
    def resolve_episode(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_episodes", anime_id=obj.pk)
        return f"{settings.HOSTNAME}{url}"
