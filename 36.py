# Example:
A = [[2, 3], [4, 5]]
B = [[10, 15], [5, 1]]
# C = [[0, 0], [0, 0]]

# C[0][0] = (A[0][0] * B[0][0]) + (A[0][1] * B[1][0])
# C[0][1] = (A[0][0] * B[0][1]) + (A[0][1] * B[1][1])
# C[1][0] = (A[1][0] * B[0][0]) + (A[1][1] * B[1][0])
# C[1][1] = (A[1][0] * B[0][1]) + (A[1][1] * B[1][1])

# Output: [[35, 33], [65, 65]]


def matrix_multiply(left, right):
    left_num_rows = len(left)
    left_num_cols = len(left[0])
    right_num_cols = len(right[0])

    result = [[0 for _ in range(left_num_rows)] for _ in range(left_num_rows)]

    for i in range(left_num_rows):
        for j in range(right_num_cols):
            for k in range(left_num_cols):
                result[i][j] += left[i][k] * right[k][j]
    return result


print(matrix_multiply(A, B))
