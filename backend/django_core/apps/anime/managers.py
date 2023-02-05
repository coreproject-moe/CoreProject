from typing import TYPE_CHECKING, Any

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import CharField, Value, Func, F
from django.db.models.functions import Cast, Concat, LPad
from django.utils.translation import gettext_lazy as _

if TYPE_CHECKING:
    from .models import AnimeModel


class AnimeManager(models.Manager["AnimeModel"]):
    # We are concating all of these together
    # so that we can perform a trigram lookup on these fields
    def get_names_and_name_synonyms_and_name_japanese_as_string(
        self,
    ) -> models.QuerySet["AnimeModel"]:
        return self.annotate(
            # https://stackoverflow.com/a/53187585
            name_synonyms_as_string=Func(
                F("name_synonyms"),
                Value(" "),
                funtion="array_to_string",
                output_field=CharField(),
            ),
            names_and_name_synonyms_and_name_japanese_as_string=Concat(
                "name",
                Value(" "),
                "name_synonyms_as_string",
                Value(" "),
                "name_japanese",
            ),
        )
