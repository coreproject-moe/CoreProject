import string
from typing import Literal


class AnimeBuilder:
    @staticmethod
    def build_list(name: Literal["anime"] | Literal["character"]):
        alphabet_list = list(string.ascii_uppercase + ".")
        return [
            f"https://myanimelist.net/anime.php?letter={letter}" for letter in alphabet_list
        ]
