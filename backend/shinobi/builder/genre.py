import httpx
from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper


class GenreBuilder:
    def __init__(self) -> None:
        # Reusuable Clients
        self.client = httpx.Client(follow_redirects=True, http2=True)

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    def _build_urls(self, ids: list[int]) -> list[str]:
        return [f"https://myanimelist.net/anime/genre/{mal_id}" for mal_id in ids]

    def _build_ids(self, html: str) -> list[int]:
        parser = self.get_parser(html)
        genre_nodes = parser.css('a[href*="genre"]')
        link_ids = [
            self.regex_helper.get_id_from_url(node.attributes["href"])
            for node in genre_nodes
        ]
        return sorted(link_ids)

    def build_dictionary(self) -> dict[int, str]:
        res = self.client.get("https://myanimelist.net/anime.php")
        html = res.content

        ids = self._build_ids(html)
        urls = self._build_urls(ids)

        dictionary = dict(zip(ids, urls))

        return dictionary
