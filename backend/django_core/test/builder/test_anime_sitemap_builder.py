from builder.sitemap import SitemapBuilder


def test_character_sitemap_builder():
    builder = SitemapBuilder("https://myanimelist.net/sitemap/index.xml")
    data = builder.build(filter="anime")
    assert "https://myanimelist.net/anime/33950/Black_Clover" in data
    assert (
        "https://myanimelist.net/anime/8861/Yosuga_no_Sora__In_Solitude_Where_We_Are_Least_Alone"
        in data
    )
    assert "https://myanimelist.net/anime/20/Naruto" in data
    assert "https://myanimelist.net/anime/21/One_Piece" in data
    # assert (
    #     "https://myanimelist.net/anime/35851/Sayonara_no_Asa_ni_Yakusoku_no_Hana_wo_Kazarou"
    #     in data
    # )
