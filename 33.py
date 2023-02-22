def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def find_primes(numbers: list[int]) -> list[int]:
    return [n for n in numbers if is_prime(n)]


print(find_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # should print [2, 3, 5, 7]
print(find_primes(list(range(100))))  # should print [2, 3, 5, 7]
