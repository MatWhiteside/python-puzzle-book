import random


def insertion_sort(input_nums: list[int]) -> list[int]:
    # Your implementation here


print(insertion_sort([5, 10, 9, 11, 4]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([-1, -2, -3, -4, -5]))
print(insertion_sort([random.randint(0, 1000) for _ in range(200)]))
