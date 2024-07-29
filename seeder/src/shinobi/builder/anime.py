import string

from selectolax.parser import HTMLParser

from shinobi.decorators.return_error_decorator import return_on_error
from shinobi.utilities.regex import RegexHelper
from shinobi.utilities.session import session


class AnimeBuilder:
    def __init__(self) -> None:
        self.anchors: list[str] = []
        self.visited_urls: set[str] = set()

        # Reusuable clients
        self.client = session

        # Facades
        self.regex_helper = RegexHelper()

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

    @staticmethod
    def add_myanimelist_if_not_already_there(url: str) -> str:
        if "myanimelist.net" not in url:
            return "https://myanimelist.net" + url
        else:
            return url

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
        alphabet_list = list("." + string.ascii_uppercase)
        return [
            f"https://myanimelist.net/anime.php?letter={letter}"
            for letter in alphabet_list
        ]

    def __build_urls(self, url: str) -> None:
        self.visited_urls.add(url)

        res = self.client.get(url)
        html = res.text

        anime_nodes = self.get_parser(html).css("a[href*='/anime/']")

        for anime_node in anime_nodes:
            anime_href = anime_node.attributes["href"]
            if (
                anime_href
                and anime_href not in self.anchors
                and self.regex_helper.check_if_string_contains_integer(anime_href)
            ):
                self.anchors.append(
                    self.add_myanimelist_if_not_already_there(anime_href)
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
