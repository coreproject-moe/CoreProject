from settings import MODELS, DATABASE_URL

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
