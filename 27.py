def find_adjacent_nodes(adj_matrix, start_node):
    adj_nodes = []
    for i, val in enumerate(adj_matrix[start_node]):
        if val == 1:
            adj_nodes.append(i)
    return adj_nodes

print(find_adjacent_nodes([
    [1, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
], 0))