def reverse_first_five_positions(input_nums: list[int]) -> list[int]:
    return input_nums[:5][::-1] + input_nums[5:]


print(reverse_first_five_positions([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(reverse_first_five_positions([100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
print(reverse_first_five_positions([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
