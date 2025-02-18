import anyio


async def run_udp_server():
    port = 5000
    async with await anyio.create_udp_socket(
        local_host="0.0.0.0", local_port=port
    ) as udp:
        print(f"UDP server listening on port {port}")

        async for packet, (host, port) in udp:
            await udp.sendto(b"Hello, " + packet, host, port)
