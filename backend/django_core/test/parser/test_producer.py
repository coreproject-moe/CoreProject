from parser.producer import ProducerParser

import httpx
import datetime


def get_producer_res_given_mal_id(mal_id: int) -> httpx.Response:
    return httpx.get(f"https://myanimelist.net/anime/producer/{mal_id}")
