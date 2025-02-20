from coreproject_tracker.functions import convert_ipv4_coded_ipv6_to_ipv4

__all__ = ["convert_ip"]


def convert_ip(value: str) -> str:
    if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(value):
        return ipv4_address
    else:
        return value
