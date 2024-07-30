import re
from selectolax.parser import HTMLParser
from typing import Set
from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.session import session

import xml.etree.ElementTree as ET


class StaffBuilder:
    def __init__(self) -> None:
        # Reusuable clients
        self.client = session

        # Facades
        self.regex_helper = RegexHelper()

        # Urls
        self.urls_to_visit = self.__build_people()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    def __build_people(self) -> Set[int]:
        url = "https://myanimelist.net/sitemap/index.xml"
        res = self.client.get(url)
        tree = ET.fromstring(res.content)

        people_urls = []
        pattern = re.compile(r"people")

        people_urls = [
            element.text
            for sitemap in tree
            for element in sitemap
            if "loc" in element.tag and pattern.search(element.text)
        ]

        return set(people_urls)

    def build_dictionary(
        self, excluded_ids: list[int] | None = None, sort: bool = False
    ) -> dict[int, str]:
        dictionary = {}

        for url in self.urls_to_visit:
            res = self.client.get(url)
            tree = ET.fromstring(res.content)

            for entry in tree:
                for element in entry:
                    if "loc" in element.tag:
                        content = element.text
                        dictionary[self.regex_helper.get_id_from_url(content)] = content

        if sort:
            dictionary = dict(sorted(dictionary.items()))

        return dictionary
