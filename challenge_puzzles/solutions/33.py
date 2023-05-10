def is_prime(input_num: int) -> bool:
    if input_num < 2:
        return False
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
    return True


def find_primes(input_nums: list[int]) -> list[int]:
    return [input_num for input_num in input_nums if is_prime(input_num)]


print(find_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_primes([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(find_primes([2, 3, 5, 7, 11, 13, 17]))
print(find_primes(list(range(100))))
