TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                # User models
                "models.user",
            ],
            "default_connection": "default",
        },
    },
}
