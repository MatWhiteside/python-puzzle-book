import socket
import struct


def ip_range_to_list(ip_range):
    start, end = ip_range.split("-")
    start_ip = struct.unpack("!L", socket.inet_aton(start))[0]
    end_ip = struct.unpack("!L", socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack("!L", i)) for i in range(start_ip, end_ip + 1)]


print(ip_range_to_list("192.255.255.0-192.255.255.255"))
