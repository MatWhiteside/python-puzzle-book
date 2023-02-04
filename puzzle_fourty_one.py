def knapsack(items, max_weight):
    # Create a matrix to store the maximum value at each weight
    dp = [[0 for x in range(max_weight + 1)] for y in range(len(items) + 1)]
  
    for i in range(1, len(items) + 1):
        for w in range(1, max_weight + 1):
            if items[i-1][1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][1]] + items[i-1][0])
  
    return dp[len(items)][max_weight]

items = [(60, 10), (100, 20), (120, 30)]
max_weight = 50
print(knapsack(items, max_weight))