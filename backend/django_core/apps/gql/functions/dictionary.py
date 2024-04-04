from typing import Any
from strawberry import UNSET


def clean_dictionary[T: dict[str, Any]](dictionary: T, ignored_keys: list[str] = []) -> T:
    model_data = {
        key: value
        for key, value in dictionary.items()
        if key
        not in ignored_keys
        and value != UNSET
    }

    return model_data
