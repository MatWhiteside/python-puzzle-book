def check_tic_tac_toe(board: list[list[str]]) -> str | None:
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


print(check_tic_tac_toe([["X", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(check_tic_tac_toe([["X", "O", "O"], ["O", "X", ""], ["X", "", "X"]]))
print(check_tic_tac_toe([["X", "O", "O"], ["O", "O", ""], ["X", "O", "O"]]))
print(check_tic_tac_toe([["X", "O", "O"], ["O", "X", ""], ["X", "O", "O"]]))
