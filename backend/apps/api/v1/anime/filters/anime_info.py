from ninja import Schema


class AnimeInfoFilters(Schema):
    anime_name: str = None
    anime_genres: str = None
    anime_themes: str = None
    anime_studio: str = None
    anime_producer: str = None
