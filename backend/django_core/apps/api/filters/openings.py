from ninja import Schema


class OpeningFilter(Schema):
    # Opening number
    entry: int | None = None
    # Opening/closing theme name
    name: str | None = None
