def solve_knapsack_problem(items: list[tuple[int, int]], knapsack_capacity: int) -> int:
    # Create a matrix to store the maximum value at each weight
    max_value_matrix = [
        [0 for _ in range(knapsack_capacity + 1)] for _ in range(len(items) + 1)
    ]

    for item_idx in range(1, len(items) + 1):
        for weight in range(1, knapsack_capacity + 1):

            if items[item_idx - 1][0] > weight:
                max_value_matrix[item_idx][weight] = max_value_matrix[item_idx - 1][
                    weight
                ]
            else:
                max_value_matrix[item_idx][weight] = max(
                    max_value_matrix[item_idx - 1][weight],
                    max_value_matrix[item_idx - 1][weight - items[item_idx - 1][0]]
                    + items[item_idx - 1][1],
                )

    return max_value_matrix[len(items)][knapsack_capacity]


# [(weight, value), ...]
items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 5
print(solve_knapsack_problem(items, max_weight))

items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 0
print(solve_knapsack_problem(items, max_weight))

items = []
max_weight = 5
print(solve_knapsack_problem(items, max_weight))
