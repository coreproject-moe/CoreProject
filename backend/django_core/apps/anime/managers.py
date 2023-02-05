from typing import TYPE_CHECKING, Any

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from .models import AnimeModel


class AnimeManager(models.Manager["AnimeModel"]):
    # mypy: ignore-type
    def get_username_with_discriminator(
        self,
        prefix: str = "",
    ) -> models.QuerySet["AnimeModel"]:
        prefix = prefix + "__" if prefix else ""
        pass
