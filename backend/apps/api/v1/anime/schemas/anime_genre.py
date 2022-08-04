from ninja import ModelSchema

from ..models.anime_genre import AnimeGenreModel


class AnimeGenreSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_fields = "__all__"
