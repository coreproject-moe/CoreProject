import asyncio
import json

from coreproject_tracker.enums import ACTIONS, EVENT_NAMES
from coreproject_tracker.functions import (
    addrs_to_compact,
    convert_event_id_to_event_enum,
    from_uint16,
    from_uint32,
    from_uint64,
    get_n_random_items,
    hdel,
    hget,
    hset,
    to_uint32,
)
from coreproject_tracker.validators import UdpValidator


class UDPServerProtocol(asyncio.DatagramProtocol):
    def __init__(self) -> None:
        self.transport: asyncio.DatagramTransport | None = None

    def connection_made(self, transport: asyncio.DatagramTransport) -> None:
        self.transport = transport

    async def make_udp_packet(self, params: UdpValidator) -> bytes:
        if params.action == ACTIONS.CONNECT:
            packet: bytes = b"".join(
                [
                    await to_uint32(ACTIONS.CONNECT),
                    await to_uint32(params.transaction_id),
                    params.connection_id,
                ]
            )
        elif params.action == ACTIONS.ANNOUNCE:
            packet = b"".join(
                [
                    await to_uint32(ACTIONS.ANNOUNCE),
                    await to_uint32(params.transaction_id),
                    await to_uint32(params.interval),
                    await to_uint32(params.incomplete),
                    await to_uint32(params.complete),
                    params.peers,
                ]
            )
        else:
            raise ValueError(f"Action not implemented: {params.action}")
        return packet

    async def handle_packet(self, data: bytes, addr: tuple[str, int]) -> None:
        if len(data) < 16:
            self.transport.sendto(b"Too small payload", addr)
            return

        _data = {
            "connection_id": data[0:8],
            "action": await from_uint32(data[8:12]),
            "transaction_id": await from_uint32(data[12:16]),
        }
        data_obj = UdpValidator(**_data)

        if data_obj.action == ACTIONS.ANNOUNCE:
            _data |= {
                "info_hash": data[16:36].hex(),
                "peer_id": data[36:56].hex(),
                "downloaded": await from_uint64(data[56:64]),
                "left": await from_uint64(data[64:72]),
                "uploaded": await from_uint64(data[72:80]),
                "event_id": await from_uint32(data[80:84]),
                "ip": await from_uint32(data[84:88]) or addr[0],
                "key": await from_uint32(data[88:92]),
                "numwant": await from_uint32(data[92:96]),
                "port": await from_uint16(data[96:98]) or addr[1],
            }
            data_obj = UdpValidator(**_data)
            await hset(
                data_obj.info_hash,
                f"{data_obj.ip}:{data_obj.port}",
                json.dumps(
                    {
                        "peer_id": data_obj.peer_id,
                        "info_hash": data_obj.info_hash,
                        "peer_ip": data_obj.ip,
                        "port": data_obj.port,
                        "left": data_obj.left,
                    }
                ),
            )
            redis_data = await hget(data_obj.info_hash)
            peers_list = await get_n_random_items(redis_data.values(), data_obj.numwant)
            peers: list[str] = []
            seeders: int = 0
            leechers: int = 0

            for peer in peers_list:
                peer_data = json.loads(peer)
                if peer_data["left"] == 0:
                    seeders += 1
                else:
                    leechers += 1
                peers.append(f"{peer_data['peer_ip']}:{peer_data['port']}")

            _data |= {
                "peers": await addrs_to_compact(peers),
                "complete": seeders,
                "incomplete": leechers,
            }
            data_obj = UdpValidator(**_data)

        if (event_id := data_obj.event_id) and (
            await convert_event_id_to_event_enum(event_id) == EVENT_NAMES.STOP
        ):
            await hdel(data_obj.info_hash, f"{data_obj.ip}:{data_obj.port}")

        packet = await self.make_udp_packet(data_obj)
        self.transport.sendto(packet, addr)

    def datagram_received(self, data: bytes, addr: tuple[str, int]) -> None:
        asyncio.create_task(self.handle_packet(data, addr))


async def run_udp_server(server_host: str, server_port: int) -> None:
    loop = asyncio.get_running_loop()
    print(f"Running UDP server on `udp://{server_host}:{server_port}`")

    # transport, protocol
    transport, _ = await loop.create_datagram_endpoint(
        lambda: UDPServerProtocol(), local_addr=(server_host, server_port)
    )
    try:
        await asyncio.Future()  # Keep running
    finally:
        transport.close()
