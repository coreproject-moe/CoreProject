from enum import Enum, auto

__all__ = ["IP"]


class IP(Enum):
    IPV4 = auto()
    IPV6 = auto()
