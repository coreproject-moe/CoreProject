from selectolax.parser import HTMLParser
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.string import StringHelper


class BaseParser:
    def __init__(self):
        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)
