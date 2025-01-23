from PySide6.QtCore import QThread
from websockets.sync.server import serve
from ..managers import PortManager
from typing import Optional

port_manager = PortManager()


class WebSocketServer(QThread):
    _instance: Optional["WebSocketServer"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WebSocketServer, cls).__new__(cls)
        return cls._instance

    def echo(websocket):
        for message in websocket:
            websocket.send(message)

    def run(self):
        port = port_manager.get_port()

        with serve(self.echo, "localhost", port) as server:
            server.serve_forever()
