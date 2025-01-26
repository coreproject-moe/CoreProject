from PySide6.QtCore import QThread
from websockets.sync.server import serve
from typing import Optional


class WebSocketServer(QThread):
    _instance: Optional["WebSocketServer"] = None

    def __init__(self, port: int):
        self.port = port
        super().__init__()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WebSocketServer, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @staticmethod
    def echo(websocket):
        for message in websocket:
            websocket.send(message)

    def run(self):
        with serve(self.echo, "localhost", self.port) as server:
            server.serve_forever()
