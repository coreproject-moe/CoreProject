import random

from django.conf import settings

from ..models import User


def get_random_username_discriminator(username) -> int:
    # https://www.reddit.com/r/learnpython/comments/e1hmpm/comment/f8p6htr/
    exclude = set(
        User.objects.filter(username=username)
        .values_list("username_discriminator", flat=True)
        .distinct()
    )

    return random.choice(
        [
            i
            for i in range(0, int("9" * settings.USERNAME_DISCRIMINATOR_LENGTH))
            if i not in exclude
        ]
    )
