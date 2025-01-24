import socket


def find_free_port(start_port=1024, end_port=65535):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.bind(("localhost", port))
            sock.close()
            return port  # Port is available
        except socket.error:
            continue  # Port is in use, try the next one
    return None  # No free port found
