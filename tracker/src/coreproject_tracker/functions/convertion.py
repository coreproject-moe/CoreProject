async def bin_str_to_hex_str(binary_string: str) -> str:
    # Ensure the input is treated as bytes
    binary_bytes = binary_string.encode(
        "latin1"
    )  # Use 'latin1' encoding to preserve binary data
    return binary_bytes.hex()


async def hex_str_to_bin_str(hex_str: str) -> str:
    return bytes.fromhex(hex_str).decode("latin1")
