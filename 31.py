from typing import Any
from collections.abc import Iterator


def param_count(*args: Any) -> int:
    return len(args)


print(param_count(1, 2, 3, 4, 5))


# Bonus Solution 1
def my_zip_one(*input_lists: list[Any]) -> list[tuple[Any, ...]]:
    input_lists_list = list(input_lists)
    if len(input_lists_list) == 0:
        return []

    shortest_list_length = len(input_lists_list[0])
    for to_zip_list in input_lists_list[1:]:
        if len(to_zip_list) < shortest_list_length:
            shortest_list_length = len(to_zip_list)

    zipped_result = [tuple() for _ in range(shortest_list_length)]
    for i in range(shortest_list_length):
        for to_zip_list in input_lists_list:
            zipped_result[i] += (to_zip_list[i],)

    return zipped_result


print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])))
print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(my_zip_one([], [])))
print(list(my_zip_one([1, 2, 3], [5, 6, 7, 8])))
print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7])))


# BONUS SOLUTION 2
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
