def add(x: int, y: int) -> int:
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


print(add(3, 4))
print(add(255, 256))
