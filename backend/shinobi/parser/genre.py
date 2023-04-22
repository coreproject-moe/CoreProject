from selectolax.parser import HTMLParser

from shinobi.utilities.regex import RegexHelper

from shinobi.decorators.return_error_decorator import return_on_error


class AnimeGenreParser:
    def __init__(self, html: str):
        self.parser = HTMLParser(html)

        # Facads
        self.regex_helper = RegexHelper()

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

    def build_dictionary(self):
        pass
