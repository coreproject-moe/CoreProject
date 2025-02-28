import time
from threading import Lock
from typing import Optional

from quart import Websocket

from coreproject_tracker.constants import CONNECTION_TTL


class WebsocketConnectionManager:
    _instance: Optional["WebsocketConnectionManager"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebsocketConnectionManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the connection manager with a storage dictionary and a lock."""
        self._connections: dict[
            str, (Websocket, float)
        ] = {}  # Store Websocket directly
        self._inactive_timeout = CONNECTION_TTL
        self._lock = Lock()

    def add_connection(self, identifier: str, connection: Websocket) -> None:
        """
        Store a websocket connection with an identifier and current timestamp.
        """
        with self._lock:
            self._connections[identifier] = (connection, time.time())
            self._cleanup_stale_connections()

    def remove_connection(self, identifier: str) -> None:
        """Remove a connection from storage."""
        with self._lock:
            self._connections.pop(identifier, None)

    def get_connection(self, identifier: str) -> Optional[Websocket]:
        """
        Retrieve a connection by its identifier.
        Updates the last activity timestamp when connection is accessed.
        """
        with self._lock:
            if identifier in self._connections:
                connection, _ = self._connections[identifier]

                if connection is not None and connection.connected:
                    # Update last activity time
                    self._connections[identifier] = (connection, time.time())
                    return connection
                else:
                    # Clean up dead reference
                    self.remove_connection(identifier)

            self._cleanup_stale_connections()
            return None

    def _cleanup_stale_connections(self) -> None:
        """Remove connections that haven't been active for longer than the timeout."""
        current_time = time.time()
        dead_connections = []

        with self._lock:
            for identifier, (connection, last_active) in self._connections.items():
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
