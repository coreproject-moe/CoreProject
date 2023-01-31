import re

KOKORO_WORD_COLOR_MAP: dict[str, str] = {
    "-": "white",
    "a": "white",
    "c": "white",
    "h": "white",
    "k": "white",
    "n": "white",
    "o": "yellow",
    "r": "white",
}

TAILWIND_COLOR_MAP: dict[str, str] = {
    "white": "text-white",
    "yellow": "text-warning",
}

KOKORO_REGEX = re.compile(r"kokoro-chan", re.M)


def format_kokoro_color(input: str) -> str:
    color_formated_string = ""

    # This variable has ['kokoro-chan']
    regex_words: list[str] = re.findall(KOKORO_REGEX, input)
    # First parse the word list
    # ( there could be multiple occurances of the word 'kokoro')
    for word in regex_words:
        # Parse each word in the occurances
        for letter in word:
            color = KOKORO_WORD_COLOR_MAP.get(letter)
            color_class = TAILWIND_COLOR_MAP.get(color)
            color_formated_string += (
                f"<span class='inline-flex {color_class}'>{letter}</span>"
            )

    # Color the font.
    input = re.sub(KOKORO_REGEX, color_formated_string, input)
    # Hyperlink the home
    return input
