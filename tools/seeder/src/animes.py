import httpx, asyncio
from ._conf import (
    ANIME_GENRE_ENDPOINT,
    ANIME_THEME_ENDPOINT,
    PRODUCER_ENDPOINT,
    CHARACTER_ENDPOINT,
    ANIME_ENDPOINT,
    TOKEN,
)
from ._session import session
from dateutil import parser
import contextlib
from bing_image_downloader import downloader
from io import BytesIO

BASE_URL = "https://api.jikan.moe/v4/anime"

client = httpx.AsyncClient()


def image_downloader(term: str, output_dir: str = "images"):
    return downloader.download(
        term,
        limit=1,
        output_dir=output_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True,
    )


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
    print(f"Got `genre` data for {mal_id}")
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
    print(f"Got `theme` data for {mal_id}")
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
    print(f"Got `studio`|`producer` data for {mal_id}")
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
    print(f"Got `character` data for {mal_id}")
    return data["id"]


async def post_to_backend(item):
    print(f"Got starting point for {item.get('mal_id')}")
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

    try:
        image_url = item["images"]["webp"]["image_url"]
    except KeyError:
        image_url = item["images"]["jpg"]["image_url"]
    finally:
        image = session.get(image_url)

    # Search for a good 4k cover
    search_term = f"{item.get('title')} Wallpaper 4k"
    image_downloader(search_term)

    files = {
        # Small
        "banner": BytesIO(
            image.content,
        ),
        # Large
        "cover": open(f"./images/{search_term}/Image_1.jpg", "rb"),
    }
    await client.post(
        ANIME_ENDPOINT,
        files=files,
        data=mapping,
        headers={
            "Authorization": f"Bearer {TOKEN}",
        },
    )

    print("Seeded Anime for {} | Mal ID : {}".format(item.get("title"), item["mal_id"]))


async def command() -> None:
    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(0, int(total_pages)):
        __res__ = session.get(BASE_URL, params={"page": page})
        data = __res__.json()
        asyncio.gather(*[post_to_backend(item) for item in data["data"] if data])
