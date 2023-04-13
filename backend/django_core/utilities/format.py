import re

KOKORO_WORD_COLOR_MAP = {
    "-": "white",
    "a": "white",
    "c": "white",
    "h": "white",
    "k": "white",
    "n": "white",
    "o": "yellow",
    "r": "white",
}

TAILWIND_COLOR_MAP = {
    "white": "text-white",
    "yellow": "text-warning",
}

WORD = "kokoro-chan"


def format_kokoro_color(input: str) -> str:
    KOKORO_REGEX = re.compile(rf"{WORD}", re.M)

    color_formated_string = ""

    # This variable has ['kokoro-chan']
    re.findall(KOKORO_REGEX, input)

    # Parse each letter in the word
    for letter in WORD:
        color = KOKORO_WORD_COLOR_MAP.get(letter)
        color_class = TAILWIND_COLOR_MAP.get(color)
        color_formated_string += f"<span class='inline-flex {color_class}'>{letter}</span>"

    # Color the font.
    input = re.sub(KOKORO_REGEX, color_formated_string, input)
    # Hyperlink the home
    return input
