async def bytes_to_bin_str(_bytes: bytes) -> str:
    return _bytes.decode("latin-1")


async def hex_str_to_bin_str(hex_str: str) -> str:
    return bytes.fromhex(hex_str).decode("latin1")
