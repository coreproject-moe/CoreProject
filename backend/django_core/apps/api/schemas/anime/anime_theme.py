from ninja import ModelSchema

from apps.anime.models import AnimeThemeModel


class AnimeThemeSchema(ModelSchema):
    class Config:
        model = AnimeThemeModel
        model_fields = "__all__"
