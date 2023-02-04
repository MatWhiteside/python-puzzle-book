def sum_even(numbers):
    return sum([x for x in numbers if x % 2 == 0])


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
