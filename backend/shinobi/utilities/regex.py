import re


class RegexHelper:
    def get_id_from_url(self, url) -> int:
        _match = re.search(r"/(\d+)/", url)
        _id = _match.group(1)
        if not _id.isdigit():
            raise Exception("Id is not a digit.")

        return _id

    def get_content_between_first_brackets(self, text: str) -> str:
        return re.search(r"\((.*?)\)", text).group(1)

    def replace_br_with_newline(self, text: str) -> str:
        return re.sub(r"<br\s*\/?>", "\n", text)
