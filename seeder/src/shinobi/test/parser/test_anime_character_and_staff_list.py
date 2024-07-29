from shinobi.parser.anime_character_and_staff_list import (
    AnimeCharacterAndStaffListParser,
)
from shinobi.utilities.session import session

res = session.get("https://myanimelist.net/anime/1/")


def test_first_anime_character_list() -> None:
    parser = AnimeCharacterAndStaffListParser(res.text)
    data = parser.build_dictionary()

    assert data["characters"] == [
        1,
        2,
        3,
        4,
        16,
        40,
        62,
        71,
        417,
        2734,
        2735,
        2736,
        23740,
        29313,
        45627,
    ]
    assert data["staffs"] == [
        11,
        14,
        84,
        179,
        203,
        262,
        330,
        357,
        497,
        658,
        2009,
        6519,
        40009,
    ]
