def second_largest(numbers):
    if len(numbers) < 2:
        return None

    max_num = max(numbers)
    numbers.remove(max_num)
    second_max = max(numbers)

    return second_max


print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([3, 45, 345, 435, 345, 43, 56, 34, 234, 34]))
print(second_largest([1]))
