import anyio
import socket


async def udp_server():
    print("starting udp server")
    async with await anyio.create_udp_socket(
        local_host="[::1]", local_port=1234, family=socket.AF_INET6
    ) as udp:
        async for packet, (host, port) in udp:
            print("received: ", packet)
            message = b"Hello, " + packet
            print("will send:", message)
            await udp.sendto(message, host, port)


async def main():
    async with anyio.create_task_group() as tg:
        tg.start_soon(udp_server)


anyio.run(main)
