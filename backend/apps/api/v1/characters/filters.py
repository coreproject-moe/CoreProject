from ninja import Schema


class CharacterFilter(Schema):
    mal_id: str | None = None

    # icontains based search
    #   Allowed :
    #       Sora Amamiya, Natsukawa Shiina, Momo Asakura
    #       Sora Amamiya
    name: str | None = None
