import random


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


print(insertion_sort([]))
print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([random.randint(0, 1000) for _ in range(200)]))
