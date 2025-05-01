import logging
import sys
from typing import Any

import anyio
from quart import json

from coreproject_tracker.datastructures import RedisDatastructure, UdpDatastructure
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
    to_uint32,
)


async def make_udp_packet(params: UdpDatastructure) -> bytes:
    """
    Create UDP packets for BitTorrent tracker protocol.

    Args:
        params: Dictionary containing packet parameters including 'action' and other action-specific parameters.

    Returns:
        bytes: The constructed UDP packet

    Raises:
        ValueError: If the action is not implemented
    """

    if params.action == ACTIONS.CONNECT:
        packet = b"".join(
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


async def run_udp_server(server_host: str, server_port: int):
    logging.info(f"Running UDP server on udp://{server_host}:{server_port}")
    opts = {
        "local_host": server_host,
        "local_port": server_port,
    }
    if sys.platform != "win32":
        opts |= {
            "reuse_port": True,
        }

    async with await anyio.create_udp_socket(**opts) as udp:
        async for packet, (host, port) in udp:
            if len(packet) < 16:
                await udp.sendto("Too small payload".encode(), host, port)
                continue

            _data = {
                "connection_id": packet[0:8],
                "action": await from_uint32(packet[8:12]),
                "transaction_id": await from_uint32(packet[12:16]),
            }
            data = UdpDatastructure(**_data)

            if data.action == ACTIONS.ANNOUNCE:
                _data, data = await handle_announce(_data, packet, host=host, port=port)

            if data.event_name == EVENT_NAMES.STOP:
                await hdel(data.info_hash, f"{data.ip}:{data.port}")

            packet = await make_udp_packet(data)
            logging.info(f"Sent UDP packet for {host}:{port}")
            await udp.sendto(packet, host, port)


async def handle_announce(
    _data: dict[str, Any], packet: bytes, host: str, port: int
) -> tuple[dict[str, Any], UdpDatastructure]:
    _data |= {
        "info_hash": packet[16:36],  # 20 bytes
        "peer_id": packet[36:56].hex(),  # 20 bytes
        "downloaded": from_uint64(
            packet[56:64]  # Convert 64-bit unsigned integer
        ),
        "left": from_uint64(
            packet[64:72]  # Convert 64-bit unsigned integer
        ),
        "uploaded": from_uint64(
            packet[72:80]  # Convert 64-bit unsigned integer
        ),
        "event_name": await convert_event_id_to_event_enum(
            await from_uint32(
                packet[80:84]  # Read 4-byte unsigned int (big-endian)
            ),
        ),
        "ip": await from_uint32(packet[84:88]) or host,
        "key": await from_uint32(packet[88:92]),
        "numwant": await from_uint32(packet[92:96]),
        "port": await from_uint16(packet[96:98]) or port,
    }
    data = UdpDatastructure(**_data)
    redis_stroage = RedisDatastructure(
        info_hash=data.info_hash.hex(),
        type="udp",
        peer_id=data.peer_id,
        peer_ip=data.ip,
        port=data.port,
        left=data.left,
    )

    await redis_stroage.save()

    redis_data = await hget(data.info_hash.hex()) or {}
    peers_list = await get_n_random_items(redis_data.values(), data.numwant)

    peers = []
    seeders = 0
    leechers = 0

    for peer in peers_list:
        _peers = []
        _seeders = 0
        _leechers = 0

        try:
            peer_data = json.loads(peer)

            if peer_data["left"] == 0:
                _seeders += 1
            else:
                _leechers += 1

            _peers.append(f"{peer_data['peer_ip']}:{peer_data['port']}")

        except (ValueError, KeyError):
            continue

        # This is here to make undo possible
        peers.extend(_peers)
        seeders += _seeders
        leechers += _leechers

    _data |= {
        "peers": await addrs_to_compact(peers),
        "complete": seeders,
        "incomplete": leechers,
    }
    return _data, UdpDatastructure(**_data)
