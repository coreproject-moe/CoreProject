from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper


class GenreBuilder:
    """
    Given : https://myanimelist.net/anime.php
    Return all the `genres` in MyAnimeList
    """

    base_url = "https://myanimelist.net/anime/genre/{}"

    def __init__(self, html: str) -> None:
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @property
    def genre_list(self) -> list[int]:
        genre_nodes = self.parser.css('a[href*="genre"]')
        link_ids = [
            int(self.regex_helper.get_id_from_url(node.attributes["href"]))
            for node in genre_nodes
        ]
        return sorted(link_ids)

    def build_urls(self) -> list[str]:
        return [self.base_url.format(mal_id) for mal_id in self.genre_list]
