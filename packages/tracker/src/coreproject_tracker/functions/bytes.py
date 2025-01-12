import struct

TWO_PWR_32 = 2**32


def to_uint32(value: int) -> bytes:
    """Convert an integer to a 4-byte unsigned integer in network byte order."""
    return struct.pack(">I", value)


def from_uint64(buf: bytes) -> int:
    """
    Convert an 8-byte buffer into an unsigned 64-bit integer.
    """
    # Ensure the buffer is 8 bytes long
    if len(buf) != 8:
        raise ValueError("Buffer must be exactly 8 bytes")

    # Unpack the high and low 32-bit parts (big-endian)
    high, low = struct.unpack(">II", buf)

    # Calculate the 64-bit integer
    low_unsigned = low if low >= 0 else TWO_PWR_32 + low
    return high * TWO_PWR_32 + low_unsigned


def from_uint32(data: bytes) -> int:
    return struct.unpack(">I", data)[0]


def from_uint16(data: bytes) -> int:
    return struct.unpack(">H", data)[0]
