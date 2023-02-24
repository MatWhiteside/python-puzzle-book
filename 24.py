from typing import Any


def my_zip(input_list_a: list[Any], input_list_b: list[Any]) -> list[tuple[Any, Any]]:
    zipped_result = []
    for i in range(min(len(input_list_a), len(input_list_b))):
        zipped_result.append((input_list_a[i], input_list_b[i]))
    return zipped_result


print(my_zip([1, 2, 3, 4], [5, 6, 7, 8]))
print(my_zip([], []))
print(my_zip([1, 2, 3], [5, 6, 7, 8]))
print(my_zip([1, 2, 3, 4], [5, 6, 7]))
