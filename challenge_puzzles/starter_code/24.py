from typing import Any


def my_zip(input_list_a: list[Any], input_list_b: list[Any]) -> list[tuple[Any, Any]]:
    # Your implementation here


print(my_zip([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip([], []))
print(my_zip([1, 2, 3], [5, 6, 7, 8]))
print(my_zip([1, 2, 3, 4], [5, 6, 7]))
