import string
import random

from django.db import models
from django.conf import settings

# Create your models here.


class ShortUrl:
    def __init__(self):
        self.short_letter = self._short_letter()

    def _short_letter(self) -> str:
        letters = string.ascii_lowercase + string.ascii_uppercase
        rand_letters = random.choices(letters, k=16)
        rand_letters = "".join(rand_letters)
        self.short_letter = rand_letters
        return self.short_letter

    def _does_short_exists(self) -> bool:
        is_true_or_false = PasswordResetUrl.objects.filter(
            url=self.short_letter
        ).exists()

        if is_true_or_false:
            return True
        elif not is_true_or_false:
            return False

    def logic(self) -> str:
        if not self._does_short_exists():
            return self.short_letter
        elif self._does_short_exists():
            self._short_letter()


class PasswordResetUrl(models.Model):
    url = models.CharField(max_length=16, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.id)

    def save(self, *args, **kwargs) -> None:
        self.url = ShortUrl().logic()
        super().save(*args, **kwargs)
