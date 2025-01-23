from ..functions import find_free_port
from typing import Optional


class PortManager:
    _instance: Optional["PortManager"] = None
    _port = find_free_port()

    def get_port(self):
        return self._port

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PortManager, cls).__new__(cls)
        return cls._instance
