def solve_knapsack_problem(
    items: list[tuple[int, int]], knapsack_capacity: int
) -> int:

    # Your implementation here


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
