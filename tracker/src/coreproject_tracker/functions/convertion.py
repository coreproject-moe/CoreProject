async def hex_str_to_bin_str(hex_str: str) -> str:
    return bytes.fromhex(hex_str).decode("latin1")
