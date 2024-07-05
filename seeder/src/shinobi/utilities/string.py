import html
import re


class StringHelper:
    def cleanse(self, string: str) -> str:
        # Convert any HTML line breaks to newlines
        string = re.sub(r"<br\s*/?>", "\n", string)

        # Convert non-breaking spaces to spaces
        string = string.replace("\xa0", " ")

        # Strip any remaining HTML tags
        string = html.unescape(string)  # Decode HTML entities
        string = re.sub(r"<[^>]*>", "", string)

        # Remove newlines at the end
        string = string.rstrip("\n")

        # Trim whitespace
        string = string.strip()

        return string

    @staticmethod
    def add_myanimelist_if_not_already_there(url: str) -> str:
        if "myanimelist.net" not in url:
            return "https://myanimelist.net" + url
        else:
            return url
