import datetime

from shinobi.utilities.session import session
import requests
from shinobi.parser.producer import ProducerParser


def get_producer_res_given_mal_id(mal_id: int) -> requests.Response:
    return session.get(f"https://myanimelist.net/anime/producer/{mal_id}")


def test_first_producer_parser():
    res = get_producer_res_given_mal_id(1)
    parser = ProducerParser(res.text)

    data = parser.build_dictionary()

    assert data["mal_id"] == 1
    assert data["name"] == "Pierrot"
    assert data["name_japanese"] == "ぴえろ"
    assert data["established"] == datetime.datetime(1979, 5, 1, 0, 0)
