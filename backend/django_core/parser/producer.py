# Code Owners : `horidesu`, `baseplate-admin`
# Licensed Under : AGPL-v3

from selectolax.parser import HTMLParser

from utilities.regex import RegexHelper
from ._decorators import return_specified_type_on_catched_error


class ProducerParser:
    def __init__(self, html: str):
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @return_specified_type_on_catched_error("str")
    def get_studio_url(self):
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    def build_dictionary(self):
        return {
            "mal_id": self.get_studio_id(),
            "name": self.get_title(),
            "default_title": "",
            "japanese_title": "",
            "established": "",
            "about": "",
        }
