from builder.anime import AnimeBuilder


def test_anime_builder():
    builder = AnimeBuilder()

    urls = builder.build_urls()

    assert (
        "https://myanimelist.net/anime/36305/Zutto_Mae_kara_Suki_deshita_Kokuhaku_Jikkou_Iinkai__Kinyoubi_no_Ohayou"
        in urls
    )
    assert (
        "https://myanimelist.net/anime/30831/Kono_Subarashii_Sekai_ni_Shukufuku_wo" in urls
    )
