def get_second_largest_number(input_nums: list[int]) -> int | None:
    if len(input_nums) < 2:
        return None

    max_number = max(input_nums)
    input_nums.remove(max_number)
    second_max = max(input_nums)

    return second_max


print(get_second_largest_number([1, 2, 3, 4, 5]))
print(get_second_largest_number([3, 45, 345, 435, 345, 43, 56, 34, 234, 34]))
print(get_second_largest_number([1]))
