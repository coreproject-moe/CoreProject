from functools import partial

from apps.user.models import CustomUser

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


class Token(models.Model):
    token = models.CharField(
        default=partial(
            get_random_string,
            16,
        ),
        unique=True,
        max_length=16,
        editable=False,
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"User : {self.user.username} | Token : {self.token}"

    class Meta:
        indexes = [
            models.Index(fields=["token"]),
        ]
        verbose_name = _("token")
        verbose_name_plural = _("tokens")
