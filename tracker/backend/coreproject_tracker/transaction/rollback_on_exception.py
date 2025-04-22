import copy
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    from coreproject_tracker.datastructures import MutableBox

__all__ = ["rollback_on_exception"]


@contextmanager
def rollback_on_exception(*boxes: MutableBox[Any]) -> Iterator[None]:
    """
    Context manager that restores Box values if an exception is raised inside the block.
    """
    # Take a deep copy snapshot of each box's value
    old_values = [copy.deepcopy(b.value) for b in boxes]
    try:
        yield
    except Exception:
        # Roll back each box to its original value
        for b, old in zip(boxes, old_values):
            b.value = old
        raise
