from pathlib import Path

# Goes to the directory where `server.py` is present
BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIRS = str(
    BASE_DIR.joinpath("templates"),
)

# Goes to the directory where pipfile is present
DJANGO_DIR = BASE_DIR.parent.joinpath("django_core")
DJANGO_MEDIA_DIR = str(DJANGO_DIR.joinpath("media"))

# Postgres
POSTGRES = {
    "NAME": "discord-py",
    "USER": "postgres",
    "PASSWORD": "supersecretpassword",
    "HOST": "",
    "PORT": "",
}
