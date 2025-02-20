import struct


async def to_uint32(value: int) -> bytes:
    """Convert an integer to a 4-byte unsigned integer in network byte order."""
    return struct.pack(">I", value)


async def from_uint16(data: bytes) -> int:
    """Convert an 2-byte `unsigned short` buffer into an integer."""
    return struct.unpack(">H", data)[0]


async def from_uint32(data: bytes) -> int:
    """Convert an 2-byte `unsigned int` buffer into an integer."""
    return struct.unpack(">I", data)[0]


def from_uint64(buf: bytes) -> int:
    """Convert an 8-byte `unsigned long long` buffer into an integer."""
    return struct.unpack(">Q", buf)[0]
