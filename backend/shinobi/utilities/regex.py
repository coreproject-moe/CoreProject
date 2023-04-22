import re


class RegexHelper:
    # Getters
    # -------
    def get_id_from_url(self, url: str) -> int:
        pattern = re.compile(r"/(\d+)/")
        _match = re.search(pattern, url)
        _id = _match.group(1)
        if not _id.isdigit():
            raise Exception("Id is not a digit.")

        return int(_id)

    def get_content_between_first_brackets(self, text: str) -> str:
        pattern = re.compile(r"\((.*?)\)")
        return re.search(pattern, text).group(1)

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
