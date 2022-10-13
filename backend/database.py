DATABASE_URL = "sqlite://db.sqlite3"
MODELS = [
    "models.user",
]

TORTOISE_ORM = {
    "connections": {
        "default": DATABASE_URL,
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                # User models
            ]
            + MODELS,
            "default_connection": "default",
        },
    },
}
