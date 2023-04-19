import random


def find_zero_sum_triplets(input_nums: list[int]) -> list[tuple[int, int, int]]:
    zero_sum_triplets = []

    for i in range(len(input_nums)):
        for j in range(i + 1, len(input_nums)):
            for k in range(j + 1, len(input_nums)):
                if input_nums[i] + input_nums[j] + input_nums[k] == 0:
                    zero_sum_triplets.append((i, j, k))

    return zero_sum_triplets


print(find_zero_sum_triplets([1, 2, 3, 4, 5]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9]))
print(find_zero_sum_triplets([1, 2, 3, 4, 5, -9, -9]))

random_ints = [random.randint(-100, 100) for _ in range(50)]
random_triplets = find_zero_sum_triplets(random_ints)
for a, b, c in random_triplets:
    print(
        f"{random_ints[a]} + {random_ints[b]} + {random_ints[c]} = {random_ints[a] + random_ints[b] + random_ints[c]}"
    )
