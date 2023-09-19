def solve_knapsack_problem(items: list[tuple[int, int]], knapsack_capacity: int) -> int:
    # Start the recursive call from the last item
    return knapsack_recursive(items, len(items), knapsack_capacity)

def knapsack_recursive(items: list[tuple[int, int]], index: int, remaining_capacity: int) -> int:
        # Base case: If we have considered all items or if the capacity is zero
        if index == 0 or remaining_capacity == 0:
            return 0
        
        # Get the weight and value of the current item
        weight, value = items[index - 1]
        
        # If the current item's weight is more than the remaining capacity,
        # we can't include it
        if weight > remaining_capacity:
            return knapsack_recursive(items, index - 1, remaining_capacity)
        
        # Otherwise, we have two choices:
        # 1. Include the current item and recursively check the remaining capacity
        include_current = value + knapsack_recursive(items, index - 1, remaining_capacity - weight)
        
        # 2. Exclude the current item and recursively check the next item
        exclude_current = knapsack_recursive(items, index - 1, remaining_capacity)
        
        # Return the maximum value of the two choices
        return max(include_current, exclude_current)

items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 5
print(solve_knapsack_problem(items, max_weight))

items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 0
print(solve_knapsack_problem(items, max_weight))

items = []
max_weight = 5
print(solve_knapsack_problem(items, max_weight))



def solve_knapsack_problem_bonus(items: list[tuple[int, int]], knapsack_capacity: int) -> int:
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
print(solve_knapsack_problem_bonus(items, max_weight))

items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 0
print(solve_knapsack_problem_bonus(items, max_weight))

items = []
max_weight = 5
print(solve_knapsack_problem_bonus(items, max_weight))
