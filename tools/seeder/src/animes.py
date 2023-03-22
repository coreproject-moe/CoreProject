import httpx, asyncio
import sys
from ._conf import ANIME_GENRE_ENDPOINT
from dateutil import parser

BASE_URL = "https://api.jikan.moe/v4/anime"
# test = {
#     "mal_id": 1,
#     "url": "https://myanimelist.net/anime/1/Cowboy_Bebop",
#     "images": {
#         "jpg": {
#             "image_url": "https://cdn.myanimelist.net/images/anime/4/19644.jpg",
#             "small_image_url": "https://cdn.myanimelist.net/images/anime/4/19644t.jpg",
#             "large_image_url": "https://cdn.myanimelist.net/images/anime/4/19644l.jpg",
#         },
#         "webp": {
#             "image_url": "https://cdn.myanimelist.net/images/anime/4/19644.webp",
#             "small_image_url": "https://cdn.myanimelist.net/images/anime/4/19644t.webp",
#             "large_image_url": "https://cdn.myanimelist.net/images/anime/4/19644l.webp",
#         },
#     },
#     "trailer": {
#         "youtube_id": "qig4KOK2R2g",
#         "url": "https://www.youtube.com/watch?v=qig4KOK2R2g",
#         "embed_url": "https://www.youtube.com/embed/qig4KOK2R2g?enablejsapi=1&wmode=opaque&autoplay=1",
#         "images": {
#             "image_url": "https://img.youtube.com/vi/qig4KOK2R2g/default.jpg",
#             "small_image_url": "https://img.youtube.com/vi/qig4KOK2R2g/sddefault.jpg",
#             "medium_image_url": "https://img.youtube.com/vi/qig4KOK2R2g/mqdefault.jpg",
#             "large_image_url": "https://img.youtube.com/vi/qig4KOK2R2g/hqdefault.jpg",
#             "maximum_image_url": "https://img.youtube.com/vi/qig4KOK2R2g/maxresdefault.jpg",
#         },
#     },
#     "approved": True,
#     "titles": [
#         {"type": "Default", "title": "Cowboy Bebop"},
#         {"type": "Japanese", "title": "カウボーイビバップ"},
#         {"type": "English", "title": "Cowboy Bebop"},
#     ],
#     "title": "Cowboy Bebop",
#     "title_english": "Cowboy Bebop",
#     "title_japanese": "カウボーイビバップ",
#     "title_synonyms": [],
#     "type": "TV",
#     "source": "Original",
#     "episodes": 26,
#     "status": "Finished Airing",
#     "airing": False,
#     "aired": {
#         "from": "1998-04-03T00:00:00+00:00",
#         "to": "1999-04-24T00:00:00+00:00",
#         "prop": {
#             "from": {"day": 3, "month": 4, "year": 1998},
#             "to": {"day": 24, "month": 4, "year": 1999},
#         },
#         "string": "Apr 3, 1998 to Apr 24, 1999",
#     },
#     "duration": "24 min per ep",
#     "rating": "R - 17+ (violence & profanity)",
#     "score": 8.75,
#     "scored_by": 896602,
#     "rank": 39,
#     "popularity": 43,
#     "members": 1738967,
#     "favorites": 77073,
#     "synopsis": "Crime is timeless. By the year 2071, humanity has expanded across the galaxy, filling the surface of other planets with settlements like those on Earth. These new societies are plagued by murder, drug use, and theft, and intergalactic outlaws are hunted by a growing number of tough bounty hunters.\n\nSpike Spiegel and Jet Black pursue criminals throughout space to make a humble living. Beneath his goofy and aloof demeanor, Spike is haunted by the weight of his violent past. Meanwhile, Jet manages his own troubled memories while taking care of Spike and the Bebop, their ship. The duo is joined by the beautiful con artist Faye Valentine, odd child Edward Wong Hau Pepelu Tivrusky IV, and Ein, a bioengineered Welsh Corgi.\n\nWhile developing bonds and working to catch a colorful cast of criminals, the Bebop crew's lives are disrupted by a menace from Spike's past. As a rival's maniacal plot continues to unravel, Spike must choose between life with his newfound family or revenge for his old wounds.\n\n[Written by MAL Rewrite]",
#     "background": "When Cowboy Bebop first aired in spring of 1998 on TV Tokyo, only episodes 2, 3, 7-15, and 18 were broadcast, it was concluded with a recap special known as Yose Atsume Blues. This was due to anime censorship having increased following the big controversies over Evangelion, as a result most of the series was pulled from the air due to violent content. Satellite channel WOWOW picked up the series in the fall of that year and aired it in its entirety uncensored. Cowboy Bebop was not a ratings hit in Japan, but sold over 19,000 DVD units in the initial release run, and 81,000 overall. Protagonist Spike Spiegel won Best Male Character, and Megumi Hayashibara won Best Voice Actor for her role as Faye Valentine in the 1999 and 2000 Anime Grand Prix, respectively. Cowboy Bebop's biggest influence has been in the United States, where it premiered on Adult Swim in 2001 with many reruns since. The show's heavy Western influence struck a chord with American viewers, where it became a \"gateway drug\" to anime aimed at adult audiences.",
#     "season": "spring",
#     "year": 1998,
#     "broadcast": {
#         "day": "Saturdays",
#         "time": "01:00",
#         "timezone": "Asia/Tokyo",
#         "string": "Saturdays at 01:00 (JST)",
#     },
#     "producers": [
#         {
#             "mal_id": 23,
#             "type": "anime",
#             "name": "Bandai Visual",
#             "url": "https://myanimelist.net/anime/producer/23/Bandai_Visual",
#         }
#     ],
#     "licensors": [
#         {
#             "mal_id": 102,
#             "type": "anime",
#             "name": "Funimation",
#             "url": "https://myanimelist.net/anime/producer/102/Funimation",
#         },
#         {
#             "mal_id": 233,
#             "type": "anime",
#             "name": "Bandai Entertainment",
#             "url": "https://myanimelist.net/anime/producer/233/Bandai_Entertainment",
#         },
#     ],
#     "studios": [
#         {
#             "mal_id": 14,
#             "type": "anime",
#             "name": "Sunrise",
#             "url": "https://myanimelist.net/anime/producer/14/Sunrise",
#         }
#     ],
#     "genres": [
#         {
#             "mal_id": 1,
#             "type": "anime",
#             "name": "Action",
#             "url": "https://myanimelist.net/anime/genre/1/Action",
#         },
#         {
#             "mal_id": 46,
#             "type": "anime",
#             "name": "Award Winning",
#             "url": "https://myanimelist.net/anime/genre/46/Award_Winning",
#         },
#         {
#             "mal_id": 24,
#             "type": "anime",
#             "name": "Sci-Fi",
#             "url": "https://myanimelist.net/anime/genre/24/Sci-Fi",
#         },
#     ],
#     "explicit_genres": [],
#     "themes": [
#         {
#             "mal_id": 50,
#             "type": "anime",
#             "name": "Adult Cast",
#             "url": "https://myanimelist.net/anime/genre/50/Adult_Cast",
#         },
#         {
#             "mal_id": 29,
#             "type": "anime",
#             "name": "Space",
#             "url": "https://myanimelist.net/anime/genre/29/Space",
#         },
#     ],
#     "demographics": [],
# }
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

    mapping["aired_from"] = parser.parse(item.get("aired")["from"])

    mapping["aired_to"] = parser.parse(item.get("aired")["to"])

    mapping["genres"] = await asyncio.gather(
        *[get_genre_mapping(data["mal_id"]) for data in item.get("genres")]
    )

    print(mapping)


async def command() -> None:
    _res_ = await client.get(BASE_URL)
    total_pages = _res_.json()["pagination"]["last_visible_page"]

    for page in range(0, int(total_pages)):
        __res__ = await client.get(f"https://api.jikan.moe/v4/anime?page={page}")
        data = __res__.json()
        asyncio.gather(*[post_to_backend(item) for item in data["data"]])
