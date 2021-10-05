import numpy
class Solution(object):
    """
          :type board: List[List[str]]
          :rtype: None Do not return anything, modify board in-place instead.
    """
    def solveSudoku(self, board):
        numbers = ['1', '2','3', '4','5','6','7','8','9']
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    for numb in numbers:
                        if self.possible(row, column, numb):
                            board[row][column] = numb
                            self.solveSudoku(board)
                            board[row][column] = '.'
                    return
        print(numpy.matrix(board))
        return


    def possible(self, row, column, numb):
        for i in range(9):
            if board[row][i] == numb:
                return False
            elif board[i][column] == numb:
                return False
            x0 = (row//3)*3
            y0 = (column//3)*3
            for i in range(0,3):
                for j in range(0,3):
                    if board[x0 + i][y0 + j] == numb:
                        return False
        return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    solution.solveSudoku(board)