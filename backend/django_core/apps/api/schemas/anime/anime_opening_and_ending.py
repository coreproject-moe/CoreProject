from apps.anime.models.anime_openings_and_endings import AnimeOpeningModel
from ninja import ModelSchema


class AnimeOpeningAndEndingGETSchema(ModelSchema):
    class Config:
        model = AnimeOpeningModel
        model_fields = "__all__"
