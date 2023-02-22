def climb_stairs(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


print(climb_stairs(4))


# Challenge #1
def climb_stairs_with_output(n: int) -> list[list[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1, 1], [2]]

    dp = [[] for _ in range(n)]
    dp[0] = [[1]]
    dp[1] = [[1, 1], [2]]

    for i in range(2, n):
        for seq in dp[i - 1]:
            dp[i].append(seq + [1])
        for seq in dp[i - 2]:
            dp[i].append(seq + [2])

    return dp[-1]


print(climb_stairs_with_output(4))
print(climb_stairs_with_output(0))


# Challenge #2
def climb_stairs_with_three_steps_allowed(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]


print(climb_stairs_with_three_steps_allowed(4))
