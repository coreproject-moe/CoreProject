from ninja import Schema


class CharacterFilter(Schema):
    mal_id: str = None

    # icontains based search
    #   Allowed :
    #       Sora Amamiya, Natsukawa Shiina
    #       Sora Amamiya
    name: str = None
