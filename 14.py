def reverse_first_five(lst: list[int]) -> list[int]:
    return lst[:5][::-1] + lst[5:]


print(reverse_first_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
