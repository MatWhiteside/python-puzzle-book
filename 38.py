def find_pairs(A: list[int], N: int) -> list[tuple[int, int]]:
    pairs = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == N:
                pairs.append((A[i], A[j]))
    return pairs


print(find_pairs([1, 9, 2, 8, 3, 7, 4, 6, 5, 5], 10))
print(find_pairs([11, 12, 13, 14, 15], 10))


# Bonus solution
def find_pairs_bonus(A: list[int], N: int) -> list[tuple[int, int]]:
    pairs = []
    seen = set()
    for x in A:
        if N - x in seen:
            pairs.append((x, N - x))
        else:
            seen.add(x)
    return pairs


print(find_pairs_bonus([1, 9, 2, 8, 3, 7, 4, 6, 5, 5], 10))
print(find_pairs_bonus([11, 12, 13, 14, 15], 10))
