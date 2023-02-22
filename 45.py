def knapsack(items: list[tuple[int, int]], max_weight: int) -> int:
    # Create a matrix to store the maximum value at each weight
    dp = [[0 for x in range(max_weight + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for w in range(1, max_weight + 1):
            if items[i - 1][0] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][0]] + items[i - 1][1])

    return dp[len(items)][max_weight]


# [(weight, value), ...]
items = [(5, 2), (1, 1000), (100, 1), (25, 25), (2, 1000)]
max_weight = 5
print(knapsack(items, max_weight))
