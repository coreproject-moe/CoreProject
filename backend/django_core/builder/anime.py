import string


class AnimeBuilder:
    def __init__(self) -> None:
        pass

    @staticmethod
    def build_list():
        alphabet_list = list(string.ascii_uppercase + ".")
        return [
            f"https://myanimelist.net/anime.php?letter={letter}" for letter in alphabet_list
        ]
