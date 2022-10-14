from pathlib import Path

# Base path
BASE_DIR = Path(__file__).parent.parent
STATIC_DIR = BASE_DIR.joinpath("static")
TEMPLATE_DIR = BASE_DIR.joinpath("templates")

# Database configuration
DATABASE_URL = f"sqlite://{BASE_DIR}/db.sqlite3"
MODELS = [
    "models.user",
]

# Custom values
USERNAME_DISCRIMINATOR_LENGTH = 4
CACHE_MIDDLEWARE_SECONDS = 0

# Static Url
STATIC_URL = "/static"  # https://static.example.com | Prod
