from pyloid import Bridge, PyloidAPI
from ..functions import find_free_port


class Server(PyloidAPI):
    @Bridge(result=dict)
    def get_server_port(self):
        return {"host": "localhost", "port": find_free_port()}
