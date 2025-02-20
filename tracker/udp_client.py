import socket


def udp_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    # Server address (replace with the actual server's IP and port)
    server_address = ("localhost", 5000)

    try:
        # Message to send
        message = "Hello, UDP Server!"

        # Send data
        print(f"Sending: {message}")
        client_socket.sendto(message.encode(), server_address)

        # Receive response
        data, server = client_socket.recvfrom(4096)
        print(f"Received: {data.decode()}")

    finally:
        # Close the socket
        client_socket.close()


if __name__ == "__main__":
    udp_client()
