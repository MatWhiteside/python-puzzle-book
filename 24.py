from typing import Any


def my_zip(list1: list[Any], list2: list[Any]) -> list[tuple[Any, Any]]:
    zipped = []
    for i in range(min(len(list1), len(list2))):
        zipped.append((list1[i], list2[i]))
    return zipped


print(my_zip([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip([], []))
print(my_zip([1, 2, 3], [5, 6, 7, 8]))
print(my_zip([1, 2, 3, 4], [5, 6, 7]))
