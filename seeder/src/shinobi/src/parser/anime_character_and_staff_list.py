from shinobi.decorators.return_error_decorator import return_on_error

from shinobi.mixins.parser.base import BaseParser


class AnimeCharacterAndStaffListDictionary:
    characters: list[int]
    staffs: list[int]


class AnimeCharacterAndStaffListParser(BaseParser):
    def __init__(self, html: str) -> None:
        super().__init__()
        self.parser = self.get_parser(html)

    @property
    @return_on_error([])
    def get_characters(self) -> list[int]:
        anchor_tags = self.parser.css("a[href*='/character/']")
        return sorted(
            {
                self.regex_helper.get_first_integer_from_url(anchor.attributes["href"])
                for anchor in anchor_tags
            }
        )

    @property
    @return_on_error([])
    def get_staffs(self) -> list[int]:
        anchor_tags = self.parser.css("a[href*='/people/']")
        return sorted(
            {
                self.regex_helper.get_first_integer_from_url(anchor.attributes["href"])
                for anchor in anchor_tags
            }
        )

    def build_dictionary(self) -> AnimeCharacterAndStaffListDictionary:
        dictionary = {
            "characters": self.get_characters,
            "staffs": self.get_staffs,
        }
        return dictionary
