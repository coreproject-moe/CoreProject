# Code Owners : `horidesu`, `baseplate-admin`
# Licensed Under : AGPL-v3


import re

from selectolax.parser import HTMLParser

from ..utilities.regex import RegexHelper
from ._decorators import return_none_on_exception


class ProducerParser:
    def __init__(self, html: str):
        self.parser = self.get_parser(html)

        # Facades
        self.regex_helper = RegexHelper()

    @staticmethod
    def get_parser(html):
        return HTMLParser(html)

    @return_none_on_exception
    def get_studio_url(self):
        return self.parser.css_first('meta[property="og:url"]').attributes["content"]

    def get_title(self):
        return self.get_studio_url().split("/")[-1].replace("_", " ")

    def get_studio_id(self):
        return self.regex_helper.get_id_from_url(self.get_studio_url())

    def get_alternate_titles(self):
        english_titles = [
            h1.text().strip()
            for h1 in self.parser.css("#contentWrapper > div:first-child > h1")
        ]
        japanese_titles = (
            re.search(r"Japanese:.*", self.parser.text())[0]
            .replace("Japanese: ", "")
            .strip()
        )
        return [*english_titles, japanese_titles]

    def get_established(self):
        return (
            re.search(r"Established:.*", self.parser.text())[0]
            .replace("Established:", "")
            .strip()
        )

    def get_image(self):
        return self.parser.css_first('meta[property="og:image"]').attributes["content"]

    def get_about(self):
        return self.parser.css_first(
            "#content > div:nth-of-type(1) div.spaceit_pad > span:not(.dark_text)"
        ).text()

    def build_dictionary(self):
        return {
            "mal_id": self.get_studio_id(),
            "title": self.get_title(),
        }
