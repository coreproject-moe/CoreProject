import httpx, asyncio
import sys
from ._conf import ANIME_GENRE_ENDPOINT, ANIME_THEME_ENDPOINT
from dateutil import parser
import contextlib

BASE_URL = "https://api.jikan.moe/v4/anime"

client = httpx.AsyncClient()


async def get_genre_mapping(mal_id):
    """Given `mal_id` return `pk`"""
    res = await client.get(
        ANIME_GENRE_ENDPOINT,
        params={
            "mal_id": mal_id,
        },
    )
    json = res.json()
    # Could return multiple
    data = json[0]
    return data["id"]


async def get_theme_mapping(mal_id):
    """Given `mal_id` return `pk`"""
    res = await client.get(
        ANIME_THEME_ENDPOINT,
        params={
            "mal_id": mal_id,
        },
    )
    json = res.json()
    # Could return multiple
    data = json[0]
    return data["id"]


async def post_to_backend(item):
    mapping = {
        "mal_id": item["mal_id"],
        "name": item.get("title"),
        "name_japanese": item.get("title_japanese"),
        "name_synonyms": item.get("title_synonyms"),
        "source": item.get("source"),
        "synopsis": item.get("synopsis"),
        "background": item.get("background"),
        "rating": item.get("rating"),
    }
    with contextlib.suppress(TypeError):
        mapping["aired_from"] = parser.parse(item.get("aired")["from"])
        mapping["aired_to"] = parser.parse(item.get("aired")["to"])

    mapping["genres"] = await asyncio.gather(
        *[get_genre_mapping(data["mal_id"]) for data in item.get("genres")]
    )
    mapping["themes"] = await asyncio.gather(
        *[get_theme_mapping(data["mal_id"]) for data in item.get("themes")]
    )

    mapping["studios"] = await asyncio.gather(
        *[get_studio_mapping(data["mal_id"]) for data in item.get("studios")]
    )


async def command() -> None:
    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(0, int(total_pages)):
        __res__ = await client.get(f"https://api.jikan.moe/v4/anime?page={page}")
        data = __res__.json()
        asyncio.gather(*[post_to_backend(item) for item in data["data"]])
