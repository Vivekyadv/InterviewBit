# Determine if a Sudoku is valid. The Sudoku board could be partially filled, 
# where empty cells are filled with the character '.'.

# Logic: for every integer in board, check in rows, columns and subBox
# index for subBox is calculated by indx =  (rows//3)*3 + (colm//3)
def isValidSudoku(board):
    n = len(board)
    rows = [set() for _ in range(n)]
    colm = [set() for _ in range(n)]
    subBox = [set() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            curr = board[i][j]
            if curr != '.':
                subBoxIndx = (i//3)*3 + (j//3)
                if curr in rows[i] or curr in colm[j] or curr in subBox[subBoxIndx]:
                    return 0
                else:
                    rows[i].add(curr)
                    colm[j].add(curr)
                    subBox[subBoxIndx].add(curr)
    return 1

board = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", 
"7...2...6", ".6....28.", "...419..5", "....8..79"]
print(isValidSudoku(board))