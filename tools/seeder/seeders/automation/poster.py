import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
}


def post_episode():
    ...
