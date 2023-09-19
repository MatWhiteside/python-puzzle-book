def binary_search(sorted_list: list[int], value_to_find: int) -> int:
    low = 0
    high = len(sorted_list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If value_to_find is greater, ignore left half
        if value_to_find > sorted_list[mid]:
            low = mid + 1

        # If value_to_find is smaller, ignore right half
        elif value_to_find < sorted_list[mid]:
            high = mid - 1

        # value_to_find is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


searchable_list = [2, 3, 4, 10, 40]

print(binary_search(searchable_list, 10))
print(binary_search(searchable_list, 0))
print(binary_search([], 0))
