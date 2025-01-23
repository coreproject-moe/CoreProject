from pyloid import Bridge, PyloidAPI
from ..managers import PortManager
from ..server import WebSocketServer

port_manger = PortManager()


class Server(PyloidAPI):
    @Bridge(result=dict)
    def get_server_port(self):
        return {"host": "localhost", "port": port_manger.get_port()}

    @Bridge(result=bool | str)
    def start_websocket_server(self):
        try:
            worker = WebSocketServer()
            worker.start()
            print("Started websocket server")
            return True
        except Exception as e:
            return e
