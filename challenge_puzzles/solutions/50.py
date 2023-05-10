def solve_coin_change_problem(coin_values: list[int], target_amount: int) -> int:

    if target_amount == 0:
        return 0

    if coin_values == []:
        return -1

    min_num_coins = [float("inf")] * (target_amount + 1)
    min_num_coins[0] = 0

    for current_target_amount in range(1, target_amount + 1):
        for current_coin_value in coin_values:

            if current_target_amount - current_coin_value >= 0:
                min_num_coins[current_target_amount] = min(
                    min_num_coins[current_target_amount],
                    min_num_coins[current_target_amount - current_coin_value] + 1,
                )

    return int(min_num_coins[target_amount])


print(solve_coin_change_problem([1, 6], 6))
print(solve_coin_change_problem([1, 2], 6))
print(solve_coin_change_problem([2, 1], 13))
print(solve_coin_change_problem([], 6))
print(solve_coin_change_problem([], 0))
