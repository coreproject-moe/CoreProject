
import httpx


def get_producer_res_given_mal_id(mal_id: int) -> httpx.Response:
    return httpx.get(f"https://myanimelist.net/anime/producer/{mal_id}")
