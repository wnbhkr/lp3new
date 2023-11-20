def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == "Q":
            return False

    return True


def solve_queens(board, row):
    if row == len(board):
        # All queens are placed successfully, print the solution
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = "Q"

            # Recur to place queens in the remaining rows
            solve_queens(board, row + 1)

            # Backtrack - remove the queen for the current position
            board[row][col] = "."


def eight_queens():
    # Initialize an 8x8 chessboard
    chessboard = [["." for _ in range(8)] for _ in range(8)]

    # Place the first queen (can be placed anywhere in the first row for this example)
    chessboard[0][0] = "Q"

    # Start solving the 8-Queens problem using backtracking
    solve_queens(chessboard, 1)


# Run the program
eight_queens()














#orrrrrrrrrrrrrr




import time

def solveNQueenUtils(board,cols,diag1,diag2,col,n):
    if(col >= n):
        return True 
    
    for row in range(n):
        if(cols[row] == 0 and diag1[row+col] == 0 and diag2[n+col-row-1] == 0):
            board[row][col] = 1 
            cols[row] = diag1[row+col] = diag2[n+col-row-1] = 1
            if(solveNQueenUtils(board,cols,diag1,diag2,col+1,n)):
                return True 
            
            board[row][col] = 0
            cols[row] = diag1[row+col] = diag2[n+col-row-1] = 0
            
    return False

def solveNQueen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    cols = [0]*n 
    diag1 = [0]*(2*n-1)
    diag2 = [0]*(2*n-1)
    
    if(solveNQueenUtils(board,cols,diag1,diag2,0,n)):
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print("\n")
        return True 
    return False 


n = int(input("Enter The Value of N : "))
start = time.time()
if not solveNQueen(n):
    print("No Solution Exist")
end = time.time()
print("Time Complexity: ",end-start)