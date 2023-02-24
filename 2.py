def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    if num_one + num_two < 50:
        return None
    return num_one + num_two


print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))
