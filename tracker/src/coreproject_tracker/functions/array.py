import random
from typing import TypeVar

T = TypeVar("T")


async def get_n_random_items(array: T, n: int) -> T:
    if not isinstance(array, list):
        array = list(array)

    try:
        ret = random.sample(array, n)
    except ValueError:
        ret = array
    finally:
        return ret
