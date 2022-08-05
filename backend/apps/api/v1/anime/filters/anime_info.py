from ninja import Schema


class AnimeInfoFilters(Schema):
    anime_name__icontains: str = None
    anime_name_japanese__icontains: str = None
    anime_source__icontains: str = None
    anime_genres: str = None
    anime_themes: str = None
