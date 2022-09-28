from ninja import Schema


class AnimeInfoFilters(Schema):
    mal_id: str | None = None
    kitsu_id: str | None = None
    anilist_id: str | None = None

    # Relation based on
    #       * anime_name
    #       * anime_name_japanese
    #       * anime_name_synonyms__name
    anime_name: str | None = None

    # Map as closely to model fields as possible.
    # So we can do something like
    # anime_genres__name__icontains
    anime_genres: str | None = None
    anime_themes: str | None = None
    anime_studios: str | None = None
    anime_producers: str | None = None
    anime_characters: str | None = None


# Extra imports
