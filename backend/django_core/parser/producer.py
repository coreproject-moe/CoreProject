# Code Owners : `horidesu`, `baseplate-admin`
# Licensed Under : AGPL-v3

from selectolax.parser import HTMLParser
from utilities.string import StringHelper
from utilities.regex import RegexHelper
from ._decorators import return_specified_type_on_catched_error

from dateutil import parser


class ProducerParser:
    def __init__(self, html: str):
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)
    
    @return_specified_type_on_catched_error("str")
    def get_producer_url(self):
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    @return_specified_type_on_catched_error("str")
    def get_producer_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_producer_url())

    @return_specified_type_on_catched_error("str")
    def get_producer_name(self):
        node = self.parser.css_first("#contentWrapper > div:first-child > h1")
        return self.string_helper.cleanse(node.text())

    @return_specified_type_on_catched_error("str")
    def get_producer_japanese_name(self):
        node = self.parser.select("span").text_contains("Japanese:")
        return self.string_helper.cleanse(node.matches[0].next.text())

    @return_specified_type_on_catched_error("str")
    def get_producter_establish_date(self):
        node = self.parser.select("span").text_contains("Established:")
        string_date = self.string_helper.cleanse(node.matches[0].next.text())
        actual_date = parser.parse(string_date)
        return actual_date

    @return_specified_type_on_catched_error("str")
    def get_producer_about(self):
        return self.parser.css_first(
            "#content > div:nth-of-type(1) div.spaceit_pad > span:not(.dark_text)"
        ).text()

    def build_dictionary(self):
        return {
            "mal_id": self.get_producer_id(),
            "name": self.get_producer_name(),
            "japanese_title": self.get_producer_japanese_name(),
            "established": self.get_producter_establish_date(),
            "about": self.get_producer_about(),
        }
