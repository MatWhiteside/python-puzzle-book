def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(36, 8))
print(gcd(5, 25))
