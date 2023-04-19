def bitwise_add(num_one: int, num_two: int) -> int:
    while num_two != 0:
        carry = num_one & num_two
        num_one = num_one ^ num_two
        num_two = carry << 1

    return num_one


print(bitwise_add(3, 4))
print(bitwise_add(255, 256))
print(bitwise_add(-1, -2))
