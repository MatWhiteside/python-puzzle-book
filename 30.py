import random


def find_triplets(numbers: list[int]) -> list[tuple[int, int, int]]:
    triplets = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    triplets.append((i, j, k))
    return triplets


print(find_triplets([1, 2, 3, 4, 5]))
print(find_triplets([1, 2, 3, 4, 5, -9]))

random_ints = [random.randint(-100, 100) for _ in range(50)]
random_triplets = find_triplets(random_ints)
for (a, b, c) in random_triplets:
    print(
        f"{random_ints[a]} + {random_ints[b]} + {random_ints[c]} = {random_ints[a] + random_ints[b] + random_ints[c]}"
    )
