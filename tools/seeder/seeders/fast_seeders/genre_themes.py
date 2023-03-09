from typing import List
import httpx
import json
import asyncio
import re
from selectolax.parser import HTMLParser
from functools import partial
import dotenv
import os

dotenv.load_dotenv()
AUTHBEARER = os.getenv("AUTHBEARER")

HEADERS = {
    "authorization": f"Bearer {AUTHBEARER}",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}


async def get_genres() -> List[dict]:
    async with httpx.AsyncClient() as client:
        genres_data = await client.get("https://api.jikan.moe/v4/genres/anime")
        genres_data = genres_data.json()
        return [
            {"mal_id": genre["mal_id"], "name": genre["name"]}
            for genre in genres_data["data"]
        ]


async def async_get_themes() -> list[dict]:
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://myanimelist.net/anime.php")
    pattern = re.compile(r"^(.*) \(([\d,]+)\)$")

    themes_header = [
        header
        for header in HTMLParser(resp.text).css("div.normal_header")
        if header.text() == "Themes"
    ][0]
    themes_raw = themes_header.css_first("div + div").css(
        "div.genre-list.al a.genre-name-link"
    )

    themes = []
    for theme in themes_raw:
        if match := pattern.search(theme.text()):
            name = match[1]
            theme_id = theme.attributes["href"].split("/")[-2]
            themes.append({"mal_id": theme_id, "name": name})
        else:
            print(f"Failed to parse line: {theme.text()}")
    return themes


async def post_data(api_url: str, data: dict):
    data[0]["type"] = "Anime"
    data = json.dumps(data)
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, data=data, headers=HEADERS)
        print(response.status_code)


async def post_to_api(url: str, items: list):
    print("Posting to API:", url)
    post_data_func = partial(post_data, url)
    await asyncio.gather(*[post_data_func([item]) for item in items])


async def main():
    themes = await async_get_themes()
    await post_to_api("https://backend.coreproject.moe/api/v1/anime/themes", themes)
    genres = await get_genres()
    await post_to_api("https://backend.coreproject.moe/api/v1/anime/genres", genres)


if __name__ == "__main__":
    asyncio.run(main())
