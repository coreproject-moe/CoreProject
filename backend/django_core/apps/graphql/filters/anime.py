import strawberry
from strawberry import auto
from apps.anime.models import AnimeModel
from django.db.models.functions import Greatest
from django.contrib.postgres.search import TrigramSimilarity

@strawberry.django.filters.filter(AnimeModel,lookups=True)
class AnimeFilter:
    mal_id: auto

    name: str
    def filter_name(self, queryset):
       
        print(queryset)
        return queryset
