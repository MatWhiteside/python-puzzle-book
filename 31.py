from typing import Any
from collections.abc import Iterator


def param_count(*args: Any) -> int:
    return len(args)


print(param_count(1, 2, 3, 4, 5))


# Bonus Solution 1
def my_zip_one(*iterables: Any) -> list[tuple[Any, ...]]:
    lists = list(iterables)
    if len(lists) == 0:
        return []

    shortest_list = len(lists[0])
    for to_zip_list in lists[1:]:
        if len(to_zip_list) < shortest_list:
            shortest_list = len(to_zip_list)

    result = [tuple() for _ in range(shortest_list)]
    for i in range(shortest_list):
        for to_zip_list in lists:
            result[i] = result[i] + (to_zip_list[i],)

    return result


print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])))
print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(my_zip_one([], [])))
print(list(my_zip_one([1, 2, 3], [5, 6, 7, 8])))
print(list(my_zip_one([1, 2, 3, 4], [5, 6, 7])))


# BONUS SOLUTION 2
def my_zip_two(*iterables: list[Any]) -> Iterator[tuple[Any, ...]]:
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)


print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7, 8])))
print(list(my_zip_two([], [])))
print(list(my_zip_two([1, 2, 3], [5, 6, 7, 8])))
print(list(my_zip_two([1, 2, 3, 4], [5, 6, 7])))
