from ninja import Schema


class StaffFilter(Schema):
    mal_id: int | None = None
    kitsu_id: int | None = None
    anilist_id: int | None = None

    # icontains based search
    #   Allowed :
    #       Sora Amamiya, Natsukawa Shiina, Momo Asakura
    #       Sora Amamiya
    name: str | None = None

    given_name: str | None = None
    family_name: str | None = None
