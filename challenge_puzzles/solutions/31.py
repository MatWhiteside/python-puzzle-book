from typing import Any
from collections.abc import Iterator


def param_count(*args: Any) -> int:
    return len(args)


print(param_count(1, 2, 3, 4, 5))
print(param_count("hello"))
print(param_count())


# Bonus Solution 1
def my_zip_one(*input_lists: list[Any]) -> list[tuple[Any, ...]]:
    if len(input_lists) == 0:
        return []

    shortest_length = min(len(input_list) for input_list in input_lists)
    zipped_result = [tuple() for _ in range(shortest_length)]

    for i in range(shortest_length):
        for input_list in input_lists:
            zipped_result[i] += (input_list[i],)

    return zipped_result


print(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))
print(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip_one([], []))
print(my_zip_one([1, 2, 3], [5, 6, 7, 8]))
print(my_zip_one([1, 2, 3, 4], [5, 6, 7]))


# Bonus Solution (alternative)
def my_zip_two(*input_lists: list[Any]) -> Iterator[tuple[Any, ...]]:
    sentinel = object()
    input_lists_iterators = [iter(input_list) for input_list in input_lists]
    while input_lists_iterators:
        zipped_result = []
        for input_list_iterator in input_lists_iterators:
            elem = next(input_list_iterator, sentinel)
            if elem is sentinel:
                return
            zipped_result.append(elem)
        yield tuple(zipped_result)


print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(my_zip_two([], [])))
print(list(my_zip_two([1, 2, 3], [5, 6, 7, 8])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7])))
