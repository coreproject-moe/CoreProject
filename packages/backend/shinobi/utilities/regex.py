import re


class RegexHelper:
    # Getters
    # -------
    def get_id_from_url(self, url: str) -> int:
        pattern = re.compile(r"/(\d+)/")

        _match = re.search(pattern, url)
        if not _match:
            raise Exception("No match found")

        _id_ = _match.group(1)
        if not _id_.isdigit():
            raise Exception("Id is not a digit.")

        return int(_id_)

    def get_content_between_first_brackets(self, text: str) -> str:
        pattern = re.compile(r"\((.*?)\)")
        if content := re.search(pattern, text):
            return content.group(1)
        else:
            raise Exception("No content found")

    def get_first_integer_from_url(self, text: str) -> int:
        pattern = r"\/(\d+)\/"
        _matches = re.search(pattern, text)
        _id = _matches.group(1)
        if not _id.isdigit():
            raise Exception("Id is not a digit.")

        return int(_id)

    # Checks
    # -------
    def check_if_string_contains_integer(self, string: str) -> bool:
        pattern = re.compile(r"\d+")
        return bool(re.search(pattern, string))

    def check_if_string_contains_bracket(self, string: str) -> bool:
        pattern = re.compile(r"\[\d+\]")
        return bool(re.search(pattern, string))

    # Replacements
    # ------------
    def replace_br_with_newline(self, text: str) -> str:
        return re.sub(r"<br\s*\/?>", "\n", text)

    def remove_anime_from_the_end_of_a_string(self, text: str) -> str:
        pattern = r"(.*?)\sAnime"

        return re.sub(pattern, r"\1", text)
