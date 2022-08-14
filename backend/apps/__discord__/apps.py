from django.apps import AppConfig
from threading import Thread


class DiscordConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.__discord__"

    def ready(self) -> None:
        """"""
        # Call discord funtion here
        # Thread(target=).start()
