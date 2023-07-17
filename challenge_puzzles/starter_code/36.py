# Example:
A = [[2, 3], [4, 5]]
B = [[10, 15], [5, 1]]
# C = [[0, 0], [0, 0]]

# C[0][0] = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
# C[0][1] = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
# C[1][0] = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
# C[1][1] = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])

# Output: [[35, 33], [65, 65]]


def matrix_multiply(
    left_matrix: list[list[int]], right_matrix: list[list[int]]
) -> list[list[int]]:

    # Your implementation here


print(matrix_multiply(A, B))
print(matrix_multiply([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]))
print(matrix_multiply([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]], [[1, 2, 3]]))
