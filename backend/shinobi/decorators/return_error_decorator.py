# These decorators catch :
#   AttributeError : In case `selectolax` fails to find the dom node
#   IndexError : In case `selectolax` finds empty dom node

from typing import Type, Callable, Any, Union, Tuple
import functools


def return_on_error[T](return_type: T) -> Callable[[Callable], Callable]:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                return func(*args, **kwargs)
            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator
