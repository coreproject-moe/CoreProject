import random

from django.conf import settings
from django.contrib.auth import get_user_model


def get_random_discriminator(username: str) -> int:
    # https://www.reddit.com/r/learnpython/comments/e1hmpm/comment/f8p6htr/
    exclude = set(
        get_user_model()
        .objects.filter(username=username)
        .values_list("discriminator", flat=True)
        .distinct()
    )

    return random.choice(
        [i for i in range(0, int("9" * settings.DISCRIMINATOR_LENGTH)) if i not in exclude]
    )
