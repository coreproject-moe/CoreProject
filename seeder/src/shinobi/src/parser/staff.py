import datetime
import re
from io import BytesIO
from typing import Any, TypedDict

from dateutil import parser

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.mixins.parser.base import BaseParser


class StaffImageDictionary(TypedDict):
    image: BytesIO
    mimetype: str


class StaffDictionary(TypedDict):
    mal_id: str
    name: str
    staff_image: StaffImageDictionary
    given_name: str
    family_name: str
    alternate_name: list[str]
    birthday: datetime.datetime
    about: str


class StaffParser(BaseParser):
    def __init__(self, html: str):
        super().__init__()
        self.parser = self.get_parser(html)

    @property
    @return_on_error("")
    def get_staff_url(self) -> str:
        return self.parser.css_first("meta[property='og:url']").attributes["content"]

    @property
    @return_on_error("")
    def get_staff_id(self) -> str:
        return self.regex_helper.get_id_from_url(self.get_staff_url)

    @property
    @return_on_error({})
    def get_staff_image(self) -> StaffImageDictionary:
        url = self.parser.css_first("meta[property='og:image']").attributes["content"]
        if url:
            res = self.client.get(url)
            return {
                "image": BytesIO(res.content),
                "mimetype": url.split(".")[-1],
            }

    @property
    @return_on_error("")
    def get_staff_name(self) -> str:
        return self.parser.css_first("meta[property='og:title']").attributes["content"]

    @property
    @return_on_error("")
    def get_staff_about(self) -> str:
        return self.parser.css_first(
            "div#content table tr td.borderClass .people-informantion-more"
        ).text()

    @property
    @return_on_error("")
    def get_staff_family_name(self) -> str:
        node = self.parser.css_first("#content table tr td.borderClass")
        matches = node.select("span").text_contains("Family name:").matches
        if len(matches) > 1:
            raise ValueError("There are more than one node in family name node")

        # MAL screwed up the HTML here
        html_match = re.search(
            r"Family name:(.*?)(Alternate names|Birthday|Website|Member Favorites|More)",
            matches[0].parent.text(),
        )
        family_name = self.string_helper.cleanse(html_match.group(1))
        # MyAnimeList has it Empty in places
        # raise AttributeError so we can return None
        if not family_name:
            raise AttributeError("Can't find family name using regex")

        return family_name

    @property
    @return_on_error("")
    def get_staff_given_name(self) -> str:
        node = self.parser.select("span").text_contains("Given name:").matches
        if len(node) > 1:
            raise ValueError("There are more than one node in given name node")

        given_name = self.string_helper.cleanse(node[0].next.text())
        if not given_name:
            raise AttributeError("Can't find given name")

        return given_name

    @property
    @return_on_error([])
    def get_staff_alternate_name(self) -> str:
        node = self.parser.css_first("div#content table tr td.borderClass")
        matches = node.select("div span").text_contains("Alternate names:").matches

        if len(matches) > 1:
            raise ValueError("There are more than one node in alternate name node")

        names = matches[0].next.text().split(",")
        alternate_name = [self.string_helper.cleanse(name) for name in names]

        return alternate_name

    @property
    @return_on_error("")
    def get_staff_birthday(self) -> str:
        node = self.parser.css_first("div#content table tr td.borderClass")
        matches = node.select("div span").text_contains("Birthday:").matches
        if len(matches) > 1:
            raise ValueError("There are more than one node in birthday node")

        birthday = parser.parse(self.string_helper.cleanse(matches[0].next.text()))
        return birthday

    def build_dictionary(self) -> dict[str, Any]:
        dictionary: StaffDictionary = {
            "mal_id": self.get_staff_id,
            "name": self.get_staff_name,
            "given_name": self.get_staff_given_name,
            "family_name": self.get_staff_family_name,
            "alternate_name": self.get_staff_alternate_name,
            "birthday": self.get_staff_birthday,
            "about": self.get_staff_about,
            "staff_image": self.get_staff_image,
        }
        return dictionary
