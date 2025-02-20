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


async def make_udp_packet(params: UdpValidator) -> bytes:
    """
    Create UDP packets for BitTorrent tracker protocol.

    Args:
        params: Dictionary containing packet parameters including 'action' and other
            action-specific parameters.

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

    # elif params.action == ACTIONS.SCRAPE:
    #     scrape_response = [
    #         to_uint32(ACTIONS.SCRAPE),
    #         to_uint32(params.transaction_id),
    #     ]

    #     for info_hash, file in params["files"].items():
    #         scrape_response.extend(
    #             [
    #                 to_uint32(file.complete),
    #                 to_uint32(
    #                     file.downloaded
    #                 ),  # Note: this only provides a lower-bound
    #                 to_uint32(file.incomplete),
    #             ]
    #         )

    #     packet = b"".join(scrape_response)

    # elif params.action == ACTIONS.ERROR:
    #     packet = b"".join(
    #         [
    #             to_uint32(ACTIONS.ERROR),
    #             to_uint32(params.transaction_id),
    #             str(params.get("failure_reason", "")).encode(),
    #         ]
    #     )

    else:
        raise ValueError(f"Action not implemented: {params.action}")

    return packet


async def run_udp_server(server_host: str, server_port: int):
    print(f"Running UDP server on `udp://{server_host}:{server_port}`")
    async with await anyio.create_udp_socket(
        local_host=server_host,
        local_port=server_port,
    ) as udp:
        async for packet, (host, port) in udp:
            if len(packet) < 16:
                # log.error(
                #     f"received packet length is {packet} is shorter than 16 bytes"
                # )
                await udp.sendto(b"", host, port)

            _data = {
                "connection_id": packet[0:8],
                "action": await from_uint32(packet[8:12]),
                "transaction_id": await from_uint32(packet[12:16]),
            }
            data = UdpValidator(**_data)

            if data.action == ACTIONS.ANNOUNCE:
                _data = (
                    _data
                    | {
                        "info_hash": packet[16:36].hex(),  # 20 bytes
                        "peer_id": packet[36:56].hex(),  # 20 bytes
                        "downloaded": await from_uint64(
                            packet[56:64]  # Convert 64-bit unsigned integer
                        ),
                        "left": await from_uint64(
                            packet[64:72]  # Convert 64-bit unsigned integer
                        ),
                        "uploaded": await from_uint64(
                            packet[72:80]  # Convert 64-bit unsigned integer
                        ),
                        "event_id": await from_uint32(
                            packet[80:84]  # Read 4-byte unsigned int (big-endian)
                        ),
                        "ip": await from_uint32(packet[84:88]) or host,
                        "key": await from_uint32(packet[88:92]),
                        "numwant": await from_uint32(packet[92:96]),
                        "port": await from_uint16(packet[96:98]) or port,
                    }
                )
                data = UdpValidator(**_data)
                await hset(
                    data.info_hash,
                    f"{data.ip}:{data.port}",
                    json.dumps(
                        {
                            "peer_id": data.peer_id,
                            "info_hash": data.info_hash,
                            "peer_ip": data.ip,
                            "port": data.port,
                            "left": data.left,
                        }
                    ),
                )
                redis_data = await hget(data.info_hash)
                peers_list = await get_n_random_items(redis_data.values(), data.numwant)

                peers = []
                seeders = 0
                leechers = 0

                for peer in peers_list:
                    peer_data = json.loads(peer)

                    if peer_data["left"] == 0:
                        seeders += 1
                    else:
                        leechers += 1

                    peers.append(f"{peer_data['peer_ip']}:{peer_data['port']}")

                _data = _data | {
                    "peers": await addrs_to_compact(peers),
                    "complete": seeders,
                    "incomplete": leechers,
                }
                data = UdpValidator(**_data)

            if (event_id := data.event_id) and (
                await convert_event_id_to_event_enum(event_id) == EVENT_NAMES.STOP
            ):
                await hdel(data.info_hash, f"{data.ip}:{data.port}")

            packet = await make_udp_packet(data)
            print(data.ip)
            await udp.sendto(packet, host, port)
            print(f"Sent data to {host}:{port} with {packet}")
