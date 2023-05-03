import functools
from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")
# These decorators catch :
#   AttributeError : In case `selectolax` fails to find the dom node
#   IndexError : In case `selectolax` finds empty dom node


def return_on_error(
    return_type: type[T],
) -> Callable[[Callable[..., Any]], Callable[..., T]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                return func(*args, **kwargs)

            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator
