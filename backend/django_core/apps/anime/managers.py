from typing import TYPE_CHECKING

from django.db import models
from django.db.models import CharField, Value, Func, F
from django.db.models.functions import Concat

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
                function="array_to_string",
                output_field=CharField(),
            ),
            names_and_name_synonyms_and_name_japanese_as_string=Concat(
                "name",
                Value(" "),
                "name_japanese",
                Value(" "),
                "name_synonyms_as_string",
            ),
        )
