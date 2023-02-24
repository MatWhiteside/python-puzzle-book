def knapsack(items: list[tuple[int, int]], max_weight: int) -> int:
    # Create a matrix to store the maximum value at each weight
    max_value_matrix = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]

    for item_idx in range(1, len(items) + 1):
        for weight in range(1, max_weight + 1):
            if items[item_idx - 1][0] > weight:
                max_value_matrix[item_idx][weight] = max_value_matrix[item_idx - 1][weight]
            else:
                max_value_matrix[item_idx][weight] = max(max_value_matrix[item_idx - 1][weight], max_value_matrix[item_idx - 1][weight - items[item_idx - 1][0]] + items[item_idx - 1][1])

    return max_value_matrix[len(items)][max_weight]


# [(weight, value), ...]
items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 5
print(knapsack(items, max_weight))
