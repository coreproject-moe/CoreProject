from django.apps import AppConfig


class AnimeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.anime"

    def ready(self) -> None:
        from . import signals  # noqa
