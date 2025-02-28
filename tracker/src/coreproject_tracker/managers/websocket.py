import asyncio

from quart import Websocket


class WebsocketConnectionManager:
    _instance = None
    _connections = {}
    _ttl = 60  # Time to live for stale connections in seconds

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(WebsocketConnectionManager, cls).__new__(cls)
        return cls._instance

    def add_connection(self, peer_id, ws):
        self._connections[peer_id] = {
            "websocket": ws,
            "last_active": asyncio.get_event_loop().time(),
        }

    def get_connection(self, peer_id) -> Websocket:
        return self._connections.get(peer_id, {}).get("websocket")

    def remove_connection(self, peer_id):
        self._connections.pop(peer_id, None)

    async def _cleanup_stale_connections(self):
        while True:
            await asyncio.sleep(self._ttl)
            current_time = asyncio.get_running_loop().time()
            for peer_id in list(self._connections.keys()):
                if current_time - self._connections[peer_id]["last_active"] > self._ttl:
                    self.remove_connection(peer_id)

    async def start_cleanup_task(self):
        """Start cleanup task only when an event loop is running."""
        await asyncio.sleep(1)  # Small delay to ensure the event loop is running
        asyncio.create_task(self._cleanup_stale_connections())

    async def close_all(self):
        for peer_id, conn_data in self._connections.items():
            ws = conn_data["websocket"]
            await ws.close()
        self._connections.clear()
