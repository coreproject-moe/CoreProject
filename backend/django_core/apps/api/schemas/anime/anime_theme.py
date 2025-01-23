from apps.anime.models.anime_theme import AnimeThemeModel
from ninja import ModelSchema


class AnimeThemeGETSchema(ModelSchema):
    class Config:
        model = AnimeThemeModel
        model_fields = "__all__"


class AnimeThemePOSTSchema(ModelSchema):
    class Config:
        model = AnimeThemeModel
        model_exclude = [
            "id",
            "type",
            "created_at",
            "updated_at",
            "is_locked",
        ]
