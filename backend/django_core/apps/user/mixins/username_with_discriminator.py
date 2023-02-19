from typing import TYPE_CHECKING

from django.conf import settings
from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad

if TYPE_CHECKING:
    from ..models import CustomUser


class UsernameWithDiscriminatorManager(models.Manager["CustomUser"]):
    # mypy: ignore-type
    def get_username_with_discriminator(
        self,
        prefix: str = "",
    ) -> models.QuerySet["CustomUser"]:
        prefix = prefix + "__" if prefix else ""
        return self.annotate(
            discriminator_as_string=Cast(
                f"{prefix}discriminator", output_field=CharField()
            ),
            username_with_discriminator=Concat(
                f"{prefix}username",
                Value("#"),
                LPad(
                    "discriminator_as_string",
                    int(settings.DISCRIMINATOR_LENGTH),
                    Value("0"),
                ),
                output_field=CharField(),
            ),
        )
