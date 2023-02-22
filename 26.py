from typing import Any


def rotate_list_left(lst: list[Any], positions: int) -> list[Any]:
    return lst[positions:] + lst[:positions]


print(rotate_list_left([1, 2, 3, 4, 5], 2))
print(rotate_list_left([1, 2, 3, 4, 5], 2))
