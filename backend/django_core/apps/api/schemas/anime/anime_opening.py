from apps.anime.models.anime_openings_and_endings import AnimeOpeningModel
from ninja import ModelSchema


class AnimeOpeningGETSchema(ModelSchema):
    class Config:
        model = AnimeOpeningModel
        model_fields = "__all__"


class AnimeOpeningPOSTSchema(ModelSchema):
    class Config:
        model = AnimeOpeningModel
        model_exclude = [
            "id",
        ]
