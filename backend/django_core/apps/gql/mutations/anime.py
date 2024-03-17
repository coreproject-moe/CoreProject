import strawberry_django
from strawberry import auto
from apps.anime.models import AnimeModel
import datetime


@strawberry_django.input(AnimeModel, fields=["name"], partial=True)
class AnimeInput:
    name: auto
