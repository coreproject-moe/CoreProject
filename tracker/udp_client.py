import socket


def send_udp_message(server_ip="127.0.0.1", server_port=1234, message="Test message"):
    """
    Send a simple UDP message to a server and print the response

    Args:
        server_ip (str): Server IP address
        server_port (int): Server port number
        message (str): Message to send
    """
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

    try:
        # Convert message to bytes
        message_bytes = message.encode("utf-8")

        # Send message
        print(f"Sending to {server_ip}:{server_port}: {message}")
        client_socket.sendto(message_bytes, (server_ip, server_port))

        # Set timeout for receiving response (5 seconds)
        client_socket.settimeout(5)

        # Wait for response
        try:
            data, server = client_socket.recvfrom(1024)
            print(f"Response from {server[0]}:{server[1]}: {data.decode('utf-8')}")
        except socket.timeout:
            print("No response received (timeout)")

    finally:
        # Close socket
        client_socket.close()
        print("Socket closed")


# Example usage
if __name__ == "__main__":
    # You can modify these parameters as needed
    send_udp_message(
        server_ip="[::1]",  # localhost
        server_port=1234,  # port to connect to
        message="Hello, UDP server!",  # your test message
    )
