from ninja import ModelSchema

from apps.anime.models import AnimeGenreModel


class AnimeGenreSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_fields = "__all__"
