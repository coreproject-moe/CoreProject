from ninja import Schema


class AnimeInfoFilters(Schema):
    mal_id: int | None = None
    kitsu_id: int | None = None
    anilist_id: int | None = None

    # Relation based on
    #       * name
    #       * name_japanese
    #       * name_synonyms__name
    name: str | None = None

    # Map as closely to model fields as possible.
    # So we can do something like
    # genres__name__icontains
    genres: str | None = None
    themes: str | None = None
    studios: str | None = None
    producers: str | None = None
    characters: str | None = None


# Extra imports
