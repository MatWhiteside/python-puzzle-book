from typing import Any
from collections.abc import Iterator


def param_count(*args: Any) -> int:
    # Your implementation here


print(param_count(1, 2, 3, 4, 5))
print(param_count("hello"))
print(param_count())


# Bonus Solution 1
def my_zip_one(*input_lists: list[Any]) -> list[tuple[Any, ...]]:
    # Your implementation here


print(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
print(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip_one([], []))
print(my_zip_one([1, 2, 3], [5, 6, 7, 8]))
print(my_zip_one([1, 2, 3, 4], [5, 6, 7]))


# Bonus Solution (alternative)
def my_zip_two(*input_lists: list[Any]) -> Iterator[tuple[Any, ...]]:
    # Your implementation here


print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(my_zip_two([], [])))
print(list(my_zip_two([1, 2, 3], [5, 6, 7, 8])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7])))
