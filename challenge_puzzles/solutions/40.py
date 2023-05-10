import random


def insertion_sort(input_nums: list[int]) -> list[int]:
    for key_index in range(1, len(input_nums)):
        value_to_insert = input_nums[key_index]
        previous_index = key_index - 1

        while previous_index >= 0 and value_to_insert < input_nums[previous_index]:
            input_nums[previous_index + 1] = input_nums[previous_index]
            previous_index -= 1

        input_nums[previous_index + 1] = value_to_insert

    return input_nums


print(insertion_sort([5, 10, 9, 11, 4]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([-1, -2, -3, -4, -5]))
print(insertion_sort([random.randint(0, 1000) for _ in range(200)]))
