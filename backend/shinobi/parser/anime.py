from selectolax.parser import HTMLParser

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.string import StringHelper


class AnimeParser:
    def __init__(self, html: str) -> None:
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @property
    @return_on_error("")
    def get_anime_url(self) -> str:
        return self.parser.css_first("meta[property='og:url']").attributes["content"]

    @property
    @return_on_error("")
    def get_anime_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_anime_url)

    @property
    @return_on_error("")
    def get_anime_name(self) -> str:
        return self.parser.css_first("meta[property='og:title']").attributes["content"]

    @property
    @return_on_error("")
    def get_anime_name_japanese(self) -> str:
        node = self.parser.select("span").text_contains("Japanese:").matches
        if len(node) > 1:
            raise ValueError("There are more than one node in name japanese node")

        name_japanese = self.string_helper.cleanse(node[0].next.text())
        return name_japanese

    @property
    @return_on_error("")
    def get_anime_name_synonyms(self) -> list[str]:
        node = self.parser.css(
            'h2:contains("Alternative Titles") + div:has(+ h2:contains("Information"))'
        )
        print(node)

    def build_dictionary(self):
        dictionary = {
            "mal_id": self.get_anime_id,
            "name": self.get_anime_name,
            "name_japanese": self.get_anime_name_japanese,
            "name_synonyms": self.get_anime_name_synonyms,
            "source": "",
            # Datetime
            "aired_from": "",
            "aired_to": "",
            "synopsis": "",
            "background": "",
            "rating": "",
            # List[int]
            "genres": "",
            "themes": "",
            "characters": "",
            "studios": "",
            "producers": "",
            "staffs": "",
            "recommendations": "",  # self
            "episodes": "",
            "openings": "",
            "endings": "",
        }
        return dictionary
