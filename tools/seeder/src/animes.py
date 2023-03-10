import httpx, asyncio

from datetime import datetime

BASE_URL = "https://api.jikan.moe/v4/anime"

client = httpx.AsyncClient()
GENRE_URL = ''
async def get_genre_mapping(mal_id):
    client.get('')


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

    try:
        mapping["aired_from"] = datetime.strptime(
            item.get("aired")["from"], "%Y-%m-%dT%H:%M:%SZ"
        )
    except:
        pass

    try:
        mapping["aired_to"] = datetime.strptime(
            item.get("aired")["to"], "%Y-%m-%dT%H:%M:%SZ"
        )
    except:
        pass

    try:
        mapping["genres"] = await asyncio.gather(
            *[get_genre_mapping(data["mal_id"]) for data in item.get("genres")]
        )
    except:
        pass


async def command() -> None:

    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(0, int(total_pages)):
        __res__ = await client.get(f"https://api.jikan.moe/v4/anime?page={page}")
        data = __res__.json()
        asyncio.gather(*[post_to_backend(item) for item in data["data"]])
