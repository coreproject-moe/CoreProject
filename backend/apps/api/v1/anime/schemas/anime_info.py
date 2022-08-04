from ninja import ModelSchema

from ..models import AnimeInfoModel
from typing import Optional


class AnimeInfoSchema(ModelSchema):
    anime_genres: Optional[str]

    class Config:
        model = AnimeInfoModel
        model_fields = [
            "mal_id",
            "anime_name",
            "anime_name_japanese",
            "anime_source",
            "anime_aired_from",
            "anime_aired_to",
            "anime_banner",
            "anime_cover",
            "anime_synopsis",
            "anime_background",
            "anime_rating",
            "updated",
        ]

    # Fix me later
    # 1/anime_genres
    @staticmethod
    def resolve_anime_genres(obj):
        return f"{obj.id}/anime_genres"
