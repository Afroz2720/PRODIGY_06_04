def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, row, col):
    # Check the row
    if num in board[row]:
        return False
    
    # Check the column
    if num in (board[i][col] for i in range(len(board))):
        return False

    # Check the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row_start + i][box_col_start + j] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Backtrack

    return False

def main():
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku Board:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku Board:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
