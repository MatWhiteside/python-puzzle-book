import socket
import struct


def ip_range_to_list(input_ip_range: str) -> list[str]:
    # Your implementation here


print(ip_range_to_list("192.168.1.1-192.168.1.5"))
print(ip_range_to_list("1.1.1.0-1.1.1.1"))
print(ip_range_to_list("192.255.255.0-192.255.255.0"))
