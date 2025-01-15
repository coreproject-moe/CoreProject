from apps.anime.models.anime_genre import AnimeGenreModel
from ninja import ModelSchema


class AnimeGenreGETSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_fields = "__all__"


class AnimeGenrePOSTSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_exclude = [
            "id",
            "type",
            "created_at",
            "updated_at",
            "is_locked",
        ]
