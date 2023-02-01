from apps.anime.models.anime_genre import AnimeGenreModel
from ninja import ModelSchema


class AnimeGenreSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_fields = "__all__"
