import random

__all__ = ["get_n_random_items"]


async def get_n_random_items[T](array: T, n: int) -> T:
    """Given a set of array elements, returns n random elements from array"""

    # If we pass only one element to the array
    if not isinstance(array, list):
        array = list(array)

    try:
        ret = random.sample(array, n)
    except ValueError:
        ret = array
    finally:
        return ret
