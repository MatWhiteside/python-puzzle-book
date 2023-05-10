def find_adjacent_nodes(adj_matrix: list[list[int]], start_node: int) -> list[int]:
    return [i for i, is_connected in enumerate(adj_matrix[start_node]) if is_connected]


print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 0))
print(find_adjacent_nodes([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 1))
print(find_adjacent_nodes([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]], 1))
