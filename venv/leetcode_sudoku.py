
def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    for row in range(9):
        for column in range(9):
            if board[row][column] == '.':
                for numb in range(1,10):
                    if possible(row, column, numb):
                        board[row][column] = str(numb)
                        if solveSudoku(board):
                            return True
                        board[row][column] = '.'
                return False
    print(board)
    return True

def possible(row, column, numb):
    n = str(numb)
    for i in range(9):
        if board[row][i] == n:
            return False
        elif board[i][column] == n:
            return False
        x0 = (row // 3) * 3
        y0 = (column // 3) * 3
        for j in range(0, 3):
            for k in range(0, 3):
                if board[x0 + j][y0 + k] == n:
                    return False
    return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solveSudoku(board)
    print(board)