import httpx, asyncio, os
from ._conf import (
    ANIME_GENRE_ENDPOINT,
    ANIME_THEME_ENDPOINT,
    PRODUCER_ENDPOINT,
    CHARACTER_ENDPOINT,
    ANIME_ENDPOINT,
    STAFF_ENDPOINT,
    TOKEN,
)

import yt_dlp
from ._session import session
from dateutil import parser
import contextlib
from bing_image_downloader import downloader
from io import BytesIO
from datetime import datetime
import json

BASE_URL = "https://api.jikan.moe/v4/anime"

client = httpx.AsyncClient()
MISSING_CHARACTER_ENRTIES = []
MISSING_GENRE_ENTRIES = []
MISSING_STUDIO_ENTRIES = []
MISSING_THEME_MAPPING = []
MISSING_STAFF_ENTRIES = []


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
    try:
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
    except IndexError:
        MISSING_GENRE_ENTRIES.append(mal_id)
        return ""


async def get_theme_mapping(mal_id):
    """Given `mal_id` return `pk`"""
    try:
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
    except IndexError:
        MISSING_THEME_MAPPING.append(mal_id)
        return ""


async def get_studio_or_producer_mapping(mal_id):
    try:
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
    except IndexError:
        MISSING_STUDIO_ENTRIES.append(mal_id)
        return ""


async def get_character_mapping(mal_id):
    try:
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
    except IndexError:
        MISSING_CHARACTER_ENRTIES.append(mal_id)
        return ""


async def get_staff_mapping(mal_id):
    try:
        res = await client.get(STAFF_ENDPOINT, params={"mal_id": mal_id})
        json = res.json()
        print(json)
        # Could return multiple
        data = json["items"][0]
        print(f"Got `staff` data for {mal_id}")
        return data["id"]
    except IndexError:
        MISSING_STAFF_ENTRIES.append(mal_id)


async def get_anime_opening_mapping(string):
    ydl_opts = {
        "default_search": "ytsearch",  # set the default search to YouTube
        "max_results": 1,  # limit to only one result
        "quiet": True,  # suppress console output
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(string, download=False)


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
        mapping["aired_from"] = datetime.isoformat(
            parser.parse(item.get("aired")["from"])
        )
        mapping["aired_to"] = datetime.isoformat(parser.parse(item.get("aired")["to"]))

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

    # Get Staffs
    staff_res = session.get(f'{BASE_URL}/{item["mal_id"]}/staff')
    staff_res_json = staff_res.json()
    mapping["staffs"] = await asyncio.gather(
        *[
            get_staff_mapping(data["person"]["mal_id"])
            for data in staff_res_json["data"]
        ]
    )

    # Get Characters
    characters_res = session.get(f'{BASE_URL}/{item["mal_id"]}/staffs')
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

    # res = await client.post(
    #     ANIME_ENDPOINT,
    #     files=files,
    #     data=mapping,
    #     headers={
    #         "Authorization": f"Bearer {TOKEN}",
    #     },
    # )
    # if not res.status_code == 200:
    #     raise Exception("This is not meant to happen")

    log_dictionary = {
        "MISSING_CHARACTER_ENRTIES": MISSING_CHARACTER_ENRTIES,
        "MISSING_GENRE_ENTRIES": MISSING_GENRE_ENTRIES,
        "MISSING_STUDIO_ENTRIES": MISSING_STUDIO_ENTRIES,
        "MISSING_THEME_MAPPING": MISSING_THEME_MAPPING,
        "MISSING_STAFF_ENTRIES": MISSING_STAFF_ENTRIES,
    }

    json.dump(
        log_dictionary,
        open("anime.lock", "w", encoding="utf-8"),
        indent=2,
    )
    print("Seeded Anime for {} | Mal ID : {}".format(item.get("title"), item["mal_id"]))


async def command() -> None:
    starting_page = 0
    # Load JSON file and get data from it
    if os.path.exists("anime.lock"):
        print("Lock file found. Do you want to use it?")
        global MISSING_CHARACTER_ENRTIES, MISSING_GENRE_ENTRIES, MISSING_STUDIO_ENTRIES, MISSING_THEME_MAPPING
        # While loop to ask for data
        while True:
            answer = input("\r").lower()

            if "y" in answer:
                data = json.load(open("anime.lock", encoding="utf-8"))
                starting_number = int(data.get("STARTING_NUMBER", starting_number))
                character_number = int(data.get("CHARACTER_NUMBER", character_number))

                MISSING_CHARACTER_ENRTIES = data.get(
                    "MISSING_CHARACTER_ENRTIES", MISSING_CHARACTER_ENRTIES
                )
                MISSING_GENRE_ENTRIES = data.get(
                    "MISSING_GENRE_ENTRIES", MISSING_GENRE_ENTRIES
                )
                MISSING_STUDIO_ENTRIES = data.get(
                    "MISSING_STUDIO_ENTRIES", MISSING_STUDIO_ENTRIES
                )
                MISSING_THEME_MAPPING = data.get(
                    "MISSING_THEME_MAPPING", MISSING_THEME_MAPPING
                )
                MISSING_STAFF_ENTRIES = data.get(
                    "MISSING_STAFF_ENTRIES", MISSING_STAFF_ENTRIES
                )

                break

            elif "n" in answer:
                break

    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(starting_page, int(total_pages)):
        __res__ = await client.get(BASE_URL, params={"page": page})
        data = __res__.json()

        for item in data["data"]:
            await post_to_backend(item)
            break
        break

        # asyncio.gather(*[post_to_backend(item) for item in data["data"]])
