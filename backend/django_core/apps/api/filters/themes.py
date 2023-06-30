from ninja import Schema


class ThemeFilter(Schema):
    name: str | None = None
    mal_id: int | None = None
