from typing import TypedDict

from selectolax.parser import HTMLParser

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.string import StringHelper


class GenreDictionary(TypedDict):
    mal_id: int
    name: str
    description: str
    type: str


class AnimeGenreParser:
    def __init__(self, html: str):
        self.parser = HTMLParser(html)

        # Facads
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @property
    @return_on_error("")
    def get_url(self) -> str:
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    @property
    @return_on_error("")
    def get_mal_id(self) -> int:
        return self.regex_helper.get_id_from_url(self.get_url)

    @property
    @return_on_error("")
    def get_name(self) -> str:
        html = self.parser.css_first("span.di-ib.mt4")
        # Remove span nodes
        html.strip_tags(["span.fw-n"])
        actual_text = self.regex_helper.remove_anime_from_the_end_of_a_string(html.text())
        return self.string_helper.cleanse(actual_text)

    @property
    @return_on_error("")
    def get_description(self) -> str:
        text = self.parser.css_first("p.genre-description").text()
        return self.regex_helper.replace_br_with_newline(text)

    @property
    @return_on_error("")
    def get_type(self) -> str:
        text = self.parser.css("div.di-ib")
        # The second node actually shows the item
        actual_node = text[1]
        return self.string_helper.cleanse(actual_node.text())

    def build_dictionary(self) -> GenreDictionary:
        dictionary: GenreDictionary = {
            "mal_id": self.get_mal_id,
            "name": self.get_name,
            "description": self.get_description,
            "type": self.get_type,
        }
        return dictionary
