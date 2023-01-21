from ninja import Schema


class ProducerFilter(Schema):
    mal_id: int | None = None

    # icontains based search
    #   Allowed :
    #       A1 Pictures, Studio Ghibli
    #       A1 Pictures
    name: str | None = None
