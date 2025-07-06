import socket

# Define server address and port
SERVER_ADDRESS = "127.0.0.1"  # Change to the server's IP if needed
SERVER_PORT = 5000  # Change to the appropriate port

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == "exit":
            break

        # Send message to server
        client_socket.sendto(message.encode(), (SERVER_ADDRESS, SERVER_PORT))

        # Receive response from server
        data, server = client_socket.recvfrom(1024)
        print(f"Received from server: {data.decode()}")

finally:
    client_socket.close()
    print("Connection closed.")
