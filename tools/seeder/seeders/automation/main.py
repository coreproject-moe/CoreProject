import asyncio
from contextlib import suppress
from itertools import count
import random
import requests
import gogo_api
from typing import Dict, Optional
import streamsb
import streamtape
import subprocess
import dotenv
import os
import poster
from tools import downloader, select_highest_resolutions

dotenv.load_dotenv()


TOKEN = os.getenv("TOKEN")


def fetch_episode_summary(mal_id: str, episode: int) -> dict:
    print("getting episode summary")
    resp_json = requests.get(
        f"https://api.jikan.moe/v4/anime/{mal_id}/episodes/{episode}"
    ).json()
    print(resp_json)
    data = resp_json["data"]
    return {"episode_name": data["title"], "episode_summary": data["synopsis"]}


def is_anime_episode_available(anime_id: int, episode: int) -> bool:
    res = requests.get(
        f"https://backend.coreproject.moe/api/v1/anime/{anime_id}/episodes/{episode}"
    )
    return bool(res.ok)


def fetch_episodes(anime_id: int) -> list:
    response = gogo_api.get_anime(anime_id)
    return response["episodes"]


def get_download_link(anime_id: int, episode: int) -> str:
    return select_highest_resolutions(gogo_api.get_download_links(anime_id, episode))


def find_anime_by_name(anime_name: str) -> dict[str, str] | None:
    with suppress(Exception):
        search_url = f"https://backend.coreproject.moe/api/v1/anime?name={anime_name}"
        response = requests.get(search_url)
        return response.json()["items"][0]


def download_anime_episode(anime_id: int, episode_no: int) -> str:
    download_url = get_download_link(anime_id, episode_no)
    filename = f"{anime_id}_episode_{episode_no}.mp4"
    downloader(download_url, filename)
    return filename


def create_thumbnail(filename: str) -> str:
    cmd = f'ffprobe -i {filename} -show_entries format=duration -v quiet -of csv="p=0"'
    output = subprocess.check_output(cmd, shell=True)
    timestamp = random.randint(1, round(float(output)))
    image_name = f"{filename[:-3]}png"
    cmd = f"ffmpeg -ss {timestamp} -i {filename} -frames:v 1 {image_name}"
    subprocess.call(cmd, shell=True)
    return image_name


async def upload_file(filename: str):
    streamsb_file_code = await streamsb.upload_to_streamsb_by_file(filename)
    streamtape_file_code = await streamtape.upload_to_streamtape(filename)
    return {
        "streamsb_file_code": streamsb_file_code,
        "streamtape_file_code": streamtape_file_code,
    }


def upload_file_to_providers(filename: str):
    return asyncio.run(upload_file(filename))


def create_new_anime(name: str):
    ...


def process_anime_episodes(anime_name: str):  # sourcery skip: extract-method
    anime = find_anime_by_name(anime_name)
    if not anime:
        create_new_anime(anime_name)
        anime = find_anime_by_name(anime_name)
    if anime:
        anime_name = anime["name"]
        anime_name_ = anime_name.replace(" ", "-")
        mal_id = anime["mal_id"]
        anime_id = anime["id"]
        episodes = fetch_episodes(anime_name_)

        for episode_no in episodes:
            try:
                episode_no = episodes[1]
                if not is_anime_episode_available(mal_id, episode_no):
                    filename = download_anime_episode(anime_name_, episode_no)
                    thumbnail_path = create_thumbnail(
                        f"{anime_name_}_episode_{episode_no}.mp4"
                    )
                    summary = fetch_episode_summary(mal_id, episode_no)
                    episode_name = summary["episode_name"]
                    episode_summary = summary["episode_summary"]
                    providers = upload_file_to_providers(filename)
                    poster.post_episode(
                        anime_id=anime_id,
                        episode_no=episode_no,
                        thumbnail_path=thumbnail_path,
                        episode_name=episode_name,
                        summary_synopsis=episode_summary,
                        providers=providers,
                    )
            finally:
                with suppress(Exception):
                    os.remove(filename)
                    os.remove(thumbnail_path)


def scrape_anime_list():
    for page in count(1):
        animes = gogo_api.get_anime_list(page)
        if not animes:
            break
        for anime in animes:
            process_anime_episodes(anime["title"])


# if __name__ == "__main__":
#     scrape_anime_list()
