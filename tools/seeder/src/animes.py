import httpx, asyncio
import sys
from ._conf import (
    ANIME_GENRE_ENDPOINT,
    ANIME_THEME_ENDPOINT,
    PRODUCER_ENDPOINT,
    CHARACTER_ENDPOINT,
)
from ._session import session
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


async def get_studio_or_producer_mapping(mal_id):
    res = await client.get(
        PRODUCER_ENDPOINT,
        params={
            "mal_id": mal_id,
        },
    )
    json = res.json()
    # Could return multiple
    data = json["items"][0]
    return data["id"]


async def get_character_mapping(mal_id):
    res = await client.get(
        CHARACTER_ENDPOINT,
        params={
            "mal_id": mal_id,
        },
    )
    json = res.json()
    # Could return multiple
    data = json["items"][0]
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
        *[
            get_studio_or_producer_mapping(data["mal_id"])
            for data in item.get("studios")
        ]
    )
    mapping["producers"] = await asyncio.gather(
        *[
            get_studio_or_producer_mapping(data["mal_id"])
            for data in item.get("producers")
        ]
    )

    # Get Characters
    characters_res = session.get(f'{BASE_URL}/{item["mal_id"]}/characters')
    character_res_json = characters_res.json()
    mapping["characters"] = await asyncio.gather(
        *[
            get_character_mapping(data["character"]["mal_id"])
            for data in character_res_json["data"]
        ]
    )

    print(mapping)
    sys.exit(0)


async def command() -> None:
    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(0, int(total_pages)):
        __res__ = await client.get(BASE_URL, params={"page": page})
        data = __res__.json()
        asyncio.gather(*[post_to_backend(item) for item in data["data"]])
