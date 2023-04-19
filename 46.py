import socket
import struct


def ip_range_to_list(input_ip_range: str) -> list[str]:
    start, end = input_ip_range.split("-")
    start_ip = struct.unpack("!L", socket.inet_aton(start))[0]
    end_ip = struct.unpack("!L", socket.inet_aton(end))[0]
    return [
        socket.inet_ntoa(struct.pack("!L", ip_address))
        for ip_address in range(start_ip, end_ip + 1)
    ]


print(ip_range_to_list("192.168.1.1-192.168.1.5"))
print(ip_range_to_list("1.1.1.0-1.1.1.1"))
print(ip_range_to_list("192.255.255.0-192.255.255.0"))
