from typing import Generic, TypeVar

from attrs import define

T = TypeVar("T")


@define
class MutableBox(Generic[T]):
    """A simple mutable container for any type T."""

    value: T
