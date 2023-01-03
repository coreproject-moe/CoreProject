from typing import NoReturn, Self

from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"

    def ready(self: Self) -> NoReturn:
        from . import signals  # noqa
