from pyloid import Bridge


class Server:
    @Bridge(result=tuple[str, int])
    def get_server_port():
        return ("localhost", 10000)
