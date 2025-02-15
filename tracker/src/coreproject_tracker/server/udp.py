import trio
import socket


async def run_udp_server():
    port = 5000  # Same port as HTTP/WebSocket
    sock = trio.socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    await sock.bind(("0.0.0.0", port))
    print(f"UDP server listening on port {port}")

    while True:
        data, addr = await sock.recvfrom(1024)
        print(f"Received UDP message from {addr}: {data.decode()}")
        await sock.sendto(b"UDP Echo: " + data, addr)
