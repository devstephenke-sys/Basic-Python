def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True  # solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # backtrack

    return False
import random

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill diagonal 3x3 boxes
    for i in range(0, 9, 3):
        fill_box(board, i, i)

    # Solve board to get a full solution
    solve(board)

    # Remove numbers to create puzzle
    remove_numbers(board, 40)  # remove 40 cells
    return board


def fill_box(board, row, col):
    nums = list(range(1, 10))
    random.shuffle(nums)
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = nums.pop()


def remove_numbers(board, count):
    removed = 0
    while removed < count:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            removed += 1

if __name__ == "__main__":
    print("=== Sudoku Generator + Solver ===\n")
    sudoku_board = generate_board()
    print("Sudoku Puzzle:")
    print_board(sudoku_board)

    input("\nPress Enter to solve the puzzle...")

    solve(sudoku_board)
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
