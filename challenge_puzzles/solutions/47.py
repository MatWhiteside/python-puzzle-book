def solve_maze(
    maze: list[list[int]], start_pos: tuple[int, int], end_pos: tuple[int, int]
) -> bool:

    num_rows, num_cols = len(maze), len(maze[0])
    queue = []
    queue.append(start_pos)
    maze[start_pos[1]][start_pos[0]] = 2

    while queue:
        curr_x, curr_y = queue.pop(0)

        if curr_x == end_pos[0] and curr_y == end_pos[1]:
            return True

        for exploring_x, exploring_y in [
            (curr_x + 1, curr_y),
            (curr_x - 1, curr_y),
            (curr_x, curr_y + 1),
            (curr_x, curr_y - 1),
        ]:
            if (
                0 <= exploring_x < num_cols
                and 0 <= exploring_y < num_rows
                and maze[exploring_y][exploring_x] == 0
            ):
                queue.append((exploring_x, exploring_y))
                maze[exploring_y][exploring_x] = 2

    return False


start = (0, 0)
end = (1, 2)

solvable_maze = [
    [0, 1, 1], 
    [0, 0, 1], 
    [1, 0, 1]
]

print(solve_maze(solvable_maze, start, end))


start = (1, 0)
end = (1, 9)

solvable_maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(solve_maze(solvable_maze, start, end))

unsolvable_maze = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(solve_maze(unsolvable_maze, start, end))
