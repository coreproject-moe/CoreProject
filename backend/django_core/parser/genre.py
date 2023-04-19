from selectolax.parser import HTMLParser

from utilities.regex import RegexHelper

from ._decorators import return_specified_type_on_catched_error


class AnimeGenreParser:
    def __init__(self, html: str):
        self.parser = HTMLParser(html)

        # Facads
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @property
    @return_specified_type_on_catched_error("str")
    def get_url(self) -> str:
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    @property
    @return_specified_type_on_catched_error("str")
    def get_mal_id(self) -> int:
        return self.regex_helper.get_id_from_url(self.get_url)

    def build_dictionary(self):
        pass
