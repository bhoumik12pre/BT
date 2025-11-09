# Program: N-Queens Problem using Backtracking
# Aim: To design an N×N chessboard with one queen placed initially and
# use backtracking to safely place the remaining queens.

# --- Logic ---
# We must place N queens on an N×N chessboard such that no two queens attack each other.
# A queen attacks along the same row, column, and both diagonals.
# Backtracking will be used to try possible placements and undo wrong choices.

# --- Function to print the current chessboard ---
def print_board(board):                        # Function to display the board in matrix form
    for row in board:                          # Loop through each row of the board
        print(" ".join(str(x) for x in row))   # Print each element (0 or 1) separated by space
    print()                                    # Print an empty line for clarity


# --- Function to check if placing a queen is safe at a given position ---
def is_safe(board, row, col, n):
    # Check vertically above (same column)
    for i in range(row):                       # Loop through all previous rows
        if board[i][col] == 1:                 # If there is a queen in same column
            return False                       # Position not safe

    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:                   # If a queen found in diagonal
            return False                       # Not safe to place

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:                   # If a queen found in that diagonal
            return False                       # Not safe

    # If all checks passed → safe position
    return True


# --- Recursive Backtracking Function ---
def solve_nqueens(board, row, n):
    # Base case: if all queens are placed successfully
    if row >= n:                               # Means we have placed queens in all rows
        print("\nOne of the possible solutions:")   # Print heading for the found solution
        print_board(board)                     # Display the board configuration
        return True                            # Return True to indicate solution found

    # Try placing queen in each column of the current row
    for col in range(n):                       # For every column in the current row
        if is_safe(board, row, col, n):        # Check if placing queen here is safe
            board[row][col] = 1                # Place the queen (mark position as 1)
            # Recursively try to place the rest of the queens
            if solve_nqueens(board, row + 1, n):   # Move to next row
                return True                    # If solution found, stop further searching
            board[row][col] = 0                # Backtrack: remove queen (undo the move)

    # If queen cannot be placed in any column in this row
    return False


# --- Main Program ---
n = int(input("Enter the size of the chessboard (N): "))    # Input board size (N×N)

# Step 1: Create an N×N board initialized with 0s (empty positions)
board = [[0 for _ in range(n)] for _ in range(n)]           # Matrix of zeros

# Step 2: Ask user for position of first queen
first_col = int(input("Enter the column number (0 to N-1) to place the first Queen: "))
board[0][first_col] = 1                                     # Place first queen at row 0, given column

print("\nInitial board with first Queen placed:")           # Display initial configuration
print_board(board)

# Step 3: Call backtracking function starting from second row
if not solve_nqueens(board, 1, n):                          # Try to place remaining queens
    print("No solution exists for this configuration.")      # If no arrangement possible
