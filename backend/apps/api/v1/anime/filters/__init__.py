from ninja import Schema


class AnimeInfoFilters(Schema):
    anime_name: str = None
    anime_genres: str = None
    anime_themes: str = None
    anime_studios: str = None
    anime_producers: str = None

    # Map as closely to model fields as possible.
    # So we can do something like
    # anime_genres__name__icontains


# Extra imports
