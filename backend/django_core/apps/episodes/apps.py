from django.apps import AppConfig


class EpisodesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.episodes"

    def ready(self) -> None:
        from . import signals as signals
