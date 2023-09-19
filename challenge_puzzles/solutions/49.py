def solve_climbing_stairs_problem(total_stairs: int) -> int:
    if total_stairs == 0:
        return 0
    if total_stairs == 1:
        return 1
    if total_stairs == 2:
        return 2

    num_combinations = [0] * (total_stairs + 1)
    num_combinations[0] = 0
    num_combinations[1] = 1
    num_combinations[2] = 2

    for num_stairs in range(3, total_stairs + 1):
        num_combinations[num_stairs] = (
            num_combinations[num_stairs - 1] + num_combinations[num_stairs - 2]
        )
    return num_combinations[-1]


print(solve_climbing_stairs_problem(4))
print(solve_climbing_stairs_problem(10))
print(solve_climbing_stairs_problem(0))


# Bonus #1
def solve_climbing_stairs_problem_with_output(total_stairs: int) -> list[list[int]]:
    if total_stairs == 0:
        return []
    if total_stairs == 1:
        return [[1]]
    if total_stairs == 2:
        return [[1, 1], [2]]

    num_combinations = [[] for _ in range(total_stairs + 1)]
    num_combinations[0] = []
    num_combinations[1] = [[1]]
    num_combinations[2] = [[1, 1], [2]]

    for num_stairs in range(3, total_stairs + 1):
        for seq in num_combinations[num_stairs - 1]:
            num_combinations[num_stairs].append(seq + [1])
        for seq in num_combinations[num_stairs - 2]:
            num_combinations[num_stairs].append(seq + [2])

    return num_combinations[-1]


print(solve_climbing_stairs_problem_with_output(4))
print(solve_climbing_stairs_problem_with_output(10))
print(solve_climbing_stairs_problem_with_output(0))


# Bonus #2
def solve_climbing_stairs_problem_with_three_steps_allowed(total_stairs: int) -> int:
    if total_stairs == 0:
        return 0
    if total_stairs == 1:
        return 1
    if total_stairs == 2:
        return 2
    if total_stairs == 3:
        return 4

    num_combinations = [0] * (total_stairs + 1)
    num_combinations[0] = 0
    num_combinations[1] = 1
    num_combinations[2] = 2
    num_combinations[3] = 4

    for num_stairs in range(4, total_stairs + 1):
        num_combinations[num_stairs] = (
            num_combinations[num_stairs - 1]
            + num_combinations[num_stairs - 2]
            + num_combinations[num_stairs - 3]
        )

    return num_combinations[total_stairs]


print(solve_climbing_stairs_problem_with_three_steps_allowed(4))
print(solve_climbing_stairs_problem_with_three_steps_allowed(10))
print(solve_climbing_stairs_problem_with_three_steps_allowed(0))
