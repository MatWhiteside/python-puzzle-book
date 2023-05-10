def get_tic_tac_toe_winner(input_board: list[list[str]]) -> str | None:
    # Check rows
    for row in input_board:
        if row[0] == row[1] == row[2]:
            return row[0]

    # Check columns
    for i in range(3):
        if input_board[0][i] == input_board[1][i] == input_board[2][i]:
            return input_board[0][i]

    # Check diagonals
    if input_board[0][0] == input_board[1][1] == input_board[2][2]:
        return input_board[0][0]
    if input_board[0][2] == input_board[1][1] == input_board[2][0]:
        return input_board[0][2]

    return None


print(get_tic_tac_toe_winner([["X", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "X", ""], ["X", "", "X"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "O", ""], ["X", "O", "O"]]))
print(get_tic_tac_toe_winner([["X", "O", "O"], ["O", "X", ""], ["X", "O", "O"]]))
