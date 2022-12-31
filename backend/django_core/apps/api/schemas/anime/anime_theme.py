from apps.anime.models import AnimeThemeModel
from ninja import ModelSchema


class AnimeThemeSchema(ModelSchema):
    class Config:
        model = AnimeThemeModel
        model_fields = "__all__"
