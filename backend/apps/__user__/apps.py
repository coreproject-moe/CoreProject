from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.__user__"

    def ready(self):
        import apps.__user__.signals
