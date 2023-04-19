from typing import Any, Callable, Optional


# These decorators catch :
#   AttributeError : In case `selectolax` fails to find the dom node
#   IndexError : In case `selectolax` finds empty dom node


def return_empty_string_on_catched_error(
    func: Callable[..., Any]
) -> Callable[..., Optional[Any]]:
    def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            return func(*args, **kwargs)

        except (AttributeError, IndexError):
            return ""

    return wrapper


def return_empty_list_on_catched_error(
    func: Callable[..., Any]
) -> Callable[..., Optional[Any]]:
    def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
        try:
            return func(*args, **kwargs)

        except (AttributeError, IndexError):
            return []

    return wrapper
