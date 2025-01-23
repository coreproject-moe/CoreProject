from pyloid import Bridge, PyloidAPI
from ..server import WebSocketServer
from ..functions.port import find_free_port


class Server(PyloidAPI):
    def __init__(self):
        super().__init__()

        self.__port = find_free_port()

    @Bridge(result=dict)
    def get_server_port(self):
        return {"host": "localhost", "port": self.__port}

    @Bridge(result=str)
    def start_websocket_server(self):
        worker = WebSocketServer(self.__port)

        try:
            worker.start()
            print("Started websocket server")
            return "true"
        except Exception as e:
            return e
