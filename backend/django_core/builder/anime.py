import string
from typing import Literal
import httpx


class AnimeBuilder:
    @staticmethod
    def build_list():
        alphabet_list = list("." + string.ascii_uppercase)
        return [
            f"https://myanimelist.net/anime.php?letter={letter}" for letter in alphabet_list
        ]

    def build_urls():
        pass
