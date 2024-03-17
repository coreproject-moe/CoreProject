from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.session import session


class AnimeGenreBuilder:
    def __init__(self) -> None:
        # Reusuable Clients
        self.client = session

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    def __build_urls(self, ids: list[int]) -> list[str]:
        return [f"https://myanimelist.net/anime/genre/{mal_id}" for mal_id in ids]

    def __build_ids(self, html: str) -> list[int]:
        parser = self.get_parser(html)
        genre_nodes = parser.css('a[href*="genre"]')
        link_ids = [
            self.regex_helper.get_id_from_url(node.attributes["href"])
            for node in genre_nodes
            if node.attributes["href"]
        ]

        return sorted(link_ids)

    def build_dictionary(self) -> dict[int, str]:
        res = self.client.get("https://myanimelist.net/anime.php")
        html = res.text

        ids = self.__build_ids(html)
        urls = self.__build_urls(ids)

        dictionary = dict(zip(ids, urls))

        return dictionary
