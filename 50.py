def min_coins(coins: list[int], target: int) -> int:
    dp = [float("inf")] * (target + 1)
    dp[0] = 0
    for t in range(1, target + 1):
        for c in coins:
            if t - c >= 0:
                dp[t] = min(dp[t], dp[t - c] + 1)
    return dp[target]


print(min_coins([1, 6], 6))
print(min_coins([1, 2], 6))
print(min_coins([2, 1], 13))
