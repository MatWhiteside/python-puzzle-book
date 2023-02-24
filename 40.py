import random


def insertion_sort(input_nums: list[int]) -> list[int]:
    for i in range(1, len(input_nums)):
        key = input_nums[i]
        j = i - 1
        while j >= 0 and key < input_nums[j]:
            input_nums[j + 1] = input_nums[j]
            j -= 1
        input_nums[j + 1] = key
    return input_nums


print(insertion_sort([5, 10, 9, 11, 4]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([random.randint(0, 1000) for _ in range(200)]))
