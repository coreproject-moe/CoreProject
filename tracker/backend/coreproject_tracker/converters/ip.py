from coreproject_tracker.functions import convert_ipv4_coded_ipv6_to_ipv4

__all__ = ["convert_ip"]


def convert_ip(value: str) -> str:
    ipv4_address = convert_ipv4_coded_ipv6_to_ipv4(value)
    if ipv4_address is False:
        raise ValueError(f"Invalid IPv4 address: {value}")

    if isinstance(ipv4_address, str):
        return ipv4_address
    else:
        return value
