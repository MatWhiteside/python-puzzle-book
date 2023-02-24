def sum_even(input_nums: list[int]) -> int:
    return sum(input_num for input_num in input_nums if input_num % 2 == 0)


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
