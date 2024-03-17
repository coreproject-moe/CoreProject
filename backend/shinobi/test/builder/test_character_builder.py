import pytest

from shinobi.builder.character import CharacterBuilder


@pytest.mark.long
def test_character_dictionary_builder() -> None:
    builder = CharacterBuilder()
    dictionary = builder.build_dictionary(excluded_ids=[54915])

    dictionary_keys = list(dictionary.keys())
    dictionary_values = list(dictionary.values())

    assert 54915 not in dictionary_keys

    assert "https://myanimelist.net/character/117223/Aqua" in dictionary_values
    assert "https://myanimelist.net/character/206276/Hitori_Gotou" in dictionary_values
