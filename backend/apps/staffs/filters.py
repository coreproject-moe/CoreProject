from ninja import Schema


class StaffFilter(Schema):
    mal_id: str | None = None
    kitsu_id: str | None = None
    anilist_id: str | None = None

    # icontains based search
    #   Allowed :
    #       Sora Amamiya, Natsukawa Shiina, Momo Asakura
    #       Sora Amamiya
    name: str | None = None

    given_name: str | None = None
    family_name: str | None = None
