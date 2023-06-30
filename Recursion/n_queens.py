def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if n_queens_solver(board, 0, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

def n_queens_solver(board, col, n):
    if col >= n:
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if n_queens_solver(board, col + 1, n):
                return True

            board[row][col] = 0

    return False

def is_safe(board, row, col, n):
    # Check row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

# Example for 4-Queens problem
solve_n_queens(5)
