from pyloid import Bridge, PyloidAPI


class Server(PyloidAPI):
    @Bridge(result=tuple[str, int])
    def get_server_port(self):
        return ("localhost", 10000)
