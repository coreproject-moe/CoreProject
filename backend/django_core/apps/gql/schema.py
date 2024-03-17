import strawberry
from typing import cast

import strawberry_django.permissions

from apps.anime.models import AnimeModel
from .permissions import IsAuthenticated, IsSuperUser
from strawberry import UNSET

from .types.anime import Anime
from .types.character import Character
from .types.producer import Producer
from .types.staff import Staff
import strawberry_django
from strawberry.schema.config import StrawberryConfig
from .mutations.anime import AnimeInput

import strawberry_django
from strawberry.types import Info

from apps.anime.models import AnimeNameSynonymModel
from apps.anime.models.anime_genre import AnimeGenreModel
from apps.anime.models.anime_theme import AnimeThemeModel
from apps.characters.models import CharacterModel
from apps.producers.models import ProducerModel
from apps.staffs.models import StaffModel


@strawberry.type
class Query:
    animes: list[Anime] = strawberry_django.field(pagination=True)
    characters: list[Character] = strawberry_django.field(pagination=True)
    staffs: list[Staff] = strawberry_django.field(pagination=True)
    producers: list[Producer] = strawberry_django.field(pagination=True)


@strawberry.type
class Mutation:
    @strawberry_django.mutation(
        permission_classes=[IsSuperUser],
        extensions=[strawberry_django.permissions.IsSuperuser()],
    )
    def add_anime(self, info: Info, data: AnimeInput) -> Anime:
        kwargs = {
            "mal_id": data.mal_id,
            "anilist_id": data.anilist_id,
            "kitsu_id": data.kitsu_id,
            "name": data.name,
            "name_japanese": data.name_japanese,
            "source": data.source,
            "aired_from": data.aired_from,
            "aired_to": data.aired_to,
            "banner": data.banner,
            "cover": data.cover,
            "synopsis": data.synopsis,
            "background": data.background,
            "rating": data.rating,
            # m2m Fields
            "staffs": data.staffs,
            "genres": data.genres,
            "themes": data.themes,
            "studios": data.studios,
            "producers": data.producers,
            "characters": data.characters,
            #   synonyms names can be
            #       like this   :   ['hello,world']
            #   What we want is :   ['hello', 'world']
            "name_synonyms": data.name_synonyms,
        }
        model_data = {
            key: value
            for key, value in kwargs.items()
            if key
            not in [
                # Ignore M2M relations
                "name_synonyms",
                "genres",
                "themes",
                "studios",
                "producers",
                "characters",
                "staffs",
            ]
            and value != UNSET
        }

        instance = AnimeModel.objects.create(**model_data)

        if name_synonyms_list := kwargs.get("name_synonyms", None):
            for anime_name_synonym in name_synonyms_list:
                anime_synonym_instance, _ = AnimeNameSynonymModel.objects.get_or_create(
                    name=anime_name_synonym.strip(),
                )
                instance.name_synonyms.add(anime_synonym_instance)

        if genres_list := kwargs.get("genres", None):
            for genre in genres_list:
                genre_instance = AnimeGenreModel.objects.get(pk=genre)
                instance.genres.add(genre_instance)

        if themes_list := kwargs.get("themes", None):
            for theme in themes_list:
                theme_instance = AnimeThemeModel.objects.get(pk=theme)
                instance.themes.add(theme_instance)

        if studios_list := kwargs.get("studios", None):
            for studio in studios_list:
                studio_instance = ProducerModel.objects.get(pk=studio)
                instance.studios.add(studio_instance)

        if producers_list := kwargs.get("producers", None):
            for producer in producers_list:
                producer_instance = ProducerModel.objects.get(pk=producer)
                instance.producers.add(producer_instance)

        if characters_list := kwargs.get("characters", None):
            for character in characters_list:
                character_instance = CharacterModel.objects.get(pk=character)
                instance.characters.add(character_instance)

        if staffs_list := kwargs.get("staffs", None):
            for staff in staffs_list:
                staff_instance = StaffModel.objects.get(pk=staff)
                instance.staffs.add(staff_instance)

        return cast(Anime, instance)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=False),
)
