from ninja import Schema


class CharacterFilter(Schema):
    mal_id: int | None = None
    kitsu_id: int | None = None
    anilist_id: int | None = None

    # icontains based search
    #   Allowed :
    #       Sora Amamiya, Natsukawa Shiina, Momo Asakura
    #       Sora Amamiya
    name: str | None = None
