from ninja import Schema


class GenreFilter(Schema):
    name: str | None = None
    mal_id: int | None = None
