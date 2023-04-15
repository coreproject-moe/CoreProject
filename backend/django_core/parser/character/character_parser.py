from selectolax.parser import HTMLParser
import re
from typing import List, Dict, Union


class CharacterParser:
    def __init__(self, html: str) -> None:
        self.html: str = html
        self.parser: HTMLParser = self.get_parser()

    def get_parser(self) -> HTMLParser:
        return HTMLParser(self.html)

    @staticmethod
    def parse_mal_id(url: str) -> int:
        return int(url.split("/")[-2])

    def get_mal_id(self) -> int:
        return self.parse_mal_id(
            self.parser.css_first("meta[property='og:url']").attributes["content"]
        )

    def get_character_url(self) -> str:
        return self.parser.css_first("meta[property='og:url']").attributes["content"]

    def get_title(self) -> str:
        return self.parser.css_first("meta[property='og:title']").attributes["content"]

    def get_kanji_title(self) -> str:
        try:
            return self.parser.css_first("h2.normal_header span small").text().strip("()")
        except Exception:
            return ""

    def get_about(self) -> str:
        try:
            text = self.parser.css_first("#content > table tr > td:nth-child(2)").text()
            return re.search(r"<br><br(.*?)<br><br>", text)[0].strip("<br><br>")
        except Exception:
            return ""

    def get_nicknames(self) -> List[str]:
        try:
            aliases = self.parser.css_first("h1").text().strip()
            aliases = aliases[aliases.find('"') + 1 : aliases.rfind('"')].strip()
            return aliases.split(", ")
        except Exception:
            return []

    def get_member_favorites_count(self) -> int:
        try:
            pattern = r"Member Favorites: (\d+,?\d+)"
            match = re.search(pattern, self.html)
            return int(re.search(r"\d+,?\d+", match[0])[0].replace(",", ""))
        except Exception:
            return None

    def get_image(self) -> str:
        try:
            return self.parser.css_first("meta[property='og:image']").attributes["content"]
        except Exception:
            return ""

    def get_animeography(self) -> List[int]:
        try:
            anime_links = {
                link
                for link in self.parser.css("td.borderClass tr a")
                if "/anime/" in link.attributes.get("href", "")
            }

            return list(
                {self.parse_mal_id(link.attributes["href"]) for link in anime_links}
            )
        except Exception:
            return []

    def get_mangagraphy(self) -> List[int]:
        try:
            manga_links = [
                link
                for link in self.parser.css("td.borderClass tr a")
                if "/manga/" in link.attributes.get("href", "")
            ]
            return list(
                {self.parse_mal_id(link.attributes["href"]) for link in manga_links}
            )
        except Exception:
            return []

    def get_voice_actors(self) -> List[Dict[str, Union[str, int]]]:
        try:
            return [
                {
                    "language": td.css_first("small").text(),
                    "mal_id": self.parse_mal_id(td.css_first("a").attributes["href"]),
                }
                for td in self.parser.css("table > tbody > tr > td:nth-child(2)")
                if "/people/" in td.css_first("a").attributes["href"]
            ]
        except Exception:
            return []

    def get_character(self) -> dict[str, str | int]:
        return {
            "url": self.get_character_url(),
            "about": self.get_about(),
            "title": self.get_title(),
            "mal_id": self.get_mal_id(),
            "kanji_title": self.get_kanji_title(),
            "nicknames": self.get_nicknames(),
            "favorite": self.get_member_favorites_count(),
            "image": self.get_image(),
            "animeography": self.get_animeography(),
            "mangaography": self.get_mangagraphy(),
            "voice_actors": self.get_voice_actors(),
        }
