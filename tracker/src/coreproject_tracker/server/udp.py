import anyio
import socket
from coreproject_tracker.validators import UdpValidator
from coreproject_tracker.functions import (
    from_uint16,
    from_uint32,
    from_uint64,
    to_uint32,
    hset,
    hget,
    hdel,
    get_n_random_items,
    convert_event_id_to_event_enum,
    addrs_to_compact,
)
import json
from coreproject_tracker.enums import ACTIONS, EVENT_NAMES


async def run_udp_server(server_host: str, server_port: int):
    async with await anyio.create_udp_socket(
        local_host="127.0.0.1", local_port=5000
    ) as udp:
        print("UDP server listening on 127.0.0.1:9999")
        while True:
            data, addr = await udp.receive()
            print(f"Received {data} from {addr}")
            await udp.sendto(b"ACK: " + data, addr)  # Echo response
