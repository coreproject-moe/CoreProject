import os

from dotenv import load_dotenv

load_dotenv()


TOKEN = os.environ.get("TOKEN")

# URLS
BASE_URL = "https://backend.coreproject.moe/"
CHARACTER_ENDPOINT = BASE_URL + "api/v1/characters"
STAFF_ENDPOINT = BASE_URL + "api/v1/staffs"
ANIME_GENRE_ENDPOINT = BASE_URL + "api/v1/anime/genres"
ANIME_THEME_ENDPOINT = BASE_URL + "api/v1/anime/themes"
PRODUCER_ENDPOINT = BASE_URL + "api/v1/producers"
