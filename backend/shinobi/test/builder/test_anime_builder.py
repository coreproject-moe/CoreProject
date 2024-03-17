import pytest

from shinobi.builder.anime import AnimeBuilder


@pytest.mark.long
def test_anime_dictionary_builder() -> None:
    builder = AnimeBuilder()
    dictionary = builder.build_dictionary(excluded_ids=[54915])

    dictionary_keys = list(dictionary.keys())
    dictionary_values = list(dictionary.values())

    assert 54915 not in list(dictionary_keys)

    assert (
        "https://myanimelist.net/anime/36305/Zutto_Mae_kara_Suki_deshita_Kokuhaku_Jikkou_Iinkai__Kinyoubi_no_Ohayou"
        in dictionary_values
    )
    assert (
        "https://myanimelist.net/anime/30831/Kono_Subarashii_Sekai_ni_Shukufuku_wo"
        in dictionary_values
    )
