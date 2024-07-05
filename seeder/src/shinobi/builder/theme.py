from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.session import session
from shinobi.utilities.string import StringHelper


class AnimeThemeBuilder:
    def __init__(self) -> None:
        self.anchors: list[str] = []

        # Reusuable clients
        self.client = session

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    def __build_ids(self) -> list[int]:
        return [self.regex_helper.get_first_integer_from_url(item) for item in self.anchors]

    def __build_urls(self, html: str) -> list[str]:
        parser = self.get_parser(html)
        theme_parent_node = (
            parser.select("div.normal_header").text_contains("Themes").matches[0].next.next
        )
        theme_anchor_nodes = theme_parent_node.css('a[href*="genre"]')

        self.anchors = [
            self.string_helper.add_myanimelist_if_not_already_there(
                anchor.attributes["href"]
            )
            for anchor in theme_anchor_nodes
            if anchor.attributes["href"]
        ]
        return self.anchors

    def build_dictionary(self) -> dict[int, str]:
        res = self.client.get("https://myanimelist.net/anime.php")
        html = res.text

        urls = self.__build_urls(html)
        ids = self.__build_ids()

        dictionary = dict(zip(ids, urls))

        return dictionary
