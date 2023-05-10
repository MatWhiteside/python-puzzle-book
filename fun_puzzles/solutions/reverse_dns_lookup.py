import socket


def reverse_dns_lookup(ip_address: str) -> str:
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return None


print(reverse_dns_lookup("8.8.8.8"))
print(reverse_dns_lookup("208.67.222.222"))
print(reverse_dns_lookup("1.1.1.1"))
