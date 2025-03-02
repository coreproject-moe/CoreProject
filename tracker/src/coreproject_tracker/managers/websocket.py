from quart import Websocket


class WebsocketConnectionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebsocketConnectionManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.connections = {}

    async def add_connection(self, identifier: str, ws: Websocket) -> None:
        self.connections[identifier] = ws

    async def remove_connection(self, identifier: str) -> None:
        self.connections.pop(identifier, None)

    async def get_connection(self, identifier: str) -> Websocket:
        return self.connections[identifier]
