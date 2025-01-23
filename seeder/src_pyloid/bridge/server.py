from pyloid import Bridge, PyloidAPI
from ..managers import PortManager

port_manger = PortManager()


class Server(PyloidAPI):
    @Bridge(result=dict)
    def get_server_port(self):
        return {"host": "localhost", "port": port_manger.get_port()}
