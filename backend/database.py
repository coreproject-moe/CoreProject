from settings import DATABASE_URL, MODELS

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
