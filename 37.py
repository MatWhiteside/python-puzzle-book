def gcd(num_one: int, num_two: int) -> int:
    if num_two == 0:
        return num_one
    return gcd(num_two, num_one % num_two)


print(gcd(36, 8))
print(gcd(5, 26))
