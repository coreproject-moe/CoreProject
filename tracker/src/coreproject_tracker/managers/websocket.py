import asyncio
import time


class WebsocketConnectionManager:
    _instance = None

    def __new__(cls, ttl: int = 60):
        if cls._instance is None:
            cls._instance = super(WebsocketConnectionManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, ttl: int = 60):
        self.connections = {}
        self.ttl = ttl

    async def add_connection(self, identifier: str, ws):
        self.connections[identifier] = (ws, time.time())
        await self._cleanup_stale_connections()

    async def remove_connection(self, identifier: str):
        self.connections.pop(identifier, None)

    async def get_connection(self, identifier: str):
        if identifier in self.connections:
            connection, _ = self.connections[identifier]
            if connection is not None:
                self.connections[identifier] = (connection, time.time())
                return connection
            else:
                await self.remove_connection(identifier)
        await self._cleanup_stale_connections()
        return None

    async def _cleanup(self):
        while True:
            await asyncio.sleep(self.ttl)
            await self._cleanup_stale_connections()

    async def _cleanup_stale_connections(self):
        current_time = time.time()
        to_remove = [
            identifier
            for identifier, (connection, last_active) in self.connections.items()
            if connection is None or (current_time - last_active) > self.ttl
        ]
        for identifier in to_remove:
            del self.connections[identifier]
