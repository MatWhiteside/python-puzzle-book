from typing import Any


def rotate_list_left(input_list: list[Any], rotate_amount: int) -> list[Any]:
    return input_list[rotate_amount:] + input_list[:rotate_amount]


print(rotate_list_left([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 2))
