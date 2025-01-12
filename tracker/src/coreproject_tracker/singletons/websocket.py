import time
import weakref
from threading import Lock
from typing import Optional

from autobahn.twisted.websocket import WebSocketServerProtocol

from coreproject_tracker.constants import (
    CONNECTION_TTL,
)


class WebsocketConnectionManager:
    _instance: Optional["WebsocketConnectionManager"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebsocketConnectionManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Store connections and their last activity time
        self._connections: dict[str, (weakref.ref, float)] = {}
        self._inactive_timeout = CONNECTION_TTL
        self._lock = Lock()

    def add_connection(
        self, identifier: str, connection: WebSocketServerProtocol
    ) -> None:
        """
        Store a websocket connection with an identifier and current timestamp
        Uses weakref to avoid memory leaks
        """
        with self._lock:
            self._connections[identifier] = (weakref.ref(connection), time.time())
            self._cleanup_stale_connections()

    def remove_connection(self, identifier: str) -> None:
        """Remove a connection from storage"""
        with self._lock:
            if identifier in self._connections:
                del self._connections[identifier]

    def get_connection(self, identifier: str) -> WebSocketServerProtocol | None:
        """
        Retrieve a connection by its identifier
        Updates the last activity timestamp when connection is accessed
        """
        with self._lock:
            if identifier in self._connections:
                connection_ref, _ = self._connections[identifier]
                connection = connection_ref()

                if connection is not None and connection.connected:
                    # Update last activity time
                    self._connections[identifier] = (connection_ref, time.time())
                    return connection
                else:
                    # Clean up dead reference
                    self.remove_connection(identifier)

            self._cleanup_stale_connections()
            return None

    def _cleanup_stale_connections(self) -> None:
        """Remove connections that haven't been active for longer than the timeout"""
        current_time = time.time()
        dead_connections = []

        for identifier, (connection_ref, last_active) in self._connections.items():
            connection = connection_ref()

            # Remove if connection is dead or inactive
            if (
                connection is None
                or not connection.connected
                or (current_time - last_active) > self._inactive_timeout
            ):
                dead_connections.append(identifier)

        # Clean up identified dead/stale connections
        for identifier in dead_connections:
            self.remove_connection(identifier)
