import string
import httpx
from selectolax.parser import HTMLParser
import re
from decorators.return_error_decorator import return_on_error


class AnimeBuilder:
    def __init__(self) -> None:
        self.anchors = []
        self.visited_urls = set()

        # Reusuable clients
        self.client = httpx.Client()

    @staticmethod
    def get_parser(html: str) -> HTMLParser:
        return HTMLParser(html)

    @staticmethod
    def build_list():
        alphabet_list = list("." + string.ascii_uppercase)
        return [
            f"https://myanimelist.net/anime.php?letter={letter}" for letter in alphabet_list
        ]

    @staticmethod
    def check_if_string_contains_bracket(string: str) -> bool:
        pattern = re.compile(r"\[\d+\]")

        if re.search(pattern, string):
            return True

        return False

    @return_on_error("")
    def has_next_page(self, html: str) -> bool:
        parser = self.get_parser(html)
        node = parser.select("div.normal_header > .fl-r > div > span.bgColor1")

        if len(node.matches) > 1:
            raise AttributeError("More than one node found")

        select_node = node.matches[0]

        select_node_list = select_node.text().split(" ")
        for item in select_node_list:
            if self.check_if_string_contains_bracket(item):
                bracketed_element_position = select_node_list.index(item)
                break

        if bracketed_element_position == len(select_node_list) - 1:
            return False

        return True

    def get_all_pages_in_span_tag(self, html):
        parser = self.get_parser(html)
        node = (
            parser.css_first("div.normal_header > .fl-r > div > span.bgColor1")
            .select("a")
            .matches
        )
        anchors = [anchor.attributes["href"] for anchor in node]
        return anchors

    def _build_urls(self, url: str) -> None:
        # print(url)
        # print(self.visited_urls)
        self.visited_urls.add(url)

        res = self.client.get(url)
        html = res.content

        anime_nodes = self.get_parser(html).css("a[href*=anime]")
        for anime_node in anime_nodes:
            anime_href = anime_node.attributes["href"]
            if anime_href not in self.anchors:
                self.anchors.append(anime_href)

        if self.has_next_page(html):
            all_pages = self.get_all_pages_in_span_tag(html)

            next_url = list(set(all_pages) ^ self.visited_urls)[0]
            self._build_urls(f"https://myanimelist.net{next_url}")

    def build_urls(self):
        self._build_urls("https://myanimelist.net/anime.php?letter=.")
        print(self.anchors)
