# Code Owners : `horidesu`, `baseplate-admin`
# Licensed Under : AGPL-v3

from typing import TypedDict

from selectolax.parser import HTMLParser
from utilities.regex import RegexHelper

# We need to return `None` on exception.
# Because there can be cases where the node doesn't exist in HTML
from ._decorators import return_empty_string_on_catched_error


class CharacterDictionary(TypedDict):
    mal_id: str
    name: str
    name_kanji: str
    character_image: str
    about: str


class CharacterParser:
    def __init__(self, html: str):
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @return_empty_string_on_catched_error
    def get_character_url(self) -> str:
        return self.parser.css_first("meta[property='og:url']").attributes["content"]

    @return_empty_string_on_catched_error
    def get_character_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_character_url())

    @return_empty_string_on_catched_error
    def get_character_name(self):
        return self.parser.css_first("meta[property='og:title']").attributes["content"]

    @return_empty_string_on_catched_error
    def get_character_name_kanji(self):
        return self.regex_helper.get_content_between_first_brackets(
            self.parser.css_first("h2.normal_header span small").text()
        )

    @return_empty_string_on_catched_error
    def get_about(self):
        html = self.parser.css_first("#content table tbody tr > td:nth-of-type(2)")
        tags = ["div", "br", "table", "h2"]
        html.strip_tags(tags)
        sentences = html.text().split("\n")
        return "\n\n".join(sentences).strip()

    @return_empty_string_on_catched_error
    def get_character_image(self):
        return self.parser.css_first("meta[property='og:image']").attributes["content"]

    def build_dictionary(self) -> CharacterDictionary:
        dictionary = {
            "mal_id": self.get_character_id(),
            "name": self.get_character_name(),
            "name_kanji": self.get_character_name_kanji(),
            "character_image": self.get_character_image(),
            "about": self.get_about(),
        }
        return dictionary
