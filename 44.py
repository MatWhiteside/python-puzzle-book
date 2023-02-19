def binary_search(sorted_list, value_to_find):
    low = 0
    high = len(sorted_list) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if value_to_find > sorted_list[mid]:
            low = mid + 1

        # If x is smaller, ignore right half
        elif value_to_find < sorted_list[mid]:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


sorted_list = [2, 3, 4, 10, 40]
value_to_find = 0
print(binary_search(sorted_list, value_to_find))

sorted_list = [2, 3, 4, 10, 40]
value_to_find = 10
print(binary_search(sorted_list, value_to_find))
