# https://www.educative.io/answers/how-to-convert-hex-to-rgb-and-rgb-to-hex-in-python


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    return ("{:X}{:X}{:X}").format(red, green, blue)
