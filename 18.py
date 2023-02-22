def num_digits(n: int) -> int:
    if n == 0:
        return 0
    return 1 + num_digits(n // 10)


print(num_digits(1234))
print(num_digits(0))
print(num_digits(123456789))
