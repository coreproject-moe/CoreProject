import datetime

import httpx

from shinobi.parser.producer import ProducerParser


def get_producer_res_given_mal_id(mal_id: int) -> httpx.Response:
    return httpx.get(f"https://myanimelist.net/anime/producer/{mal_id}")


def test_first_producer_parser():
    res = get_producer_res_given_mal_id(1)
    parser = ProducerParser(res.text)

    data = parser.build_dictionary()

    assert data["mal_id"] == "1"
    assert data["mal_id"].isdigit()
    assert data["name"] == "Pierrot"
    assert data["name_japanese"] == "ぴえろ"
    assert data["established"] == datetime.datetime(1979, 5, 22, 0, 0)
    assert (
        data["about"]
        == "Pierrot ぴえろ (Pierrot Co., Ltd.) is a Japanese animation studio established in May 1979 by former employees of both Tatsunoko Production and Mushi Production. Its headquarters are located in Mitaka, Tokyo. Pierrot is renowned for several worldwide popular anime series, such as Naruto, Bleach, Yu Yu Hakusho, Black Clover, Boruto: Naruto Next Generations, Tokyo Ghoul, and Great Teacher Onizuka."
    )
