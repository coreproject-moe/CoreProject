import string

from selectolax.parser import HTMLParser

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.session import session
from shinobi.utilities.string import StringHelper


class CharacterBuilder:
    def __init__(self) -> None:
        self.anchors: list[str] = []
        self.visited_urls: set[str] = set()

        # Reusuable clients
        self.client = session

        # Facades
        self.regex_helper = RegexHelper()
        self.string_helper = StringHelper()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @return_on_error("")
    def has_next_page(self, html: str) -> bool:
        parser = self.get_parser(html)
        node = parser.css_first("div.normal_header > div.fl-r > div > span.bgColor1")

        select_node_list = node.text().split(" ")
        for item in select_node_list:
            if self.regex_helper.check_if_string_contains_bracket(item):
                bracketed_element_position = select_node_list.index(item)
                break

        if bracketed_element_position == len(select_node_list) - 1:
            return False

        return True

    def get_all_pages_in_span_tag(self, html: str) -> list[str]:
        parser = self.get_parser(html)
        node = (
            parser.css_first("div.normal_header > div.fl-r > div > span.bgColor1")
            .select("a")
            .matches
        )
        anchors = [anchor.attributes["href"] for anchor in node]
        return [item for item in anchors if item is not None]

    def _build_word_list(self) -> list[str]:
        alphabet_list = list(string.ascii_uppercase)
        return [
            f"https://myanimelist.net/character.php?letter={letter}"
            for letter in alphabet_list
        ]

    def __build_urls(self, url: str) -> None:
        self.visited_urls.add(url)

        res = self.client.get(url)
        html = res.text

        character_nodes = self.get_parser(html).css("a[href*='/character/']")

        if len(character_nodes) == 0:
            print(
                f"""
                Status : {res.status_code}
                URL : {url}
            """
            )

        for character_node in character_nodes:
            character_href = character_node.attributes["href"]
            if (
                character_href
                and character_href not in self.anchors
                and self.regex_helper.check_if_string_contains_integer(character_href)
            ):
                self.anchors.append(
                    self.string_helper.add_myanimelist_if_not_already_there(
                        character_href
                    )
                )

        if self.has_next_page(html):
            all_pages = self.get_all_pages_in_span_tag(html)
            for item in all_pages:
                myanimelist_formated_url = "https://myanimelist.net" + item
                if myanimelist_formated_url not in self.visited_urls:
                    next_url = myanimelist_formated_url
                    break

            self.__build_urls(next_url)

    def __build_ids(self) -> list[int]:
        return [
            self.regex_helper.get_first_integer_from_url(item) for item in self.anchors
        ]

    def build_dictionary(
        self, excluded_ids: list[int] | None = None, sort: bool = False
    ) -> dict[int, str]:
        for url in self._build_word_list():
            self.__build_urls(url)

        dictionary = dict(zip(self.__build_ids(), self.anchors))

        if sort:
            dictionary = dict(sorted(dictionary.items()))

        if excluded_ids:
            dictionary = {
                key: value
                for key, value in dictionary.items()
                if key not in excluded_ids
            }

        return dictionary
