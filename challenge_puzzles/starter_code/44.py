def quicksort(input_list: list[int], low: int, high: int) -> list[int]:
    # Your implementation here


unsorted_list = [5, 7, 8, 1, 2, 4, 99, 77, 56, 43, 12, 98]
print(quicksort(unsorted_list, 0, len(unsorted_list) - 1))

unsorted_list = [10, 5, -10, -5, 0]
print(quicksort(unsorted_list, 0, len(unsorted_list) - 1))

print(quicksort([], 0, 0))
