from shinobi.parser.genre import AnimeGenreParser
from shinobi.utilities.session import session

res = session.get("https://myanimelist.net/anime/genre/1")


def test_anime_genre_parser() -> None:
    parser = AnimeGenreParser(res.text)
    data = parser.build_dictionary()

    assert int(data["mal_id"]) == 1
    assert data["name"] == "Action"
    assert (
        data["description"]
        == "Exciting action sequences take priority and significant conflicts between characters are usually resolved with one's physical power. While the overarching plot may involve one group against another, the narrative in action stories is always focused on the strengths/weaknesses of individual characters and the effort they put into their personal battles with the opposing group's members.\n\nContrast with Military or Sports where the narrative is on collective achievement, or monster-of-the-week where the brief action scenes are a predicted climax to the episode's plot."
    )
    assert data["type"] == "Anime"
