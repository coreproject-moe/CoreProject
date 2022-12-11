from django.apps import AppConfig
from typing import NoReturn, Self


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"

    def ready(self: Self) -> NoReturn:
        from . import signals  # noqa
