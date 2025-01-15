from apps.anime.models import AnimeModel, AnimeNameSynonymModel
from django.db.models import Avg
from django.shortcuts import resolve_url
from ninja import ModelSchema

from .anime_opening_and_ending import AnimeOpeningAndEndingGETSchema

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
    staffs: str
    genres: str
    producers: str
    studios: str
    characters: str
    themes: str
    episodes: str
    episodes_count: int
    average_episode_length: int
    name_synonyms: list[AnimeNameSynonymSchema] = []
    openings: list[AnimeOpeningAndEndingGETSchema] = []
    endings: list[AnimeOpeningAndEndingGETSchema] = []

    class Config:
        model = AnimeModel
        model_fields = "__all__"

    @staticmethod
    def resolve_average_episode_length(obj: AnimeModel) -> int:
        if instance := obj.episodes.all():
            avg = instance.aggregate(value=Avg("episode_length"))
            return avg["value"]
        else:
            return 0

    @staticmethod
    def resolve_episodes_count(obj: AnimeModel) -> int:
        return obj.episodes.count()

    @staticmethod
    def resolve_staffs(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_staff_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_genres(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_genre_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_producers(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_producer_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_studios(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_studio_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_characters(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_character_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_themes(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_anime_theme_info", anime_id=obj.pk)
        return f"{url}"

    @staticmethod
    def resolve_episodes(obj: AnimeModel) -> str:
        url = resolve_url("api-1.0.0:get_individual_episodes", anime_id=obj.pk)
        return f"{url}"
